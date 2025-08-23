sentence1 = "Python Python is a high-level, interpreted programming language."
sentence2 = "It is widely used in web development, data science, machine learning, and automation."
sentence3 = "Python’s syntax is simple and easy to read, making it beginner-friendly."
sentence4 = "It has a huge collection of libraries like NumPy, Pandas, and TensorFlow."
sentence5 = "Python is open-source and supported by a large global community."

all_sentences=[
    sentence1,
    sentence2,
    sentence3,
    sentence4,
    sentence5
]
print("Before Split:", all_sentences)  
for i in range(len(all_sentences)):
  all_sentences[i]=all_sentences[i].split()

print("After Split:", all_sentences) 

results = []

for i in range(len(all_sentences)):
    for j in range(i + 1, len(all_sentences)):
        sentence_i = all_sentences[i]
        sentence_j = all_sentences[j]

        similarity_score = 0
        common_words = {}  # dictionary: word -> count

        for word_i in sentence_i:
            for word_j in sentence_j:
                if word_i.lower() == word_j.lower():
                    similarity_score += 1
                    if word_i.lower() in common_words:
                        # increase count if word already exists
                        common_words[word_i.lower()] += 1
                    else:
                        # first occurrence
                        common_words[word_i.lower()] = 1

        # Convert dictionary to list of tuples (word, count) if you prefer
        common_words_list = [(w, c) for w, c in common_words.items()]

        results.append((similarity_score, i, j, sentence_i, sentence_j, common_words_list))

# Sort results by score (highest first)
results.sort(key=lambda x: x[0], reverse=True)

print("Similarity Scores:")
for score, i, j, sent_i, sent_j, commons in results:
    print(f"Sentence {i} && Sentence {j} -> {score}, Common words: {commons}")