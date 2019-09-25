
def image_analyser():

	import cv2
	import glob
	import numpy as np
	import matplotlib.pyplot as plt
	#Crio as listas que guardarão as imgs
	X_treino = []
	X_teste = []
	
	#Itero sobre os arquivos de img já separando-os em treino e teste
	files_treino = []
	files_teste = []
	aux = 0
	while aux<=74:
		files_treino.append("images\\teste_wave\\%s.png"%aux)
		aux+=1
	aux2=75
	while aux2<=98:
		files_teste.append("images\\teste_wave\\%s.png"%aux2)
		aux2+=1

	#Junto todos as imgs em um np.array, para posterior leitura na convnet
	for myFile_treino in files_treino:
	    image = plt.imread(myFile_treino)
	    X_treino.append(image)

	for myFile_teste in files_teste:
	    image = plt.imread(myFile_teste)
	    X_teste.append(image)

	print('X_treino shape:', np.array(X_treino).shape)
	print('X_teste shape:', np.array(X_teste).shape)

	return [X_treino, X_teste]

# auxiliar = image_analyser()

# print(auxiliar[1])
