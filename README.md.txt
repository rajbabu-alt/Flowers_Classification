# Flower Classification using MobileNetV2

## Overview

This project is a deep learning application that classifies flower images into five categories using transfer learning with MobileNetV2.

The model can classify:

- Daisy
- Dandelion
- Rose
- Sunflower
- Tulip

## Features

- Transfer Learning with MobileNetV2
- TensorFlow/Keras
- Gradio Web Interface
- Hugging Face Deployment
- Real-time Flower Prediction

## Model Performance

- Validation Accuracy: 89.54%

## Technologies Used

- Python
- TensorFlow
- MobileNetV2
- NumPy
- Gradio
- Hugging Face Spaces

## Files

- `Flower_Classification.ipynb` — Model training notebook
- `flower_classifier_fixed.keras` — Trained model
- `app.py` — Gradio application
- `README.md` — Project documentation

## Challenges Faced

While deploying the model on Hugging Face, the model incorrectly predicted "dandelion" for almost every image.

### Root Cause

The images were being normalized twice:

- First in `app.py`
- Again inside the model through a Rescaling layer

### Solution

Removed the extra normalization step from `app.py`, which fixed the predictions and restored expected model performance.

## Future Improvements

- Support more flower species
- Add confidence visualization
- Improve model accuracy
- Deploy a mobile-friendly version

## Application Preview

### Home Page

![Home Page](images/homepage.png)

### Prediction Example

![Prediction](images/prediction.png)