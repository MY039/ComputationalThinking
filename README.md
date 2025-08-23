# 🔍 Sentence Similarity Checker in Python

This project compares 5 sentences amongst themselves and calculates similarity scores based on **common words**.  
It also keeps track of how many times each common word occurs between sentence pairs.

---

## 🚀 Features
- Cleans punctuation (commas and periods).  
- Splits text into sentences and words.
- Compares every pair of sentences from the input.  
- Counts **common words** (with frequency).  
- Sorts results by highest similarity score.  

---

## 📂 Example Output
- Sentence 0 && Sentence 1 -> 2, Common words: [('python', 1), ('is', 1)]
- Sentence 2 && Sentence 4 -> 3, Common words: [('and', 2), ('python', 1)]

---

## ⚡ Usage

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/sentence-similarity.git
   cd sentence-similarity
   ```
   
2. Add your text files (e.g., file1.txt, file2.txt).

3. Run the script:
  ```bash
  python similarity.py
  ```


## 🛠️ Tech
- Python 3
- No external dependencies (only built-in libraries)

   
