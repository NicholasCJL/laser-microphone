from utility_functions import *

in_path = "110322"
filename = "C4background0000"
out_path = "audio"

c_list = ['r', 'g', 'b']

for i in range(3):
    data = subtract_mean(get_data(f"{in_path}/{filename}{i}.csv"))
    data = np.array(data, dtype='float64')
    y, f = get_fft(data)
    if i == 0:
        y_total = y
        data_total = data
    else:
        y_total += y
        data_total += data
    print(f.size)
    fig, ax = plt.subplots()
    plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y[1:]) ** 2), c=c_list[i], linewidth=0.5)
    plt.xlabel("log Frequency", fontsize=19)
    plt.ylabel("Power (dB)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    plt.ylim([-45, 170])
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    plt.show()
    sf.write(f"{out_path}/background_original{i}.wav", data, 20000)

fig, ax = plt.subplots()
plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y_total[1:] / 3) ** 2), c='k', linewidth=0.5)
plt.xlabel("log Frequency", fontsize=19)
plt.ylabel("Power (dB)", fontsize=19)
ax.tick_params(axis='both', labelsize=17)
plt.ylim([-45, 170])
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.show()
sf.write(f"{out_path}/background_mixed.wav", irfft(y_total / 3), 20000)

fig, ax = plt.subplots()
y, f = get_fft(data_total)
plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y[1:] / 3) ** 2), c='k', linewidth=0.5)
plt.xlabel("log Frequency", fontsize=16)
plt.ylabel("Power (dB)", fontsize=16)
ax.tick_params(axis='both', labelsize=15)
plt.ylim([-45, 170])
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.show()
sf.write(f"{out_path}/background_mixed_average.wav", irfft(y_total / 3), 20000)