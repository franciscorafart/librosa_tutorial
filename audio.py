import IPython.display as ipd
from librosa import load, display
import matplotlib.pyplot as plt

# Opening audio file
audio_path = './techno.wav'
x, sr = load(audio_path, sr=44100)
print(x.shape, sr)

# Playing sound file
ipd.Audio(audio_path)

# Displaying wave image
plt.figure(figsize=(14, 5))
display.waveplot(x, sr=sr)
