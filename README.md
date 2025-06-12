
# 🧠 COVID-19 Chest X-Ray Classification with CNN

This project classifies chest X-ray images as **COVID-19**, **Normal**, or **Viral Pneumonia** using a Convolutional Neural Network (CNN) built in TensorFlow/Keras.

## 📁 Dataset

- Source: [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)
- Classes: `COVID`, `NORMAL`, `Viral Pneumonia`

## ⚙️ Project Pipeline

1. Mount Google Drive and download Kaggle dataset
2. Organize and split images into train and validation sets
3. Build CNN model using:
   - Convolution + MaxPooling
   - Flatten + Dense(128)
   - Dropout(0.5)
   - Output (Softmax for 3 classes)
4. Compile with Adam optimizer
5. Train model for 10 epochs
6. Evaluate using accuracy, classification report & confusion matrix
7. Save the model
8. Build a **Gradio web interface** to make predictions

## 🚀 Gradio Interface

Launch the interface with:

```python
import gradio as gr
iface.launch()

