import numpy as np
import matplotlib.pyplot as plt
import librosa
from librosa.feature import chroma_cqt
from librosa.display import specshow
import json
import os
from PIL import Image

# %matplotlib inline

print("Inicio:\n")

### Abre a lista de músicas e informações
filename = 'audios\\list.json'
with open(filename, 'r') as f:
    data = json.load(f)


for musica in data["list"]:

    mudança = False

    print(musica["name"])
    print(" ")

    ### leitura da música
    y, sr = librosa.load("audios\\"+musica["name"]+"."+musica["type"])
    ### tamanho da musica
    lenght = y.size * sr

    ### Detecção do tempo da música
    ### Como usar esse tempo pra recortar a imagem?
    ### indica o tempo para a música em questão no arquivo json somente se o valor no arquivo
    ### for igual a zero. Senão, é dispensado a mudança
    if musica["tempo"] == 0:
        tempo_estimado = librosa.beat.tempo(y,sr)
        print (tempo_estimado[0])
        musica["tempo"] = tempo_estimado[0]
        mudança = True

    ### execução da transformada
    chroma = chroma_cqt(y, cqt_mode='full')

    ### criação da imagem base - chromograma completo
    plt.axis('off')
    plt.margins(0)
    specshow(chroma,bins_per_octave=12)

    ### salva o arquivo de imagem - chromograma completo
    plt.savefig("images\\"+musica["name"]+"_whole.png", bbox_inches='tight', pad_inches=0)

    ### Cria um diretório com o nome da música, para salvar as imagens recortadas
    os.mkdir("images\\"+musica["name"])

    ### recupera as dimensões (em pixel) do chromograma
    img = Image.open("images\\"+musica["name"]+"_whole.png")
    width, height = img.size
    
    ## coordenada inicial, para os recortes
    stage = 0
    indice = 0
    ## espessura da faixa a ser extraída
    ## necessita analisar, utilizando o tempo da musica
    step = 4

    ### While que varre a foto, recortando faixas e criando imagens 
    while stage+step <= width:
        img_cut=img.crop((stage,0,stage+step,height))
        img_cut.save("images\\"+musica["name"]+"\\%s.png"%indice,"png")

        ### Varre a foto de step em step
        stage += step
        indice += 1

### Reescreve o arquivo lista com o tempo correto da música se ocorrer uma mudança no arquivo
### mudança no arquivo é indicado por uma flag MUDANÇA
if mudança == True:
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

