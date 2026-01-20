# Generating Melodies with RNN-LSTM

A Deep Learning project focused on the intersection of Artificial Intelligence and Music Theory. This repository contains a Recurrent Neural Network (RNN) using Long Short-Term Memory (LSTM) units to learn musical structures from a dataset of folk songs and generate original MIDI melodies.

## Project Overview

This project explores how sequence-based neural networks can capture the essence of melody, rhythm, and harmony. By processing MIDI data into a symbolic representation, the model learns the probability distribution of the next note in a sequence, allowing it to compose new musical phrases.

## Key Features:

- Symbolic Music Processing: Converts MIDI data into a specialized text-based format for neural network consumption.
- LSTM Architecture: Utilizes the memory capabilities of LSTM to maintain long-term dependencies in musical phrases.
- Temperature-based Sampling: Allows control over the randomness of the generated output (from conservative to highly creative).
- End-to-End Pipeline: Includes scripts for data pre-processing, training, and melody generation.

## Tech Stack

- Language: Python
- Deep Learning Framework: TensorFlow / Keras
- Music Analysis: Music21
- Training Hardware: NVIDIA Tesla T4 GPU (via Google Colab)

## Model Architecture & Training

1.  LSTM Layer: 256 units to capture temporal musical patterns.
2.  Dropout Layer: 0.2 to prevent overfitting.
3.  Dense Layer: Softmax activation to predict the next note index.

## Training Details:

- Sequence Length: 32-64 notes.
- Batch Size: 32-64.
- Loss Function: Sparse Categorical Crossentropy.
- Optimizer: Adam.
- Final Loss achieved: ~0.7 (indicating high structural coherence).

## File Structure

- `preprocess.py`: Handles data encoding, mapping creation, and sequence generation.
- `train.py`: Defines the model architecture and executes the training loop.
- `melodygenerator.py`: Loads the trained `.h5` model and `mapping.json` to synthesize new MIDI files.
- `mapping.json`: The "vocabulary" of the model (notes and durations).

## How to Run

1. Pre-process data: Run `preprocess.py` to prepare your dataset and generate the mapping.
2. Train the model: Execute `train.py`. Ensure GPU acceleration is enabled for optimal performance.
3. Generate Music: Use `melodygenerator.py` to produce original melodies.

## About the Author

Iryna Malii
Computer Science student and Music Production specialist. This project serves as a research milestone in my journey to combine AI R&D with professional audio engineering.
