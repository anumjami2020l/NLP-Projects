# Unveiling the Power of Deep Learning: Comparative Study of LSTM, BERT, and GRU for Disaster Tweet Classification

##  Overview
This repository contains the research implementation for the paper:  
**"Unveiling the Power of Deep Learning: A Comparative Study of LSTM, BERT, and GRU for Disaster Tweet Classification"** (Published December 2023).

The project explores the effectiveness of three state-of-the-art deep learning architectures—**LSTM**, **GRU**, and **BERT**—for multiclass disaster tweet classification using real-time data collected via the Twitter API.

---

##  Research Objective
The goal is to **automatically classify tweets into disaster categories** such as:
- Earthquakes
- Floods
- Wildfires
- Other major disaster events

This enables rapid situational awareness, aiding emergency response teams and humanitarian organizations.

---

## Key Results
- **BERT** achieved the highest performance with **95% accuracy** across multiple disaster categories.
- **LSTM** and **GRU** provided competitive results but fell short in capturing contextual nuances compared to transformer-based models.

---

## Dataset
- **Source:** Real-time tweets collected via Twitter API (January–December 2023).
- **Preprocessing:**
  - Language filtering (English-only tweets)
  - Removal of URLs, mentions, hashtags, and special characters
  - Tokenization and padding for LSTM/GRU
  - BERT tokenizer for transformer-based model

---

## Tech Stack
- **Languages:** Python  
- **Frameworks/Libraries:**  
  - PyTorch / TensorFlow  
  - Hugging Face Transformers  
  - scikit-learn  
  - Pandas, NumPy  
  - Matplotlib, Seaborn  
- **APIs:** Twitter API v2  

---

## Model Training
### LSTM & GRU
- Embedding layer (GloVe pre-trained vectors)  
- Bidirectional recurrent layers  
- Dense classification head  

### BERT
- Pre-trained `bert-base-uncased` model from Hugging Face  
- Fine-tuned for disaster classification task  

---

## Evaluation Metrics
- Accuracy  
- Precision, Recall, F1-score  
- Confusion Matrix for each model  
- Comparative performance visualization  
