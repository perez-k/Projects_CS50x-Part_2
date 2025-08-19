
# 🧬 DNA Profiling with Short Tandem Repeat (STR) Matching System

A Python program that identifies a person based on their DNA by comparing Short Tandem Repeat (STR) counts against a database of known individuals.


### **How It Works**
1. **Input:**  
   - A CSV file containing individuals’ names and STR counts on their DNA 
   - A text file containing the DNA sequence to analyze (find a match) 
2. **Process:**  
   - Computes the longest consecutive run of each STR in the DNA sequence  
   - Compare the counts to each profile in the database to find a matching individual
3. **Output:**  
   - The matching individual's name, or `"No match"` if none found


### **Key Concepts**
- Reading and parsing CSV files or text files using Python’s module (csv, ...)
- String pattern recognition and matching
- Algorithmic computation of the longest consecutive substring repeats
- Use of lists and dictionaries to store computed values and compare results


### **Example Output**
```bash
$ python dna.py databases/large.csv sequences/5.txt
Cedric
```

```bash
$ python dna.py databases/large.csv sequences/10.txt
No match
```

