from utility_functions import *
from operator import add

in_path = "180322"
filename = "C4sweep0000"
out_path = "audio"

c_list = ['r', 'g', 'b']

eq = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(3):
    data = subtract_mean(get_data(f"{in_path}/{filename}{i}.csv"))
    data = np.array(data, dtype='float64')
    y, f = get_fft(data)
    if i == 0:
        y_total = y
    else:
        y_total += y
    # band pass filter from 200 Hz to 1150 Hz
    data_filtered = butter_data(data, band_pass_butterworth, 2, [200, 1150])
    y_filtered = rfft(data_filtered)
    fig, ax = plt.subplots()
    plt.plot(np.log10(f[1:]), 10 * np.log10(np.abs(y_filtered[1:]) ** 2), c=c_list[i], linewidth=0.5)
    plt.xlabel("log Frequency", fontsize=16)
    plt.ylabel("Power (dB)", fontsize=16)
    ax.tick_params(axis='both', labelsize=15)
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    plt.show()
    sf.write(f"{out_path}/sweep_filtered{i}_100_750_2.wav", data_filtered, 20000)
    eq = list(map(add, eq, [sum(np.abs(y_filtered[(5 * i)-200:(5 * i)+200])**2) for i in range(250, 601, 50)]))

print(eq)
print(y_filtered.size)
for i in range(8):
    print(250 + 50 * i, 5 * (250 + 50 * i), max(eq) / eq[i])
    print(y_filtered[5 * (250 + 50 * i)], "Before")
    peak = (max(eq) / eq[i]) ** 0.5
    curve = np.array([gaussian(i, peak-1, 200, 5) + 1 for i in range(400)])
    # print(curve)
    y_filtered[(5 * (250 + 50 * i))-25:(5 * (250 + 50 * i)+25)] *= peak
    print(y_filtered[5 * (250 + 50 * i)], "After")
print(y_filtered.size)
fig, ax = plt.subplots()
plt.plot(np.log10(f[1:]), 10 * np.log10(np.abs(y_filtered[1:]) ** 2), c='k', linewidth=0.5)
plt.xlabel("log Frequency", fontsize=16)
plt.ylabel("Power (dB)", fontsize=16)
ax.tick_params(axis='both', labelsize=15)
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.show()
sf.write(f"{out_path}/sweep_filtered_100_750_2_modulated.wav", irfft(y_filtered), 20000)

# fig, ax = plt.subplots()
# plt.plot(np.log10(f[1:]), 10 * np.log10(np.abs(y_total[1:] / 3) ** 2), c='k', linewidth=0.5)
# plt.xlabel("log Frequency", fontsize=16)
# plt.ylabel("Power (dB)", fontsize=16)
# ax.tick_params(axis='both', labelsize=15)
# fig.set_size_inches(14, 10)
# plt.tight_layout()
# plt.show()
# sf.write(f"{out_path}/sweep_mixed.wav", irfft(y_total / 3), 20000)
