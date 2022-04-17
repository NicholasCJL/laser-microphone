from utility_functions import *

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
    plt.plot(f[1:], np.log10(np.abs(y[1:]) ** 2), c='k', linewidth=0.5)
    plt.xlabel("Frequency", fontsize=16)
    plt.ylabel("Power (dB)", fontsize=16)
    ax.tick_params(axis='both', labelsize=15)
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    plt.show()
    sf.write(f"{out_path}/background_original{i}.wav", data, 20000)

fig, ax = plt.subplots()
plt.plot(f[1:], np.log10(np.abs(y_total[1:] / 3) ** 2), linewidth=0.5)
plt.xlabel("Frequency", fontsize=16)
plt.ylabel("Power (dB)", fontsize=16)
ax.tick_params(axis='both', labelsize=15)
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.show()
sf.write(f"{out_path}/background_mixed.wav", irfft(y_total / 3), 20000)