# Fashion MNIST Classification with VGG16

This project demonstrates the application of a Convolutional Neural Network (CNN) leveraging the VGG16 architecture for classifying fashion articles from the `fashion_mnist` dataset. It showcases the power of transfer learning through the use of a pre-trained VGG16 model, adapted and fine-tuned for a specific task in the realm of fashion article classification.

## Project Overview

The `fashion_mnist` dataset consists of 60,000 training images and 10,000 test images, each a 28x28 grayscale image associated with a label from 10 classes. This project enhances the classification accuracy by employing a CNN with the VGG16 model as a convolutional base. 

### Key Features

- **Transfer Learning**: Utilizes the VGG16 model pre-trained on the ImageNet dataset.
- **Model Customization**: Adds custom layers on top of the VGG16 base to tailor the network for the fashion MNIST dataset.
- **Evaluation and Visualization**: Incorporates evaluation metrics and visualizations of training performance, model architecture, and feature maps.

## Setup and Installation

Ensure you have Python 3.6+ installed. Then install the required packages:

```bash
pip install tensorflow numpy matplotlib
```

## Usage

To run this project, clone the repository and execute the main script:

```bash
git clone https://https://github.com/UkrainianEagleOwl/M3_H10.git
cd your-repository-directory
python fashion_mnist_vgg16.py
```

## Structure

- `fashion_mnist_vgg16.py`: The main script that contains the code for loading data, building, training, and evaluating the model.
- `model_architecture.png`: A visual representation of the model's architecture.
- `training_plots.png`: Plots showing the training and validation accuracy and loss over epochs.

## Model Architecture

The project uses the VGG16 model as a convolutional base, with custom layers added on top for classification. The model's architecture is visualized in `model_architecture.png`.

## Results

The model achieves a high classification accuracy on the `fashion_mnist` dataset, outperforming standard MLP models. For detailed performance metrics, refer to the training logs and evaluation results section in the script.

## Visualizations

Training performance and feature map visualizations provide insights into the model's learning process and its focus on different features within the images.

## Conclusions

The use of a pre-trained VGG16 model demonstrates the effectiveness of transfer learning in improving classification accuracy on the fashion MNIST dataset. This approach can be adapted and extended to other image classification tasks with similar success.

## License

This project is open-sourced under the MIT License. See the LICENSE file for details.
