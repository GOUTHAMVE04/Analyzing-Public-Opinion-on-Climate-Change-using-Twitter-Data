# 🌍 Climate Change Sentiment Analysis

## 📌 Project Title  
**Analyzing Public Opinion on Climate Change using Twitter Data**

## 📝 Problem Statement  
Climate change is a global challenge that affects ecosystems, economies, and human health. Understanding public perception is essential for designing effective awareness campaigns and policy-making. This project uses Twitter data to classify tweets into categories like Pro, Anti, Neutral, and News to gain insights into public sentiment about climate change.

## ✅ How I Solved It  

### Week 1 – Data Loading & Understanding  
- Loaded and explored the dataset using Pandas.  
- Checked for missing values and summarized statistics to understand the structure of the data.

### Week 2 – Univariate Analysis & Data Transformation  
- Performed distribution analysis on sentiment labels and message lengths.  
- Cleaned text data and created visualizations like word clouds to understand the context of tweets.

### Week 3 – Bivariate Analysis, Model Training & Evaluation  
- Explored relationships between sentiment and message length using boxplots and correlation matrices.  
- Trained Random Forest and Logistic Regression models.  
- Fine-tuned the Random Forest using Grid Search to achieve better accuracy and F1 scores.

## ✅ Achieved Results  
- **Accuracy:** 0.679  
- **Precision:** 0.690  
- **Recall:** 0.679  
- **F1 Score:** 0.652  

The model classifies climate change-related tweets into sentiment categories with good performance, especially in recognizing positive sentiments.

## 📥 Pre-trained Model  
Since the trained model file is large, it is hosted on Google Drive. Please download it from the link below and place it in the `./sample_data/` directory before running the project.

➡️ [Download random_forest_model.pkl](https://drive.google.com/file/d/1hUovNSE0_SDoXGGPkXRdZaLsOhPOI4t4/view?usp=sharing)

**Instructions:**  
1. Download `random_forest_model.pkl` from the above link.  
2. Place it inside the `./sample_data/` folder of the cloned repository.

## ✅ How Others Can Use This Model  
1. Clone the repository:  
   ```bash
   git clone https://github.com/GOUTHAMVE04/Analyzing-Public-Opinion-on-Climate-Change-using-Twitter-Data.git
   cd Analyzing-Public-Opinion-on-Climate-Change-using-Twitter-Data
