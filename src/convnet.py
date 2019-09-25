# -*- coding: utf-8 -*-
"""ConvNet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1taa9FZYR26zT3EZj2nM4AD1j8QSTPqRW"""

def convnet(X_train, y_train, X_test, y_test, width, height):
	"""**Import das bibliotecas utilizadas**
	"""
	# Commented out IPython magic to ensure Python compatibility.
	import numpy as np
	import matplotlib.pyplot as plt
	import seaborn as sns
	import tensorflow as tf
	import keras
	from keras.models import Sequential
	from keras.layers import Dense
	from keras.layers import Conv2D
	from keras.layers import MaxPooling2D
	from keras.layers import Flatten
	from keras.optimizers import SGD
	from keras.utils import to_categorical
	# %matplotlib inline

	"""**Adaptando os dados do dataset**"""

	"""Neste bloco o código transforma as imagens de treino e teste de modo que haja apenas um canal de cor em cada bit, já que as imagens são em escala de cinza.

	Aqui também foram normalizados os valores dos pixels de cada imagem, para que fiquem entre 0 e 1."""

	#Reshape do dataset de modo que tenha apenas um canal de cor
	X_train = X_train.reshape(X_train.shape[0], width, height, 1)
	X_test = X_test.reshape(X_test.shape[0], width, height, 1)
	input_shape = (width, height, 1)

	#Transformando os ints em vetores de tamanho 12
	y_train = to_categorical(y_train)
	X_train = to_categorical(X_train)


	"""**Criação do modelo de NN e compilação**"""

	"""Foi definido o tipo de modelo e as camadas, sendo 5:
	- Uma de convolução, a qual aplica filtros na imagem (neste caso foram 32), para que algumas características da imagem se tornem mais claras.

	- Uma de MaxPooling, que diminui o tamanho da imagem mantendo suas características principais, essa camada faz isso escolhendo o maior valor em uma janela (neste caso 2x2) e transfererindo para o próximo layer.

	- Uma camada Flatten que cria um vetor único, a partir de vetores de outras camadas.

	- Duas camadas Dense, camada em que todos os neurônios de cada camada são ligados na próxima.

	Na hora de compilar o modelo está sendo usada uma learning rate de 0.01.
	"""

	#Define o modelo e suas camadas
	model = Sequential()
	model.add(Conv2D(32, (3, 3), activation='relu',kernel_initializer='he_uniform', input_shape = input_shape))
	model.add(MaxPooling2D((2,2)))
	model.add(Flatten())
	model.add(Dense(120, activation='relu', kernel_initializer='he_uniform'))
	model.add(Dense(12, activation='softmax'))

	#compilando o modelo
	opt = SGD(lr=0.01, momentum=0.9)
	model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])

	#Fit do modelo
	history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test), verbose=0)

	#Validação do modelo
	acc = model.evaluate(X_test, y_test, verbose = 0)

	#gráfico de loss e acurácia
	plt.subplot(2,1,1)
	plt.plot(history.history['acc'])
	plt.plot(history.history['val_acc'])
	plt.title("Acurácia do modelo")
	plt.xlabel('Epoch')
	plt.ylabel('Accuracy')
	plt.legend(['train','test'], loc='lower right')
	plt.show()
	plt.savefig("images\\acuracia_convnet.png")

	plt.subplot(2,1,2)
	plt.plot(history.history['loss'])
	plt.plot(history.history['val_loss'])
	plt.title("Loss do Modelo")
	plt.xlabel('Epoch')
	plt.ylabel('Loss')
	plt.legend(['train','test'], loc='upper right')

	plt.show()

	plt.savefig("images\\loss_convnet.png")
	# print('Evaluated Loss', score[0])
	# print('Evaluated Accuracy', score[1])
