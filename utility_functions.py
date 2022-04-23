import csv
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import rfft, rfftfreq, irfft
import os

def gaussian(x, peak, mean, std):
    return peak * np.exp(-(x-mean)**2/(2*std**2))

def band_pass_butterworth(order, cutoff, sample_rate):
    nyq = 0.5 * sample_rate
    low = cutoff[0] / nyq
    high = cutoff[1] / nyq
    return signal.butter(order, [low, high], analog=False, btype='band', output='sos')

def high_pass_butterworth(order, cutoff, sample_rate):
    return signal.butter(order, cutoff, analog=False, output='sos', fs=sample_rate)

def low_pass_butterworth(order, cutoff, sample_rate):
    return signal.butter(order, cutoff, analog=False, output='sos', fs=sample_rate)

def butter_data(data, filter, order, cutoff, sample_rate=20000):
    # applies filter(order, cutoff, sample_rate) to data
    sos = filter(order, cutoff, sample_rate)
    return signal.sosfilt(sos, data)

def get_fft(data):
    return rfft(data), rfftfreq(data.size, d=1./20000)

def get_data(filename):
    output = []
    with open(filename, "r") as file:
        r = csv.reader(file)
        rows = list(r)
        rows = rows[5:]
        for row in rows:
            output.append(float(row[1]))

    return output

def subtract_mean(data):
    return data - np.mean(data)

def subtract_median(data):
    return data - np.median(data)

def main():
    in_path = "110322"
    filename = "C4background0000"
    out_path = "audio"
    target_freq = 5000

    for i in range(3):
        data = subtract_mean(get_data(f"{in_path}/{filename}{i}.csv"))
        data = np.array(data, dtype='float64')
        y, f = get_fft(data)
        if i == 0:
            y_total = y
        else:
            y_total += y
        print(f.size)
        fig, ax = plt.subplots()
        plt.plot(f[1:], np.log10(np.abs(y[1:])**2), c='k', linewidth=0.5)
        plt.xlabel("Frequency", fontsize=16)
        plt.ylabel("Power (dB)", fontsize=16)
        ax.tick_params(axis='both', labelsize=15)
        fig.set_size_inches(14, 10)
        plt.tight_layout()
        plt.show()
        sf.write(f"{out_path}/background_original{i}.wav", data, 20000)

    fig,ax = plt.subplots()
    plt.plot(f[1:], np.log10(np.abs(y_total[1:]/3)**2), linewidth=0.5)
    plt.xlabel("Frequency", fontsize=16)
    plt.ylabel("Power (dB)", fontsize=16)
    ax.tick_params(axis='both', labelsize=15)
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    plt.show()
    sf.write(f"{out_path}/background_mixed.wav", irfft(y_total/3), 20000)

if __name__ == "__main__":
    main()
# data = subtract_mean(get_data(f"{in_path}{filename}"))
# data = np.array(data, dtype="float64")
# # plt.plot(data)
# # plt.show()
# Y = rfft(data)
# X = rfftfreq(len(data), 1/20000)
# plt.plot(X, np.abs(Y))
# plt.show()
# sf.write(f"{out_path}{filename}_original.wav", data, 20000)
# ppf = len(X) / 10000
# min_freq = int(ppf * target_freq)
# Y[min_freq:] = 0
# for i in range(len(Y)):
#     Y[i] *= 0.3 + 500 * (i/len(Y))**4
# plt.plot(X, np.abs(Y))
# plt.show()
# data_filtered = irfft(Y)
# sf.write(f"{out_path}{filename}_filtered.wav", data_filtered, 20000)

"""Obsolete functions"""

def _reduce_dynamic_range(data, iterations=5):
    for _ in range(iterations):
        stddev = np.std(data)
        scaling = 2 * np.max(abs(data))/(np.max(abs(data)) - stddev)
        data *= scaling
        for i in range(len(data)):
            if abs(data[i]) > stddev:
                data[i] = stddev * abs(data[i])/data[i]
    return data