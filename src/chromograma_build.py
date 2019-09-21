import numpy as np
import matplotlib.pyplot as plt

import librosa
from librosa.feature import chroma_cqt
from librosa.display import specshow
# %matplotlib inline

y, sr = librosa.load(r"C:\Users\Osvaldo\Documents\POLITECNICA\TCC - TrancMusicaPartitura\Python\greensleves.wav")
# x, sr2 = librosa.load('Documents/MATLAB/TCC/Py Analise Som/greensleevesFM.wav')

# print(librosa.beat.tempo(y,sr))
# exit()
chroma = chroma_cqt(y, cqt_mode='full')
# # chroma2 = chroma_cqt(x, cqt_mode='full')

# # specshow(chroma, x_axis='time', y_axis='log', bins_per_octave=12)
# specshow(chroma,bins_per_octave=12)
# plt.savefig('teste_greensleves_cqt_chroma.png')

plt.axis('off')
plt.margins(0)
specshow(chroma,bins_per_octave=12)
plt.savefig('teste2_greensleves_cqt_chroma.png', bbox_inches='tight', pad_inches=0)
# specshow(chroma2, x_axis='time', y_axis='log', bins_per_octave=12)
# plt.savefig('Documents/MATLAB/TCC/Py Analise Som/greensleevesFM_cqt_chroma.png')