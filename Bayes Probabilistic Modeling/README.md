
# Project: Book Genre Classification Using Naive Bayes and Python

This project involves building a Naive Bayes classifier in Python to categorize books based on their descriptions. The project focuses on implementing Bayesian probability and text preprocessing techniques to improve classification accuracy.

## Project Structure

- **Python Script:**
  - `CA0.py`: The main script that implements the Naive Bayes classification algorithm. It preprocesses text data, trains the classifier, and evaluates its performance.

- **Data Files:**
  - `books_train.csv`: Training dataset containing book descriptions and their respective genres.
  - `books_test.csv`: Test dataset containing book descriptions for classification.

- **Documentation:**
  - `EPS_CA0_F23_V1.pdf`: A report detailing the methodology, implementation, and results of the classification project.

## Installation

To run this project, ensure you have Python installed on your machine along with the required libraries. You can install the necessary dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare the Data:**
   - Ensure that `books_train.csv` and `books_test.csv` are in the same directory as `CA0.py`.

2. **Run the Script:**
   - Execute the Python script to train the Naive Bayes model and classify the test data:
   ```bash
   python CA0.py
   ```

3. **View Results:**
   - The script outputs the classification results and evaluates the model's performance using metrics such as accuracy.

## Key Concepts

- **Naive Bayes Theorem:** Utilized for probabilistic classification based on Bayes' theorem with strong (naive) independence assumptions.
- **Text Preprocessing:** Includes tokenization, normalization, and removal of stopwords and punctuation to prepare text for classification.
- **Bag of Words Model:** Represents text data as a collection of words, disregarding grammar and word order but keeping multiplicity.

## Further Exploration

- **Additive Smoothing:** Implement smoothing techniques to handle zero probabilities for unseen words in the test set.
- **Stemming and Lemmatization:** Enhance text preprocessing by reducing words to their base or root form to improve classification accuracy.
