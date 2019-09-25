import image_analyser as imal
import pandas as pd
import convnet

print("Inicio do teste:")

[X_treino, X_teste] = imal.image_analyser()
df_y = pd.read_csv("arq_teste\\teste01\\myfile.csv", sep=';',header=None, usecols=[2])
y_treino, y_teste = df_y[:74], df_y[74:]

print("entrando na convnet")
convnet.convnet(X_treino, y_treino, X_teste, y_teste, 5, 369)

print("Tamanho do X_treino: ",len(X_treino))
print("Tamanho do X_teste: ",len(X_teste))
print("Fim do teste")
