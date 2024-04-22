# Handwritten Digit Classification using Multilayer Perceptron

## Problem Statement:
The project aims to classify handwritten digits using a Multi-Layer Perceptron (MLP) neural network.

## Introduction:
The project involves tasks such as machine learning model training and evaluation using the MNIST dataset, a benchmark dataset widely used for handwritten digit classification tasks.

## Data Set Information:
- **Source:** Derived from the National Institute of Standards and Technology (NIST) Special Database 3 (SD-3) and Special Database 1 (SD-1).
- **Content:** 60,000 training images and 10,000 test images of handwritten digits (0-9), each with a resolution of 28x28 pixels.
- **Purpose:** Commonly used for training and testing machine learning models, especially for digit recognition tasks.
- **Accessibility:** Freely available and widely used in academic and research settings.
- **Libraries used:** `keras.datasets.mnist`, `tensorflow`, `numpy`, `matplotlib.pyplot`, `sklearn.neural_network.MLPClassifier`, `sklearn.preprocessing.StandardScaler`.

## Explanation:
1. Imports necessary libraries and loads the MNIST dataset using Keras.
2. Visualizes sample images from the dataset.
3. Scales pixel values of the images to a range between 0 and 1.
4. Creates an MLP classifier with two hidden layers of sizes 64 and 32.
5. Reshapes training data into a 2D array and trains the MLP classifier.
6. Evaluates model accuracy using the testing dataset.
7. Prints accuracy score for the testing dataset.

## Conclusion:
The project demonstrates a versatile approach to data acquisition and analysis in machine learning. It showcases the application of neural networks in pattern recognition tasks using the MNIST dataset. Robust evaluation methodology ensures accurate assessment of model performance on unseen data.

## Applications:
1. Content Aggregation and Analysis
2. Information Retrieval
3. Pattern Recognition and Classification
4. Recommendation Systems

## References:
- [MNIST dataset](https://www.kaggle.com/datasets/hojjatk/mnist-dataset)
