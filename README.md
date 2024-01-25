# Potato-Leaf-Disease-Classification-App-Gradio-Huggingface
### Introduction
This is an image classification deep learning project. In this project tried to classify 2 different diseases of potato leaves along with the the healthy ones. The result of the classification is shown in percentage.

### Model architecture
We have taken only a portion of the PlantVillage dataset. There are total 2152 images in the dataset. The dataset consists of three classes Potato___Early_blight, Potato___Late_blight, Potato_healthy. We have splitted the dataset into 80:10:10. 
We have used convolutional neural network (CNN) here. CNN is popular for image classification tasks.We use a CNN coupled with a Softmax activation in the output layer. We also add the initial layers for resizing, normalization and Data Augmentation. We choosed the sequential model here. The model consists of 6 convolutional layer each followed by MaxPooling layer and 2 dense layers at the end. The model has 183,747 trainable params

### How to guide

clone the repository from: 
download the required packages according to requirements.txt
run app.py

Also view the deployed app from the huggingface spaces: 


### License
Copyright (c) 2024 Jannatul Mawa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


### Contributor
Jannatul Mawa

email: mawa.stu2017@juniv.edu
