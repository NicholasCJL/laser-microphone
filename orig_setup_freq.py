from utility_functions import *

freq = 700
in_path = "010322/pure frequency"
filename = f"C2{freq}_500_200_"
out_path = "audio/Original/pure frequency"

c_list = ['r', 'g', 'b']

f_index = freq * 5
diff_freq = [0, 0, 0, 0, 0]

for i in range(1, 4):
    data = subtract_mean(get_data(f"{in_path}/{filename}{i}00000.csv"))
    data = np.array(data, dtype='float64') * 2
    y, f = get_fft(data)
    # if i == 1:
    #     y_total = y
    #     data_total = data
    # else:
    #     y_total += y
    #     data_total += data
    # print(f.size)
    fig, ax = plt.subplots()
    plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y[1:]) ** 2), c='k', linewidth=0.5)
    plt.xlabel("log Frequency", fontsize=19)
    plt.ylabel("Power (dB)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    plt.ylim([-100, 170])
    plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    # plt.xlim([80, 3000])
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    # plt.show()
    if i == 1:
        fig.savefig(f"Images/Original/pure frequency/NMLM{freq}Hz_1.png", dpi=fig.dpi)
    diff_freq[i-1] = f[f_index-50:f_index+50][y[f_index-50:f_index+50].argmax()] - freq
    fig, ax = plt.subplots()
    plt.plot(f[1:], 20 * np.log10(np.abs(y[1:]) ** 2), c='k', linewidth=0.5)
    plt.xlabel("Frequency", fontsize=19)
    plt.ylabel("Power (dB)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    plt.ylim([-100, 170])
    plt.xlim([0, 10000])
    plt.axvline(freq, c='r', linewidth=1, linestyle='-.')
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    # plt.show()
    if i == 1:
        fig.savefig(f"Images/Original/pure frequency/NMLM{freq}Hz_1_flat.png", dpi=fig.dpi)
    sf.write(f"{out_path}/{freq}Hz_{i}.wav", data, 20000)
    filtered = butter_data(data, low_pass_butterworth, 2, 2000)
    y_filtered, f = get_fft(filtered)
    fig, ax = plt.subplots()
    plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y_filtered[1:]) ** 2), c='k', linewidth=0.5)
    plt.xlabel("log Frequency", fontsize=19)
    plt.ylabel("Power (dB)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    plt.ylim([-100, 170])
    # plt.xlim([80, 3000])
    plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    # plt.show()
    if i == 1:
        fig.savefig(f"Images/Original/pure frequency/NMLM{freq}Hz_1_filtered.png", dpi=fig.dpi)
    sf.write(f"{out_path}/{freq}Hz_{i}_filtered.wav", filtered, 20000)

diff_avg = sum(diff_freq) / 5
s_var = sum([(diff - diff_avg)**2 for diff in diff_freq]) / 4
print(diff_avg, s_var**0.5, (s_var + (0.2**2)/5)**0.5)

fig, ax = plt.subplots()
plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y_total[1:] / 3) ** 2), c='k', linewidth=0.5)
plt.xlabel("log Frequency", fontsize=19)
plt.ylabel("Power (dB)", fontsize=19)
ax.tick_params(axis='both', labelsize=17)
plt.ylim([-45, 170])
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.show()
sf.write(f"{out_path}/{freq}Hz_mixed.wav", irfft(y_total / 3), 20000)

fig, ax = plt.subplots()
plt.plot(f[1:], 20 * np.log10(np.abs(y_total[1:] / 3) ** 2), c='k', linewidth=0.5)
plt.xlabel("Frequency", fontsize=19)
plt.ylabel("Power (dB)", fontsize=19)
ax.tick_params(axis='both', labelsize=17)
plt.ylim([-45, 170])
plt.xlim([0, 10000])
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
y_filtered = rfft(butter_data(data_total, band_pass_butterworth, 2, [100,1000]))
plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y_filtered[1:] / 3) ** 2), c='k', linewidth=0.5)
plt.xlabel("log Frequency", fontsize=19)
plt.ylabel("Power (dB)", fontsize=19)
ax.tick_params(axis='both', labelsize=17)
plt.ylim([-45, 170])
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.show()
sf.write(f"{out_path}/{freq}Hz_mixed_filtered.wav", irfft(y_total / 3), 20000)
