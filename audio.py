import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy

from librosa import load, display, amplitude_to_db, stft, output

# Opening audio file
audio_path = './techno.wav'
x, sr = load(audio_path, sr=44100)
print(x.shape, sr)

# Playing sound file
ipd.Audio(audio_path)

# Displaying wave image
plt.figure(figsize=(14, 5))
display.waveplot(x, sr=sr)

# Spectogram display
X = stft(x)
Xdb = amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()

# Output audio
new_audio = 'example.wav'
# Modify x to change the array - lower amplitude
altered = [sample * 0.1 for sample in x]
altered_x = numpy.array(altered)

try:
    output.write_wav(new_audio, altered_x, sr)
except:
    print('Could not write file')

new_audio_path = './{}'.format(new_audio)
print(new_audio_path)

# TODO: install audio codecs for new audio path to work
# x, sr = load(new_audio_path, sr=44100)
# print(x.shape, sr, len(x))
ipd.Audio(new_audio_path)
