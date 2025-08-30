sentence1 = "Python Python is a high-level, interpreted programming language."
sentence2 = "It is widely used in web development, data science, machine learning, and automation."
sentence3 = "Python’s syntax is simple and easy to read, making it beginner-friendly."
sentence4 = "It has a huge collection of libraries like NumPy, Pandas, and TensorFlow."
sentence5 = "Python python is open-source and supported by a large global community."

all_sentences = [sentence1, sentence2, sentence3, sentence4, sentence5]

# Split sentences into words
for i in range(len(all_sentences)):
    all_sentences[i] = all_sentences[i].split()

results = []

# function to build frequency dict manually
def build_freq(words):
    freq = {}
    for w in words:
        lw = w.lower()
        freq[lw] = freq.get(lw, 0) + 1
    return freq

for i in range(len(all_sentences)):
    for j in range(i + 1, len(all_sentences)):
        sentence_i = all_sentences[i]
        sentence_j = all_sentences[j]

        freq_i = build_freq(sentence_i)
        freq_j = build_freq(sentence_j)

        similarity_score = 0
        common_words = {}

        for word in freq_i:
            if word in freq_j:
                common_count = min(freq_i[word], freq_j[word])  # ✅ only min counts
                similarity_score += common_count
                common_words[word] = common_count

        common_words_list = list(common_words.items())
        results.append((similarity_score, i, j, sentence_i, sentence_j, common_words_list))

# Sort results by score
results.sort(key=lambda x: x[0], reverse=True)

print("Similarity Scores:")
for score, i, j, sent_i, sent_j, commons in results:
    print(f"Sentence {i} && Sentence {j} -> {score}, Common words: {commons}")
