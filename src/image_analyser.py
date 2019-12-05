
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
		image2= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		X_treino.append(image2)

	for myFile_teste in files_teste:
		image = plt.imread(myFile_teste)
		image2= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		X_teste.append(image2)

	X_treino = np.array(X_treino)
	X_teste = np.array(X_teste)

	# a = X_treino.shape[0]
	# b = X_teste.shape[0]

	# X_treino.reshape(75, 369, 5, 1)
	# X_teste.reshape(24, 369, 5, 1)

	print('X_treino shape:', X_treino.shape)
	print('X_teste shape:', X_teste.shape)

	return [X_treino,X_teste]

# auxiliar = image_analyser()

# print(len(auxiliar[0]))
