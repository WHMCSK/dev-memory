import librosa
import librosa.display
import matplotlib.pyplot as plt

# y, sr = librosa.load('../assets/聆小珊-乘客们，请给需要帮助的乘客让个座，谢谢。车辆起步请拉好扶手，投币后，请配合朝里走。下一站终点站。.wav')

y, sr = librosa.load('../assets/伊万卡_CVA01-Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech.wav')

################## 绘制采样信号图 #################

plt.figure(1)
plt.plot(y)
plt.title('Signal')
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.savefig('音频频率图.png')

print(y.shape)
print(sr)
print(len(y))


################## 绘制频率振幅特征图 #################

import numpy as np

n_fft = 2048
ft = np.abs(librosa.stft(y[: n_fft], hop_length = n_fft + 1))
plt.figure(2)
plt.plot(ft)
plt.title('Spectrum')
plt.xlabel('Frequency Bin')
plt.ylabel('Amplitude')
plt.savefig('spectrum_tmp.png')

################## 绘制频谱图（测试） #################
import librosa.display

# ...（前面的代码不变）

# 绘制频谱图
plt.figure(3)
librosa.display.specshow(librosa.amplitude_to_db(np.abs(ft), ref=np.max), sr=sr, x_axis='time', y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrum')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.savefig('spectrum.png')


################## 绘制频谱图 #################

plt.figure(4)
spec = np.abs(librosa.stft(y, hop_length=n_fft))
spec = librosa.amplitude_to_db(spec, ref=np.max)
librosa.display.specshow(spec, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.savefig('spectrogram.png')


################## Mel Spectrogram #################

# 绘制Mel频谱图
plt.figure(5, figsize=(10, 6))
spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024)
mel_spect = librosa.power_to_db(spect, ref=np.max)
librosa.display.specshow(mel_spect, y_axis='mel', fmax=8000, x_axis='time')
plt.title('Mel Spectrogram')
plt.colorbar(format='%+2.f dB')
plt.savefig('mel_spectrogram.png')

################## Mel Scale #################

import numpy as np
import matplotlib.pyplot as plt
import librosa

# 设置线性频率范围，例如从20Hz到20kHz
fmin = 0
fmax = 22050
n_mels = 128  # 设置梅尔滤波器的数量

# 使用librosa的melspectrogram函数来获取梅尔刻度
mels = librosa.mel_frequencies(n_mels=n_mels, fmin=fmin, fmax=fmax)

# 绘制梅尔刻度
plt.figure(6)
plt.plot(mels, label='Mel Scale')
plt.xscale('log')  # 设置x轴为对数尺度，以更好地展示低频和高频之间的关系
plt.xlabel('Frequency (Hz)')
plt.ylabel('Mel')
plt.title('Mel Scale')
plt.legend()
plt.grid(True)
plt.savefig('Mel Scale.png')
plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# import librosa.display
 
# plt.figure(6)

# # 生成一些数据用于绘图
# x = np.linspace(0, 20000, 1000)
# data = np.sin(x * np.pi * 2 * (697 / 1000.0 + 1 / 10.0 * np.arange(10)))
 
# # 绘制梅尔刻度
# plt.figure()
# librosa.display.mel_freqs(sr=22050, n_mels=128, fmin=0, fmax=8000)
 
# # 绘制数据
# plt.plot(x, data)
# plt.show()