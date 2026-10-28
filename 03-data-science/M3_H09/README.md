# Fashion MNIST Classification with Neural Networks

## Introduction
This repository contains a neural network designed to classify images from the [Fashion MNIST dataset](https://github.com/zalandoresearch/fashion-mnist). The Fashion MNIST dataset includes 60,000 training images and 10,000 test images, each a 28x28 grayscale image associated with a label from 10 classes.

## Model Architecture (Version 2)
The `fashion_mnist_model_v2` is built using TensorFlow and Keras and contains the following layers:
- **Input Layer**: Flattens the 28x28 image into a 1D array.
- **First Dense Layer**: 512 neurons with ReLU activation and batch normalization.
- **Dropout**: 0.2 dropout rate for regularization.
- **Second Dense Layer**: 128 neurons with ReLU activation and batch normalization.
- **Dropout**: Another 0.2 dropout rate for regularization.
- **Output Layer**: 10 neurons (one for each class) with softmax activation to output probabilities.

The model uses the Adam optimizer and sparse categorical crossentropy as the loss function.

## Training
The model is trained for 20 epochs with a batch size of 32 and a validation split of 0.2 to monitor performance and prevent overfitting.

## Results
The `fashion_mnist_model_v2` achieved a test accuracy of approximately 87.64%, which is a competitive score for this dataset.

## Usage
To replicate the training process or to use the model for inference, you can follow these steps:

1. Clone the repository:
```
git clone https://github.com/your-github-username/fashion-mnist-classification.git
```

2. Navigate to the repository's directory:
```
cd fashion-mnist-classification
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Run the Jupyter notebook:
```
jupyter notebook fashion_mnist_classification.ipynb
```

## Visualization
The training process can be visualized in the notebook, with plots for accuracy and loss over the training epochs for both training and validation sets.

## Future Work
- Explore more complex network architectures.
- Implement data augmentation to improve model generalization.
- Tune hyperparameters such as learning rate and batch size for better performance.
- Experiment with different optimizers and loss functions.

## Contributors
- [Dmytro Filin](https://github.com/UkrainianEagleOwl)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
