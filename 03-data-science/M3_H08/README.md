# Handwritten Digit Recognition with Neural Networks

## Overview
This project demonstrates the creation, training, and testing of a fully connected neural network for recognizing handwritten digits. The neural network is built and trained using low-level TensorFlow operations on the MNIST dataset, a collection of 28x28 pixel images of handwritten digits.

## Features
- **Neural Network Creation**: Custom neural network architecture with dense layers.
- **Training on MNIST Dataset**: Utilizing the MNIST dataset for training and testing.
- **Loss and Accuracy Monitoring**: Tracking the performance of the network during training.
- **Testing on Unseen Data**: Evaluating the network's performance on test data.
- **Visual Inspection of Predictions**: Displaying test images with their predicted and actual labels.

## Neural Network Architecture
The neural network consists of:
- An input layer that flattens 28x28 pixel images into 784-element vectors.
- Two hidden dense layers with sigmoid activation functions.
- An output dense layer with softmax activation for classifying digits 0-9.

## Installation
To set up the project, follow these steps:
1. Clone the repository: `git clone [repository-url]`
2. Navigate to the project directory: `cd [project-directory]`
3. Install dependencies: `poetry install` (ensure Poetry is installed)

## Usage
Run the Jupyter Notebook `GoIT_HW_8_new.ipynb` to train and test the neural network. The notebook includes:
- Data loading and preprocessing.
- Neural network definition and training.
- Accuracy calculation and visualization of the training process.
- Testing the network on sample images from the test dataset.

## Results
The project includes visualizations of loss and accuracy over the training period, as well as sample predictions on test images. These illustrate the network's ability to learn and correctly classify handwritten digits.

## Conclusions
The final section of the notebook draws conclusions based on the network's performance metrics and visual inspection of its predictions on test data.

## License
[Specify License Here]
 
