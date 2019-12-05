import numpy as np
import pandas as pd

n_treino = 10000
n_teste = 3000


array_treino = np.array([])
array_treino = np.append(array_treino, np.random.randint(0, 35, n_treino))

array_teste = np.array([])
array_teste = np.append(array_teste, np.random.randint(0, 35, n_teste))

array_treino_lily = np.array([],dtype = object)
array_teste_lily = np.array([],dtype = object)

for i in range(n_treino):
    if array_treino[i] == 0 :
        array_treino_lily = np.append(array_treino_lily, "c'")
        
    elif array_treino[i] == 1:
        array_treino_lily = np.append(array_treino_lily, "cis'")

    elif array_treino[i] == 2:
        array_treino_lily = np.append(array_treino_lily, "d'")

    elif array_treino[i] == 3:
        array_treino_lily = np.append(array_treino_lily, "dis'")

    elif array_treino[i] == 4:
        array_treino_lily = np.append(array_treino_lily, "e'")

    elif array_treino[i] == 5:
        array_treino_lily = np.append(array_treino_lily, "f'")

    elif array_treino[i] == 6:
        array_treino_lily = np.append(array_treino_lily,  "fis'")

    elif array_treino[i] == 7:
        array_treino_lily = np.append(array_treino_lily,  "g'")

    elif array_treino[i] == 8:
        array_treino_lily = np.append(array_treino_lily,  "gis'")

    elif array_treino[i] == 9:
        array_treino_lily = np.append(array_treino_lily,  "a'")

    elif array_treino[i] == 10:
        array_treino_lily = np.append(array_treino_lily,  "ais'")

    elif array_treino[i] == 11:
        array_treino_lily = np.append(array_treino_lily,  "b'")

    elif array_treino[i] == 12:
        array_treino_lily = np.append(array_treino_lily,  "c''")
        
    elif array_treino[i] == 13:
        array_treino_lily = np.append(array_treino_lily,  "cis''")

    elif array_treino[i] == 14:
        array_treino_lily = np.append(array_treino_lily,  "d''")

    elif array_treino[i] == 15:
        array_treino_lily = np.append(array_treino_lily,  "dis''")

    elif array_treino[i] == 16:
        array_treino_lily = np.append(array_treino_lily,  "e''")

    elif array_treino[i] == 17:
        array_treino_lily = np.append(array_treino_lily,  "f''")

    elif array_treino[i] == 18:
        array_treino_lily = np.append(array_treino_lily,  "fis''")

    elif array_treino[i] == 19:
        array_treino_lily = np.append(array_treino_lily,  "g''")

    elif array_treino[i] == 20:
        array_treino_lily = np.append(array_treino_lily,  "gis''")

    elif array_treino[i] == 21:
        array_treino_lily = np.append(array_treino_lily,  "a''")

    elif array_treino[i] == 22:
        array_treino_lily = np.append(array_treino_lily,  "ais''")

    elif array_treino[i] == 23:
        array_treino_lily = np.append(array_treino_lily,  "b''")

    elif array_treino[i] == 24:
        array_treino_lily = np.append(array_treino_lily,  "c'''")
        
    elif array_treino[i] == 25:
        array_treino_lily = np.append(array_treino_lily,  "cis'''")

    elif array_treino[i] == 26:
        array_treino_lily = np.append(array_treino_lily,  "d'''")

    elif array_treino[i] == 27:
        array_treino_lily = np.append(array_treino_lily,  "dis'''")

    elif array_treino[i] == 28:
        array_treino_lily = np.append(array_treino_lily,  "e'''")

    elif array_treino[i] == 29:
        array_treino_lily = np.append(array_treino_lily,  "f'''")

    elif array_treino[i] == 30:
        array_treino_lily = np.append(array_treino_lily,  "fis'''")

    elif array_treino[i] == 31:
        array_treino_lily = np.append(array_treino_lily,  "g'''")

    elif array_treino[i] == 32:
        array_treino_lily = np.append(array_treino_lily,  "gis'''")

    elif array_treino[i] == 33:
        array_treino_lily = np.append(array_treino_lily,  "a'''")

    elif array_treino[i] == 34:
        array_treino_lily = np.append(array_treino_lily,  "ais'''")

    elif array_treino[i] ==35:
        array_treino_lily = np.append(array_treino_lily,  "b'''")
    
for j in range(n_teste):
    if array_teste[j] == 0:
        array_teste_lily = np.append(array_teste_lily,  "c'")
        
    elif array_teste[j] == 1:
        array_teste_lily = np.append(array_teste_lily,  "cis'")

    elif array_teste[j] == 2:
        array_teste_lily = np.append(array_teste_lily,  "d'")

    elif array_teste[j] == 3:
        array_teste_lily = np.append(array_teste_lily,  "dis'")

    elif array_teste[j] == 4:
        array_teste_lily = np.append(array_teste_lily,  "e'")

    elif array_teste[j] == 5:
        array_teste_lily = np.append(array_teste_lily,  "f'")

    elif array_teste[j] == 6:
        array_teste_lily = np.append(array_teste_lily,  "fis'")

    elif array_teste[j] == 7:
        array_teste_lily = np.append(array_teste_lily,  "g'")

    elif array_teste[j] == 8:
        array_teste_lily = np.append(array_teste_lily,  "gis'")

    elif array_teste[j] == 9:
        array_teste_lily = np.append(array_teste_lily,  "a'")

    elif array_teste[j] == 10:
        array_teste_lily = np.append(array_teste_lily,  "ais'")

    elif array_teste[j] == 11:
        array_teste_lily = np.append(array_teste_lily,  "b'")

    elif array_teste[j] == 12:
        array_teste_lily = np.append(array_teste_lily,  "c''")
        
    elif array_teste[j] == 13:
        array_teste_lily = np.append(array_teste_lily,  "cis''")

    elif array_teste[j] == 14:
        array_teste_lily = np.append(array_teste_lily,  "d''")

    elif array_teste[j] == 15:
        array_teste_lily = np.append(array_teste_lily,  "dis''")

    elif array_teste[j] == 16:
        array_teste_lily = np.append(array_teste_lily,  "e''")

    elif array_teste[j] == 17:
        array_teste_lily = np.append(array_teste_lily,  "f''")

    elif array_teste[j] == 18:
        array_teste_lily = np.append(array_teste_lily,  "fis''")

    elif array_teste[j] == 19:
        array_teste_lily = np.append(array_teste_lily,  "g''")

    elif array_teste[j] == 20:
        array_teste_lily = np.append(array_teste_lily,  "gis''")

    elif array_teste[j] == 21:
        array_teste_lily = np.append(array_teste_lily,  "a''")

    elif array_teste[j] == 22:
        array_teste_lily = np.append(array_teste_lily,  "ais''")

    elif array_teste[j] == 23:
        array_teste_lily = np.append(array_teste_lily,  "b''")

    elif array_teste[j] == 24:
        array_teste_lily = np.append(array_teste_lily,  "c'''")
        
    elif array_teste[j] == 25:
        array_teste_lily = np.append(array_teste_lily,  "cis'''")

    elif array_teste[j] == 26:
        array_teste_lily = np.append(array_teste_lily,  "d'''")

    elif array_teste[j] == 27:
        array_teste_lily = np.append(array_teste_lily,  "dis'''")

    elif array_teste[j] == 28:
        array_teste_lily = np.append(array_teste_lily,  "e'''")

    elif array_teste[j] == 29:
        array_teste_lily = np.append(array_teste_lily,  "f'''")

    elif array_teste[j] == 30:
        array_teste_lily = np.append(array_teste_lily,  "fis'''")

    elif array_teste[j] == 31:
        array_teste_lily = np.append(array_teste_lily,  "g'''")

    elif array_teste[j] == 32:
        array_teste_lily = np.append(array_teste_lily,  "gis'''")

    elif array_teste[j] == 33:
        array_teste_lily = np.append(array_teste_lily,  "a'''")

    elif array_teste[j] == 34:
        array_teste_lily = np.append(array_teste_lily,  "ais'''")

    elif array_teste[j] == 35:
        array_teste_lily = np.append(array_teste_lily,  "b'''")
    
data_treino = {"note_num": array_treino, "note_name": array_treino_lily}
df_treino = pd.DataFrame(data_treino)

data_teste = {"note_num": array_teste, "note_name":array_teste_lily}
df_teste = pd.DataFrame(data_teste)

df_treino.to_csv(path_or_buf = "df_treino.csv", sep=";")
df_teste.to_csv(path_or_buf = "df_teste.csv", sep=";")

