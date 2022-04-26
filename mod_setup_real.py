from utility_functions import *
import pathlib

type = "celloNA"
in_path = "180322"
filename = f"C4{type}0000"
out_path = f"audio/Modified2/{type}"

path = pathlib.Path(out_path)
path.mkdir(parents=True, exist_ok=True)

img_path = f"Images/Modified2/{type}"
path_i = pathlib.Path(img_path)
path_i.mkdir(parents=True, exist_ok=True)

background_noise = subtract_mean(get_data("110322/C4background00000.csv"))
background_noise = np.array(background_noise, dtype='float64') * 0.2

for i in range(4):
    data = subtract_mean(get_data(f"{in_path}/{filename}{i}.csv"))
    data = np.array(data, dtype='float64') * 2
    t = np.linspace(0, 5, 100001)
    y, f = get_fft(data)
    if i == 2:
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
        fig.savefig(f"{img_path}/NMLM{type}_2.png", dpi=fig.dpi)
    sf.write(f"{out_path}/{type}_{i}.wav", data, 20000)

    if i == 2:
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
        fig.savefig(f"{img_path}/NMLM{type}_2_time.png", dpi=fig.dpi)

    filtered = butter_data(data, band_pass_butterworth, 2, [100, 2000])
    y_filtered, f = get_fft(filtered)
    if i == 2:
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
        fig.savefig(f"{img_path}/NMLM{type}_2_filtered.png", dpi=fig.dpi)
    sf.write(f"{out_path}/{type}_{i}_filtered.wav", filtered, 20000)

    if i == 2:
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
        fig.savefig(f"{img_path}/NMLM{type}_2_time_filtered.png", dpi=fig.dpi)

    filtered_eq = butter_data(filtered, band_pass_butterworth, 1, [900, 2000]) * 4
    y_filtered, f = get_fft(filtered_eq)
    if i == 2:
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
        fig.savefig(f"{img_path}/NMLM{type}_2_filtered_eq.png", dpi=fig.dpi)
    sf.write(f"{out_path}/{type}_{i}_filtered_eq.wav", filtered_eq, 20000)

    if i == 2:
        fig, ax = plt.subplots()
        plt.plot(t, filtered_eq, c='k', linewidth=0.5)
        plt.xlabel("Time (s)", fontsize=19)
        plt.ylabel("Voltage (V)", fontsize=19)
        ax.tick_params(axis='both', labelsize=17)
        # plt.ylim([-100, 170])
        # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
        # plt.xlim([80, 3000])
        fig.set_size_inches(14, 10)
        plt.tight_layout()
        fig.savefig(f"{img_path}/NMLM{type}_2_time_filtered_eq.png", dpi=fig.dpi)

    # subtract noise test
    # data = subtract_mean(get_data(f"{in_path}/{filename}{i}.csv"))
    # data = np.array(data, dtype='float64') * 0.2
    # t = np.linspace(0, 5, 100000)
    # y, f = get_fft(data)
    # y -= rfft(background_noise)
    # data = irfft(y)
    # if i == 0:
    #     fig, ax = plt.subplots()
    #     plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y[1:]) ** 2), c='k', linewidth=0.5)
    #     plt.xlabel("log Frequency", fontsize=19)
    #     plt.ylabel("Power (dB)", fontsize=19)
    #     ax.tick_params(axis='both', labelsize=17)
    #     # plt.ylim([-100, 170])
    #     # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    #     # plt.xlim([80, 3000])
    #     fig.set_size_inches(14, 10)
    #     plt.tight_layout()
    #     fig.savefig(f"{img_path}/NMLM{type}_0_sb.png", dpi=fig.dpi)
    # sf.write(f"{out_path}/{type}_{i}_sb.wav", data, 20000)
    #
    # if i == 0:
    #     fig, ax = plt.subplots()
    #     plt.plot(t, data, c='k', linewidth=0.5)
    #     plt.xlabel("Time (s)", fontsize=19)
    #     plt.ylabel("Voltage (V)", fontsize=19)
    #     ax.tick_params(axis='both', labelsize=17)
    #     # plt.ylim([-100, 170])
    #     # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    #     # plt.xlim([80, 3000])
    #     fig.set_size_inches(14, 10)
    #     plt.tight_layout()
    #     fig.savefig(f"{img_path}/NMLM{type}_0_time_sb.png", dpi=fig.dpi)
    #
    # filtered = butter_data(data, band_pass_butterworth, 2, [100, 2000])
    # y_filtered, f = get_fft(filtered)
    # if i == 0:
    #     fig, ax = plt.subplots()
    #     plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y_filtered[1:]) ** 2), c='k', linewidth=0.5)
    #     plt.xlabel("log Frequency", fontsize=19)
    #     plt.ylabel("Power (dB)", fontsize=19)
    #     ax.tick_params(axis='both', labelsize=17)
    #     # plt.ylim([-100, 170])
    #     # plt.xlim([80, 3000])
    #     # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    #     fig.set_size_inches(14, 10)
    #     plt.tight_layout()
    #     # plt.show()
    #     fig.savefig(f"{img_path}/NMLM{type}_0_filtered_sb.png", dpi=fig.dpi)
    # sf.write(f"{out_path}/{type}_{i}_filtered_sb.wav", filtered, 20000)
    #
    # filtered_eq = butter_data(filtered, band_pass_butterworth, 1, [900, 1500]) * 4
    # y_filtered, f = get_fft(filtered_eq)
    # if i == 0:
    #     fig, ax = plt.subplots()
    #     plt.plot(np.log10(f[1:]), 20 * np.log10(np.abs(y_filtered[1:]) ** 2), c='k', linewidth=0.5)
    #     plt.xlabel("log Frequency", fontsize=19)
    #     plt.ylabel("Power (dB)", fontsize=19)
    #     ax.tick_params(axis='both', labelsize=17)
    #     # plt.ylim([-100, 170])
    #     # plt.xlim([80, 3000])
    #     # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    #     fig.set_size_inches(14, 10)
    #     plt.tight_layout()
    #     # plt.show()
    #     fig.savefig(f"{img_path}/NMLM{type}_0_filtered_eq_sb.png", dpi=fig.dpi)
    # sf.write(f"{out_path}/{type}_{i}_filtered_eq_sb.wav", filtered_eq, 20000)
    #
    # if i == 0:
    #     fig, ax = plt.subplots()
    #     plt.plot(t, filtered, c='k', linewidth=0.5)
    #     plt.xlabel("Time (s)", fontsize=19)
    #     plt.ylabel("Voltage (V)", fontsize=19)
    #     ax.tick_params(axis='both', labelsize=17)
    #     # plt.ylim([-100, 170])
    #     # plt.axvline(np.log10(freq), c='r', linewidth=1, linestyle='-.')
    #     # plt.xlim([80, 3000])
    #     fig.set_size_inches(14, 10)
    #     plt.tight_layout()
    #     fig.savefig(f"{img_path}/NMLM{type}_0_time_filtered_sb.png", dpi=fig.dpi)