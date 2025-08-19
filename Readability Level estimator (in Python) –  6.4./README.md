
# 📖 Week 6 – Readability  

### Description
A Python program that determines the U.S. **reading grade level** of a given text using the **Coleman–Liau index**. The program counts the number of letters, words, and sentences to estimate how difficult the text is to read. 


**How does it work?**
The program counts:  
- **Letters** (alphabetic characters)  
- **Words** (sequences separated by spaces)  
- **Sentences** (terminated by `.`, `!`, or `?`)  

It then applies the Coleman–Liau formula to estimate the U.S. grade level required to comprehend the text:  

\[
\text{index} = 0.0588 \times L - 0.296 \times S - 15.8
\]

Where:  
- **L** = average number of letters per 100 words  
- **S** = average number of sentences per 100 words 

### Key Concepts
- String parsing and text tokenization  
- Control flow with loops and conditionals   
- Implementation of a readability algorithm (Coleman–Liau index) 



### Example Output
```bash
$ python readability.py

Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
