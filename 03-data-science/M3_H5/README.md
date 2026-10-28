# Activity Recognition from Accelerometer Data

## Introduction
This project aims to classify types of human activity (idle, walking, running, stairs) based on accelerometer data using machine learning models. We explore the use of SVM and Random Forest classifiers to predict activities from mobile phone accelerometer readings.

## Objective
The goal is to accurately classify the activity a person is engaged in based on accelerometer data, potentially for applications in health monitoring or fitness tracking.

## Methodology
- **Data Preprocessing**: Data was normalized using MinMaxScaler.
- **Feature Engineering**: Time-domain features such as mean, standard deviation, skewness, and kurtosis were extracted from windowed segments of accelerometer data.
- **Model Training**: SVM and Random Forest classifiers from scikit-learn were trained and compared.

## Results
The Random Forest classifier outperformed the SVM model, achieving near-perfect classification metrics, indicating a strong fit to the data.

## Installation
Instructions for setting up the environment and installing dependencies.

## Usage
How to run the scripts and reproduce the results.

## Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the terms of the [MIT license](LICENSE.md).

## Contact
For any queries, you can reach out to Dmytro at dmitriy.fillin@gmail.com.

