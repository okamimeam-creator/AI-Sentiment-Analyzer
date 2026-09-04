// AI Sentiment Analyzer
// This simple model compares words in a sentence with two keyword lists.

const positiveWords = [
  "amazing", "awesome", "best", "brilliant", "calm", "celebrate", "enjoy", "enjoyed",
  "excellent", "excited", "fun", "friendly", "good", "great", "happy", "helpful",
  "hope", "impressive", "joy", "kind", "like", "love", "nice", "perfect", "positive",
  "proud", "recommend", "successful", "thankful", "wonderful", "win", "winning"
];

const negativeWords = [
  "angry", "annoyed", "awful", "bad", "boring", "confused", "crisis", "disappointing",
  "dislike", "doubt", "fail", "failed", "failure", "frustrated", "frustrating", "hate",
  "horrible", "late", "lost", "negative", "pain", "problem", "sad", "slow", "terrible",
  "tired", "trouble", "unhappy", "upset", "waste", "worst", "wrong"
];

const input = document.querySelector("#sentence-input");
const analyzeButton = document.querySelector("#analyze-button");
const characterCount = document.querySelector("#character-count");
const inputMessage = document.querySelector("#input-message");
const resultContent = document.querySelector("#result-content");
const sentimentIcon = document.querySelector("#sentiment-icon");
const sentimentLabel = document.querySelector("#sentiment-label");
const sentimentDescription = document.querySelector("#sentiment-description");
const positiveScore = document.querySelector("#positive-score");
const negativeScore = document.querySelector("#negative-score");
const matchedWordsList = document.querySelector("#matched-words-list");

function analyzeSentiment(sentence) {
  // Remove punctuation so words can be compared consistently.
  const words = sentence.toLowerCase().replace(/[^a-z\s']/g, " ").split(/\s+/).filter(Boolean);
  const positiveMatches = words.filter((word) => positiveWords.includes(word));
  const negativeMatches = words.filter((word) => negativeWords.includes(word));
  const positiveTotal = positiveMatches.length;
  const negativeTotal = negativeMatches.length;

  let sentiment = "neutral";
  if (positiveTotal > negativeTotal) sentiment = "positive";
  if (negativeTotal > positiveTotal) sentiment = "negative";

  return { sentiment, positiveTotal, negativeTotal, positiveMatches, negativeMatches };
}

function displayResult(result) {
  const labels = {
    positive: { icon: "😊", title: "Positive sentiment", description: "Your sentence has a cheerful and optimistic tone." },
    negative: { icon: "😞", title: "Negative sentiment", description: "Your sentence contains more words with a critical or unhappy tone." },
    neutral: { icon: "😐", title: "Neutral sentiment", description: "The positive and negative signals are balanced or missing." }
  };
  const message = labels[result.sentiment];
  const allMatches = [...result.positiveMatches, ...result.negativeMatches];

  resultContent.className = `result-content ${result.sentiment}`;
  sentimentIcon.textContent = message.icon;
  sentimentLabel.textContent = message.title;
  sentimentDescription.textContent = message.description;
  positiveScore.textContent = result.positiveTotal;
  negativeScore.textContent = result.negativeTotal;
  matchedWordsList.textContent = allMatches.length ? allMatches.join(", ") : "No sentiment keywords found.";
}

function runAnalysis() {
  const sentence = input.value.trim();
  inputMessage.textContent = "";

  if (!sentence) {
    inputMessage.textContent = "Please enter a sentence first.";
    input.focus();
    return;
  }

  displayResult(analyzeSentiment(sentence));
}

input.addEventListener("input", () => {
  characterCount.textContent = `${input.value.length} / 280`;
  if (inputMessage.textContent) inputMessage.textContent = "";
});

analyzeButton.addEventListener("click", runAnalysis);

input.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") runAnalysis();
});

document.querySelectorAll(".example-chip").forEach((button) => {
  button.addEventListener("click", () => {
    input.value = button.dataset.example;
    input.dispatchEvent(new Event("input"));
    runAnalysis();
  });
});
