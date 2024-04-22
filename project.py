# -*- coding: utf-8 -*-
"""finalMiniProject.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SHZYGwT_2irfs25rEPtYKk1sI1wYF8VT

#MNIST digit classification
"""

from keras.datasets import mnist
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

(trainImg, trainLab), (testImg, testLab) =  mnist.load_data()
print(type(trainImg))

for i in range (1,10):
  plt.subplot(4,5,i+2)
  plt.imshow(trainImg[i], cmap='gray_r')
  plt.subplots_adjust(hspace=0.5)
  #plt.axis('off')

"""Understanding the shape of the images"""

print("Number of images in the training set = ", trainImg.shape[0])
print("Pixels in each image = ", trainImg.shape[1],"x",trainImg.shape[2])
print("Number of images in the testing set = ", testImg.shape[0])
print("Pixels in each image = ", trainImg.shape[1],"x",testImg.shape[2])
print(trainLab.shape)

"""Printing the pixel values of one image"""

for row in trainImg[0]:
  print(row)
  print("")

"""Scaling the values"""

trainImg = trainImg/255                 #MinMax scaler = (val-min)/(max-min)
testImg = testImg/255

print(trainImg[0])
print(len(trainImg))

"""Using the MultiLayer Perceptron to train the model"""

mlp = MLPClassifier(hidden_layer_sizes=(64,32), max_iter=1000)

"""Creating a spearate 2D array for training MLP"""

lst =[]

for i in range(len(trainImg)):
  img = trainImg[i].reshape(-1)
  lst.append(img)


arr = np.array(lst)
print("Training labels: ",trainLab)


dataset = arr.reshape((60000,784))

mlp.fit(dataset, trainLab)

from sklearn.metrics import accuracy_score
ypred = mlp.predict(dataset)
print(accuracy_score(trainLab, ypred))

ddel = np.delete(dataset, 0, 0)

mlp.predict(ddel)

lst =[]


for i in range(0, len(testImg)):
  img = testImg[i].reshape(-1)
  lst.append(img)
tarr = np.array(lst)
print("Testing labels: ",testLab)

tdataset = tarr.reshape((10000,784))

tpred = mlp.predict(tdataset)

print("Accuracy of model: ",accuracy_score(testLab, tpred))

lst =[]
newtrain = np.array(60000*np.zeros(1))
i=0
for i in range(len(testImg)):
  img = testImg[i].reshape(-1)
  lst.append(img)
tarr = np.array(lst)
# print(testLab)

tdataset = tarr.reshape((10000,784))

tpred = mlp.predict(tdataset)

# print("Accuracy of model: ",accuracy_score(testLab, tpred))


from sklearn.metrics import confusion_matrix
import seaborn as sns

# Confusion Matrix
cm = confusion_matrix(trainLab, mlp.predict(dataset))
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
print()

# Accuracy Over Time (if applicable)
plt.plot(mlp.loss_curve_)
plt.title('Training Loss over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()
print()

# Sample Predictions
import random
sample_indices = random.sample(range(len(trainImg)), 5)
for index in sample_indices:
    plt.imshow(trainImg[index], cmap='gray_r')
    plt.title(f'True Label: {trainLab[index]}, Predicted Label: {mlp.predict(dataset[index].reshape(1, -1))[0]}')
    plt.axis('off')
    plt.show()