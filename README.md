# Honor of Kings - Google Play Reviews Sentiment Analysis Dashboard

## 📌 Project Overview

This project performs sentiment analysis on Google Play reviews for the popular mobile game, **Honor of Kings**. The goal is to analyze user feedback to determine the overall sentiment (positive, negative, or neutral) and to identify key themes and topics in the reviews.

The project uses a combination of the **VADER sentiment analysis tool** and **machine learning models** to classify the sentiment of the reviews. The entire workflow, from data scraping to model evaluation and visualization, is documented in the `ModelDevelopment.ipynb` Jupyter Notebook.

---

## ✨ Key Features

* **Data Scraping**
  Scrapes a large number of reviews for *Honor of Kings* directly from the Google Play Store using the `google-play-scraper` library.

* **Data Cleaning and Preprocessing**
  Cleans and preprocesses the raw text data by removing punctuation, converting to lowercase, and removing stop words to prepare it for analysis.

* **Sentiment Analysis with VADER**
  Uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) tool to perform a baseline sentiment analysis.

* **Machine Learning Models**
  Trains and evaluates several machine learning models:

  * Multinomial Naive Bayes
  * Logistic Regression
  * Random Forest

* **Hyperparameter Tuning**
  Uses `GridSearchCV` to find the optimal hyperparameters for the machine learning models.

* **Data Visualization**
  Creates visualizations including:

  * Count plots
  * Box plots
  * Word clouds

---

## 🧰 Tech Stack & Libraries Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* VaderSentiment
* Matplotlib
* Seaborn
* WordCloud
* google-play-scraper

You can install all the required libraries by running:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

* `ModelDevelopment.ipynb` — Jupyter Notebook with the full analysis
* `HOK-En-VADER-Analysis.csv` — The output CSV file with sentiment scores
* `app.py` — *(Future)* For deploying the model as a web app
* `data.py` — *(Future)* For data loading and processing functions
* `filters.py` — *(Future)* For filtering and data selection
* `visualizations.py` — *(Future)* For generating visualizations
* `requirements.txt` — List of required Python libraries
* `README.md` — This file

---

## ▶️ How to Run the Project

1. Clone the repository (or download the files).

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Jupyter Notebook:

   ```bash
   jupyter notebook ModelDevelopment.ipynb
   ```

This will open the notebook in your browser, where you can run the cells to see the entire analysis.

---

## 📊 Results and Findings

The analysis of the *Honor of Kings* reviews revealed a **mixed sentiment**, with a significant number of both positive and negative reviews.

* ✅ **Positive Reviews**: Highlight appreciation for gameplay, graphics, and team strategy.
* ❌ **Negative Reviews**: Common themes include bugs, matchmaking issues, and pay-to-win elements.

The **word clouds** generated from positive and negative reviews show the most mentioned topics and keywords by sentiment.

For a detailed breakdown of:

* Model performance
* Confusion matrices
* Classification reports
  👉 Please refer to the `ModelDevelopment.ipynb` notebook.

---

## 🚀 Future Improvements

* **Deployment**
  Deploy the trained model as a web application using Streamlit or Flask to allow for real-time sentiment analysis of new reviews.

* **In-Depth Analysis**
  Conduct deeper analysis to extract more granular insights (e.g., most common praises and complaints).

* **Expand Dataset**
  Scrape and analyze reviews from other platforms such as:

  * Apple App Store
  * Reddit
  * Twitter/X

* **More Advanced Models**
  Experiment with state-of-the-art NLP models like BERT or DistilBERT to improve classification performance.

---

## 📬 Contact

Feel free to reach out if you have suggestions, feedback, or want to collaborate!

---
