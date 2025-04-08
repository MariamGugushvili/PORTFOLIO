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

### 🔹 Accuracy Comparison
![Accuracy Plot](./images/fc_vs_cnn_accuracy.png)

### 📊 Training vs Validation – CNN
![Accuracy & Loss](./images/cnn_accuracy_loss_plot.png)

### 🧩 Confusion Matrices
- Fully Connected Model  
  ![FC Confusion Matrix](./images/fc_confusion_matrix.png)

- CNN Model  
  ![CNN Confusion Matrix](./images/cnn_confusion_matrix.png)

- Fine-Tuned VGG16  
  ![VGG16 Confusion Matrix](./images/vgg16_confusion_matrix.png)

### 📈 Evaluation Metrics (F1, AUC, Accuracy)
![VGG16 Metrics Table](./images/vgg16_metrics_table.png)
![VGG16 AUC](./images/vgg16_auc_curve.png)

### 🧠 Feature Maps – Before vs After Fine-Tuning
![VGG Filters Before](./images/vgg16_filters_before.png)
![VGG Filters After](./images/vgg16_filters_after.png)
---

## 🚀 Outcomes or Impact

- Learned and compared the effects of network depth, regularization, and transfer learning
- Demonstrated the performance gap between FC and CNN for image tasks
- Improved accuracy from **~45% to 84%** by adopting better architectural choices
- Showcased practical implementation of model comparison, visualization, and performance tuning
