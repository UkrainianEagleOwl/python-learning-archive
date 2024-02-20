# IMDB Sentiment Analysis using RNN Variants

## Overview
This project explores various recurrent neural network (RNN) architectures for the task of sentiment analysis on the IMDB movie review dataset. We experiment with different types of RNNs, including a simple RNN, LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit), and deep RNNs to compare their performance in classifying reviews as positive or negative.

## Models
- **Simple RNN**: The basic RNN model.
- **LSTM**: A model using Long Short-Term Memory units.
- **GRU**: A model using Gated Recurrent Units.
- **Deep RNN**: A deep network with multiple RNN layers.

## Results
Our experiments reveal that while the simple RNN had the most fluctuation in validation loss, the LSTM and GRU models performed comparably in accuracy. The deep RNN did not significantly outperform its simpler counterparts, suggesting that complexity may not always be necessary for this particular task.

## Dependencies
To run the code, you will need the following:
- Python 3.x
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib

## Installation
Clone the repository to your local machine:
```
git clone https://github.com/UkrainianEagleOwl/imdb-sentiment-analysis-rnn.git
```

Navigate to the cloned directory:
```
cd imdb-sentiment-analysis-rnn
```

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License
This project is open-sourced under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please open an issue in the repository or contact me directly at dmitriy.fillin@gmail.com
