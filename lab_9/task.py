from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from pydub import AudioSegment
from scipy import signal

from core import helpers


def main():
    AudioSegment.converter = r"C:\Program Files\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
    AudioSegment.ffprobe = r"C:\Program Files\ffmpeg-4.4-full_build\bin\ffprobe.exe"
    file = Path(f'{helpers.folder_helper.AUDIO_FOLDER_PATH}/SashaPVoice.wav')
    song = AudioSegment.from_file(file)
    song = song.set_channels(1)
    fs = song.frame_rate
    print(fs)

    samples = song.get_array_of_samples()
    N = 2048 * 1
    f, t, Sxx = signal.spectrogram(np.array(samples), fs, window=signal.windows.hann(N), nfft=N)
    plt.figure(dpi=1200)
    plt.pcolormesh(t, f, np.log10(Sxx + 1e-10))
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.savefig(f'{helpers.folder_helper.IMAGES_FOLDER_PATH}/lol.png')


if __name__ == '__main__':
    main()
