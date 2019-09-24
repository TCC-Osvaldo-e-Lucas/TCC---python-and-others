
def image_analyser():

	import cv2
	import glob
	import numpy as np
	import matplotlib.pyplot as plt
	#Crio as listas que guardarão as imgs
	X_treino = []
	X_teste = []
	#Itero sobre os arquivos de img já separando-os em treino e teste
	files_treino = glob.glob ("images\\teste_wave\\[0-74].png")
	files_teste = glob.glob("images\\teste_wave\\[75-98].png")

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

auxiliar = image_analyser()
print(auxiliar[0])
print("huehuaihf")
print(auxiliar[1])
