from utility_functions import *

# demonstration of the butterworth filter

# white noise
A = np.random.normal(0, 0.05, size=100000)
f = np.linspace(0, 10000, 50001)
y = rfft(A)

fig, ax = plt.subplots()
plt.plot(np.log10(f[1:]), 10 * np.log10(np.abs(y[1:]**2)), linewidth=0.5, c='k', label='Unfiltered')
# plt.xlabel("log Frequency", fontsize=16)
# plt.ylabel("Power (dB)", fontsize=16)
# ax.tick_params(axis='both', labelsize=15)
# fig.set_size_inches(14, 10)
# plt.tight_layout()
# plt.show()
sf.write(f"audio/white.wav", irfft(y), 20000)


y_filtered = rfft(butter_data(A, band_pass_butterworth, 2, [100,1000]))
# fig, ax = plt.subplots()
plt.plot(np.log10(f[1:]), 10 * np.log10(np.abs(y_filtered[1:]**2)), linewidth=0.5, c='maroon', label='Filtered')
plt.xlabel("log Frequency", fontsize=16)
plt.ylabel("Power (dB)", fontsize=16)
ax.tick_params(axis='both', labelsize=15)
fig.set_size_inches(14, 10)
plt.tight_layout()
plt.legend(fontsize=15)
plt.show()
sf.write(f"audio/white_filtered_2_100_1000.wav", irfft(y_filtered), 20000)