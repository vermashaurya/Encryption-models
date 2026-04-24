import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Load the dataset
data = pd.read_csv("spam_dataset.csv")

# Split the data into features (X) and labels (y)
X = data["email_text"]
y = data["label"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a CountVectorizer to convert text into tokens/features
vectorizer = CountVectorizer()
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

# Train a Random Forest classifier
classifier = RandomForestClassifier()
classifier.fit(X_train_transformed, y_train)

# Evaluate the classifier on the test set
accuracy = classifier.score(X_test_transformed, y_test)
print("Accuracy:", accuracy)

# Predict the labels for the entire dataset
data["predicted_label"] = classifier.predict(vectorizer.transform(data["email_text"]))

# Return the dataframe with predicted labels
output_data = data[["email_text", "predicted_label"]]
print(output_data)
# Count the number of spam and non-spam emails
spam_count = output_data[output_data["predicted_label"] == "spam"].shape[0]
non_spam_count = output_data[output_data["predicted_label"] != "spam"].shape[0]

# Print the counts
print("\nNumber of spam emails:", spam_count)
print("Number of non-spam emails:", non_spam_count)
