# AI Sentiment Analyzer

## Project Description

AI Sentiment Analyzer is a beginner-friendly web application for an Introduction to Artificial Intelligence course. It reads a sentence and predicts whether the overall sentiment is **positive**, **negative**, or **neutral**.

The project demonstrates how a simple rule-based AI system can make a classification by looking for meaningful words in text. It is intentionally transparent so a student can explain every step of the analysis.

## Objective

The objective is to understand a basic natural language processing idea: text can be analyzed by finding keywords and comparing the number of positive and negative signals.

## Features

- Analyze a sentence with one click.
- Classify text as Positive, Negative, or Neutral.
- Display the positive and negative scores.
- Show which sentiment words were detected.
- Include clickable example sentences.
- Show a friendly message when the input is empty.
- Responsive layout for desktop and mobile screens.
- No server, database, API, or installation required.

## Technologies Used

- HTML5 for the page structure
- CSS3 for the responsive visual design
- Vanilla JavaScript for the sentiment logic and user interaction

## How the Sentiment Analysis Works

1. The user enters a sentence.
2. JavaScript converts the sentence to lowercase and removes punctuation.
3. The sentence is split into individual words.
4. Every word is compared with a list of positive words and a list of negative words.
5. Each matching positive word increases the positive score by 1.
6. Each matching negative word increases the negative score by 1.
7. The scores are compared:
   - If the positive score is higher, the result is **Positive**.
   - If the negative score is higher, the result is **Negative**.
   - If the scores are equal, the result is **Neutral**.

This is a keyword-based model, not a full machine learning model. It is useful for learning the basic idea of text classification, but it cannot understand context, sarcasm, or every possible word.

## How to Run the Project

1. Download or copy all four project files into the same folder.
2. Double-click `index.html`.
3. Enter a sentence or click one of the examples.
4. Select **Analyze sentiment** to see the result.

The project runs directly in a modern web browser. No Node.js, package manager, or internet connection is needed for the application logic.

## Example Inputs and Outputs

| Example input | Expected output | Why |
| --- | --- | --- |
| `I love this wonderful and helpful app!` | Positive | It contains `love`, `wonderful`, and `helpful`. |
| `The service was slow and disappointing.` | Negative | It contains `slow` and `disappointing`. |
| `The meeting is scheduled for Tuesday.` | Neutral | It contains no words from either list. |

## Future Improvements

- Add more positive and negative vocabulary.
- Give different words different weights.
- Add support for negation, such as recognizing that “not good” is negative.
- Use a trained machine learning model for more nuanced predictions.
- Add a history of recent analyses.
- Add charts to visualize sentiment scores.

## Author

**Student Project**  
Introduction to Artificial Intelligence
