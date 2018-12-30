import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt

#Opening audio file
audio_path = './techno.wav'
x, sr = librosa.load(audio_path, sr=44100)
print(x.shape, sr)

#playing sound file
ipd.Audio(audio_path)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)

print('Reaches the end')


