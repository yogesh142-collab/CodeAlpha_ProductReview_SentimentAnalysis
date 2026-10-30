
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load dataset
df = pd.read_csv("product_reviews.csv")

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Analyze each review
def analyze_sentiment(review):
    score = analyzer.polarity_scores(str(review))["compound"]

    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Predicted_Sentiment"] = df["Review"].apply(analyze_sentiment)

# Display results
print("\nPRODUCT REVIEW SENTIMENT ANALYSIS")
print("---------------------------------")
print(df[["Review", "Predicted_Sentiment"]])

# Count sentiments
sentiment_counts = df["Predicted_Sentiment"].value_counts()

print("\nSentiment Summary:")
print(sentiment_counts)

# Save results
df.to_csv("sentiment_analysis_results.csv", index=False)

# Create visualization
sentiment_counts = sentiment_counts.reindex(
    ["Positive", "Negative", "Neutral"], fill_value=0
)

plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar")

plt.title("Product Review Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("sentiment_distribution.png")
plt.show()

print("\nAnalysis completed successfully!")
print("Results saved in sentiment_analysis_results.csv")
print("Chart saved as sentiment_distribution.png")
