import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def main():
    print("Let's get things started.")

    # Load the dataset from CSV file using pandas
    df = pd.read_csv("dictionary_dataset.csv")

    while True:
        # Prompt the user to enter a password
        input_password = input("Enter a password (or 'q' to quit): ")

        if input_password.lower() == "q":
            break

        # Vectorize the words in the dataset using CountVectorizer
        vectorizer = CountVectorizer()
        word_vectors = vectorizer.fit_transform(df["word"])

        # Calculate cosine similarity between user input and dataset words
        similarity_matrix = cosine_similarity(vectorizer.transform([input_password]), word_vectors)

        # Find the index of the most similar word
        most_similar_index = similarity_matrix.argmax()

        # Get the most similar word from the dataset
        most_similar_word = df.loc[most_similar_index, "word"]

        # Check if the similarity exceeds a threshold (e.g., 0.8)
        if similarity_matrix[0, most_similar_index] > 0.8:
            print("Password match found:", most_similar_word)
        else:
            print("No password match found.")

    print("The program terminated.")

if __name__ == '__main__':
    main()
