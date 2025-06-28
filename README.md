# Brain-Tumor-Detection-segmentation
This project focuses on Brain Tumor Detection using deep learning. It combines image classification to identify whether an MRI image contains a tumor and segmentation to locate and outline the tumor using a Mask R-CNN model. The project includes a custom-trained CNN classifier and a Mask R-CNN segmentation model applied to MRI scan images.
#  Brain Tumor Detection & Segmentation

This project uses deep learning to **detect and segment brain tumors** from MRI images. It includes:

- A **CNN classifier** trained to detect the presence of tumors.
- A **Mask R-CNN model** for precise **tumor segmentation**.
- A simple **GUI (Tkinter)** to test the models interactively.

---

## 📂 Project Structure

rain_tumor_project/
│
├── app1.py # GUI application to test classification
├── mainTrain.py # Trains the CNN classifier
├── mainTest.py # Tests the classifier
├── BrainTumor10EpochsCategorical.h5# Trained CNN model
│
├── Br35H-Mask-RCNN/
│ ├── annotations_all.json # Full annotation file for segmentation
│ ├── TEST/ # Test MRI images
│ ├── TRAIN/ # Training MRI images


---

##  Features

- **Classification**:
  - A custom CNN detects if a brain tumor exists in an MRI scan.
  - Trained on labeled brain MRI datasets.
  
- **Segmentation**:
  - Uses Mask R-CNN to precisely outline tumors.
  - Annotated data in COCO format for training.

- **GUI**:
  - Simple interface to select and classify MRI scans using the trained model.

---


