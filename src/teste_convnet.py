import image_analyser as imal
import convnet

print("Inicio do teste:")

[X_treino, X_teste] = imal.image_analyser()

print("Tamanho do X_treino: ",len(X_treino))
print("Tamanho do X_teste: ",len(X_teste))
print("Fim do teste")
