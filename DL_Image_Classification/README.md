# 🧠 CIFAR-10 Image Classification
# Fully Connected vs. CNN vs. Transfer Learning

## 📄 Project Overview

This project explores three different approaches to image classification using the CIFAR-10 dataset:
1. A baseline fully connected network (FC)
2. A custom-built convolutional neural network (CNN)
3. Transfer learning using the VGG16 architecture

The goal was to compare performance, learning behavior, and generalization capacity of each model on the same dataset.

---

## 🏗️ Technical Architecture

### 🟨 Dataset: CIFAR-10
- 60,000 color images (32x32), 10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck)
- Train/test split: 50,000/10,000
- Data preprocessing: normalization, one-hot encoding

---

### 🔹 Version 1: Fully Connected Network (Baseline)
- Flattened image input
- Two hidden layers: 64 and 32 neurons (ReLU)
- Softmax output layer (10 classes)
- Optimizer: Adam
- Loss: Sparse categorical crossentropy

> ⚠️ Result: High overfitting, low generalization (validation accuracy ≈ 45%)

---

### 🔹 Version 2: Custom CNN
- 3 Convolutional blocks:
  - Conv2D → BatchNorm → MaxPooling → Dropout
  - 32 → 64 → 128 filters (3x3 kernels)
- Dense layer (128 neurons) + Dropout
- Softmax output (10 classes)

> ✅ Result: Significantly improved performance  
> **Validation Accuracy: ~84%**  
> Robust feature learning and better generalization

---

### 🔹 Version 3: Transfer Learning with VGG16
- Pre-trained VGG16 with custom top layers
- Fine-tuning + Learning rate scheduling
- Comparison before and after fine-tuning

> 🚀 Result:  
> +28% improvement in validation accuracy after fine-tuning  
> Training accuracy reached ~88%  
> Validation accuracy reached ~76%  
> AUC: 0.91

---

## 🧰 Tools & Stack

- Python  
- TensorFlow / Keras  
- Matplotlib, Seaborn  
- VGG16 (pre-trained weights)  
- Scikit-learn (for confusion matrices, metrics)

---

## 🖼️ Screenshots or Mockups

### 🖼️ CIFAR-10 Dataset Samples  
![Dataset Samples](./images/Dataset%20Samples.png)  
> Visual preview of CIFAR-10 categories used for training and evaluation.

---

### 🔹 FC vs CNN Accuracy Comparison  
![Accuracy Comparison](./images/CNN%20FC%20Comparison.png)  
> CNN model significantly outperformed the fully connected model in generalization and accuracy.

---

### 📉 CNN Training vs Validation Loss  
![CNN Loss](./images/CNN%20Training_Validation%20Loss.png)

### 📉 FC Training vs Validation Loss  
![FC Loss](./images/FC%20Training_Validation%20Loss.png)  
> Clear indication of better convergence and reduced overfitting in the CNN vs. FC model.

---

### 🧠 Confusion Matrix – Fully Connected Model  
![FC Confusion Matrix](./images/FC%20Confusion%20Matrix.png)

### 🧠 Confusion Matrix – CNN Model  
![CNN Confusion Matrix](./images/CNN%20Confusion%20Matrix.png)  
> The CNN shows a tighter distribution of correct predictions compared to the FC baseline.

---

### 📈 VGG16 Accuracy & Loss  
![VGG16 Accuracy and Loss](./images/VGG16%20Accuracy%20and%20Loss.png)  
> Fine-tuned VGG16 showed stable and consistent performance, with improved accuracy over epochs.

---

### 🔍 VGG16 Model Comparison  
![VGG16 Comparison](./images/VGG16%20Comparison.png)  
> Detailed evaluation of VGG16 before and after fine-tuning, including classification metrics and confusion matrix.



---

## 🚀 Outcomes or Impact

- Learned and compared the effects of network depth, regularization, and transfer learning
- Demonstrated the performance gap between FC and CNN for image tasks
- Improved accuracy from **~45% to 84%** by adopting better architectural choices
- Showcased practical implementation of model comparison, visualization, and performance tuning
