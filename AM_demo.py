import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def main():
    def gen_sin(f, k, x, t, fps, timescale):
        # generates sin function at time t
        return np.sin(2 * np.pi * f * t / (fps * timescale) - k * x)

    def animate(frame):
        """
        plots <frame> in animation
        :param frame: frame number
        :return: None
        """
        ax.clear()
        plt.axis('off')
        plt.ylim([-4, 4])
        ax.plot(gen_sin(f, k, x, frame, fps, timescale)-2.5, c='k')
        ax.plot((0.5 * (gen_sin(f, k, x, frame, fps, timescale) + 1)
                       * gen_sin(f*carrier_scale, carrier_scale*k, x, frame, fps, timescale)),
                c='firebrick')
        ax.plot(gen_sin(f*carrier_scale, carrier_scale*k, x, frame, fps, timescale) + 2.5, c='red')
        # plt.title(str(frame))
        return

    # plotting setup
    fps = 33
    timescale = 3
    fig, ax = plt.subplots()
    fig.set_dpi(100)
    fig.set_size_inches(12, 9)
    plt.tight_layout()
    mpl.rcParams['animation.ffmpeg_path'] = r'C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe'

    x = np.linspace(0, 1, 10000)
    k = 2 * np.pi / 0.5
    f = 1
    carrier_scale = 20
    animation = FuncAnimation(fig, animate, frames=99, interval=1000/fps, repeat=False)
    animation.save('AM.mp4')

if __name__ == "__main__":
    main()