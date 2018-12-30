import librosa

audio_path = './techno.wav'
x, sr = librosa.load(audio_path, sr=44100)

print(x.shape, sr)