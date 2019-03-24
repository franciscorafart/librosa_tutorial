# Needs to run with Jupyter Notebook

import IPython.display as ipd
from librosa import load, display, feature, power_to_db
import matplotlib.pyplot as plt
import numpy as np

# Opening audio file
audio_path = './techno.wav'
x, sr = load(audio_path, sr=44100)
print(x.shape, sr)

# Playing sound file
ipd.Audio(audio_path)

# Displaying wave image
plt.figure(figsize=(14, 5))
display.waveplot(x, sr=sr)

# melspectrogram
S = feature.melspectrogram(x, sr=sr)
log_S = power_to_db(S, ref=np.max)
display.specshow(log_S, x_axis='time', y_axis='chroma')

# Tempo
onset_env = onset.onset_strength(x, sr=sr)
tempo = beat.tempo(onset_env,sr=sr)
print('tempo={}'.format(tempo))

y_harmonic, y_percusive = effects.hpss(x)
tempo, beats = beat.beat_track(y=y_percusive, sr=sr)
print('tempo: {}, beats: {}'.format(tempo,beats))
