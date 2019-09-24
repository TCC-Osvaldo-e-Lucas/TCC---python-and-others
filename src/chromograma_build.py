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
print(" ")

### Abre a lista de músicas e informações
# filename = 'audios\\list.json' #Lista de músicas
filename = 'audios\\list treino.json' #Lista de audio para treino 1
with open(filename, 'r') as f:
    data = json.load(f)


for musica in data["list"]:

    mudança = False

    ### Checa para ver se a música já foi analisada.
    if os.path.isdir("images\\"+musica["name"]) == False:


        print("Criando imagens e dados sobre "+musica["name"])
        print(" ")

        ### leitura da música
        y, sr = librosa.load("audios\\"+musica["name"]+"."+musica["type"])
        ### tamanho da musica
        if musica["duration"] == 0:
            ### calcula o a duração da música em segundos
            lenght = y.size/sr
            musica["duration"] = lenght
            mudança = True
        ### print dos tamanhos da música
        print("tamanho da música em s: ",musica["duration"])
        length_min = musica["duration"]/60
        print("tamanho da música em m: %s"%length_min)
    


        ### execução da transformada
        chroma = chroma_cqt(y)
        logcqt = librosa.amplitude_to_db(np.abs(chroma))

        #Definição de frequência mínima e máxima de acordo com a amplitude do piano
        fmin = librosa.note_to_hz('A0',round_midi=True)
        fmax = librosa.note_to_hz('C8',round_midi=True)


        ### criação da imagem base - chromograma completo
        plt.axis('off')
        plt.margins(0)
        specshow(chroma, fmin=fmin, fmax=fmax, cmap='coolwarm')
        # specshow(chroma2, x_axis='time', y_axis='log', bins_per_octave=12)
        
        ### Salva o chromograma com o nome padrão
        plt.savefig("images\\"+musica["name"]+"_whole.png", bbox_inches='tight', pad_inches=0)


        ### Detecção do tempo da música
        ### Como usar esse tempo pra recortar a imagem?
        ### indica o tempo para a música em questão no arquivo json somente se o valor no arquivo
        ### for igual a zero. Senão, é dispensado a mudança
        if musica["tempo"] == 0:
            ### tempo estimado em BPM
            tempo_estimado = librosa.beat.tempo(y,sr)
            print ("tempo estimado: ",tempo_estimado[0])
            musica["tempo"] = tempo_estimado[0]
            mudança = True
        
        ### batimentos por segundo
        bps = musica["tempo"]/60
        ### segundos por batimento, considerando um batimento uma semínima
        spb = 1/bps
        ### duração de tempo delta de uma fusa
        delta = spb/8
        ### calcula quantos pixels precisa, para ter um pixel para cada "Fusa"
        pixels_fusa = musica["duration"]/delta

        print("numeros de pixels: ",pixels_fusa)

        ### Cria um diretório com o nome da música, para salvar as imagens recortadas
        ### já que foi constatado que o diretório não existe no inicio do IF
        os.mkdir("images\\"+musica["name"])

        ### recupera as dimensões (em pixel) do chromograma
        img = Image.open("images\\"+musica["name"]+"_whole.png")
        width, height = img.size
    
        ## coordenada inicial, para os recortes
        stage = 0
        indice = 0
        ## espessura da faixa a ser extraída
        ## necessita analisar, utilizando o tempo da musica
        step = 5

        ### While que varre a foto, recortando faixas e criando imagens 
        while stage+step <= width:
            img_cut=img.crop((stage,0,stage+step,height))
            img_cut.save("images\\"+musica["name"]+"\\%s.png"%indice,"png")

            ### Varre a foto de step em step
            stage += step
            indice += 1

    else:
        print(musica["name"]+" já foi analisada. Caso queira refazer a analise, apague a pasta da música em questão antes")
        print (" ")
### Após analisadas todas as músicas da lista, vemos se houve alteração no arquivo Json

### Reescreve o arquivo lista com o tempo correto da música se ocorrer uma mudança no arquivo
### mudança no arquivo é indicado por uma flag MUDANÇA
if mudança == True:
    print("Houve alteração no arquivo Json")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
else:
    print("Não houve alteração no arquivo Json")

print("Fim.")
exit()



### leitura da música
y, sr = librosa.load("audios\\greensleves.wav")
# x, sr2 = librosa.load('Documents/MATLAB/TCC/Py Analise Som/greensleevesFM.wav')

### Detecção do tempo da música
tempo_estimado = librosa.beat.tempo(y,sr)

print(27*53)