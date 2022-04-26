from utility_functions import *

type = "seashells"
in_path = "010322/words"
filename = f"C2{type}_500_200_0000"
out_path = "audio/Original/words"

for i in range(10):
    data = subtract_mean(get_data(f"{in_path}/{filename}{i}.csv"))
    data = np.array(data, dtype='float64') * 2
    t = np.linspace(0, 5, 100001)
    y, f = get_fft(data)
    fig, ax = plt.subplots()
    plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y[1:]) ** 2), c='k', linewidth=0.5)
    plt.xlabel("log Frequency", fontsize=19)
    plt.ylabel("Power (dB)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    # plt.ylim([-100, 170])
    # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    # plt.xlim([80, 3000])
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    if i == 1:
        fig.savefig(f"Images/Original/words/NMLM{type}_1.png", dpi=fig.dpi)
    sf.write(f"{out_path}/{type}_{i}.wav", data, 20000)

    fig, ax = plt.subplots()
    plt.plot(t, data, c='k', linewidth=0.5)
    plt.xlabel("Time (s)", fontsize=19)
    plt.ylabel("Voltage (V)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    # plt.ylim([-100, 170])
    # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    # plt.xlim([80, 3000])
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    if i == 1:
        fig.savefig(f"Images/Original/words/NMLM{type}_1_time.png", dpi=fig.dpi)

    filtered = butter_data(data, band_pass_butterworth, 2, [100, 2000])
    y_filtered, f = get_fft(filtered)
    fig, ax = plt.subplots()
    plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y_filtered[1:]) ** 2), c='k', linewidth=0.5)
    plt.xlabel("log Frequency", fontsize=19)
    plt.ylabel("Power (dB)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    # plt.ylim([-100, 170])
    # plt.xlim([80, 3000])
    # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    # plt.show()
    if i == 1:
        fig.savefig(f"Images/Original/words/NMLM{type}_1_filtered.png", dpi=fig.dpi)
    sf.write(f"{out_path}/{type}_{i}_filtered.wav", filtered, 20000)

    fig, ax = plt.subplots()
    plt.plot(t, filtered, c='k', linewidth=0.5)
    plt.xlabel("Time (s)", fontsize=19)
    plt.ylabel("Voltage (V)", fontsize=19)
    ax.tick_params(axis='both', labelsize=17)
    # plt.ylim([-100, 170])
    # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    # plt.xlim([80, 3000])
    fig.set_size_inches(14, 10)
    plt.tight_layout()
    if i == 1:
        fig.savefig(f"Images/Original/words/NMLM{type}_1_time_filtered.png", dpi=fig.dpi)