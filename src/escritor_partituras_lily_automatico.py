import numpy as np
import pandas as pd

df_treino = pd.read_csv(r"../arq_teste/teste02/df_treino.csv", sep=';', usecols=['note_name'])
df_teste = pd.read_csv(r"../arq_teste/teste02/df_teste.csv", sep=';', usecols=['note_name'])

n_treino = 10000
n_teste = 1000

file_lily_treino = np.array([])
file_lily_teste = np.array([])

for i in range(int(n_treino/100)):
    np.append(file_lily_treino, open("../arq_teste/teste02/treino_lily/lily_treino%s.ly" % i, "w"))
    file_lily_treino[i].write("\version \"2.18.2\"")
    file_lily_treino[i].write("\n{")
    for j in range(100):
        if j == 0:
            file_lily_treino[i].write(df_treino[100*i+j])

    file_lily_treino[i].write("\n}")
    file_lily_treino[i].close    

for k in range(n_teste/100):
    np.append(file_lily_teste, open("../arq_teste/teste02/teste_lily/lily_teste%s.ly" % k, "w"))
    file_lily_teste[k].write("\version \"2.18.2\"")
    file_lily_teste[k].write("\n{")
    for m in range(100):
        file_lily_teste[k].write(df_teste[100*k+m])

    file_lily_teste[k].write("\n}")
    file_lily_teste[k].close    


                                  