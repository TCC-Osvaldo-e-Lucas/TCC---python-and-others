import numpy as np
import matplotlib.pyplot as plt

import librosa
from librosa.feature import chroma_cqt
from librosa.display import specshow
import json
import os
# %matplotlib inline

print("Inicio:\n")

### Abre a lista de músicas e informações
filename = 'audios\\list.json'
with open(filename, 'r') as f:
    data = json.load(f)


for musica in data["list"]:
    print(musica["name"])
    print(" ")
    ### leitura da música
    y, sr = librosa.load("audios\\"+musica["name"])

    ### Detecção do tempo da música
    tempo_estimado = librosa.beat.tempo(y,sr)
    print (tempo_estimado[0])

    ### indica o tempo para a música em questão
    musica["tempo"] = tempo_estimado[0]
    ### execução da transformada
    chroma = chroma_cqt(y, cqt_mode='full')

    ### criação da imagem base - chromograma completo
    plt.axis('off')
    plt.margins(0)
    specshow(chroma,bins_per_octave=12)

    ### salva o arquivo de imagem
    plt.savefig("images\\chromograma_"+musica["name"]+".png", bbox_inches='tight', pad_inches=0)

### Reescreve o arquivo lista com o tempo correto da música
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)


print("Fim.")
exit()



# ### leitura da música
# y, sr = librosa.load("audios\\greensleves.wav")
# # x, sr2 = librosa.load('Documents/MATLAB/TCC/Py Analise Som/greensleevesFM.wav')

# ### Detecção do tempo da música
# tempo_estimado = librosa.beat.tempo(y,sr)

# ### execução da transformada
# chroma = chroma_cqt(y, cqt_mode='full')

# ### criação da imagem base - chromograma completo
# plt.axis('off')
# plt.margins(0)
# specshow(chroma,bins_per_octave=12)
# # specshow(chroma2, x_axis='time', y_axis='log', bins_per_octave=12)

# plt.savefig('imagem_base.png', bbox_inches='tight', pad_inches=0)

