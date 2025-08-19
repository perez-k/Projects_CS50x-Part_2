# Hogwarts Harry Potter-Themed House Database Queries

### Description
Python and SQL programs that manage and query a relational database of Hogwarts student and their house assignments.  
The first program (`import.py`) parses data from a CSV file and loads it into a SQL database.  
The second program (`roster.py`) queries the database to retrieve, filter, and organize information from multiple related tables and provides a list of students in a house, including their names and dates of birth.  
The dataset is based on a simulated scenario inspired by the *Harry Potter* universe.

---

### **Key Concepts**
- Querying relational databases using SQL
- Filtering, grouping, and ordering data in related tables

---

### **Example Output**
```bash
$ python import.py characters.csv
```
```bash
$ python roster.py Gryffindor
```

Lavender Brown, born 1979
Colin Creevey, born 1981
Seamus Finnigan, born 1979
Hermione Jean Granger, born 1979
Neville Longbottom, born 1980
Parvati Patil, born 1979
Harry James Potter, born 1980
Dean Thomas, born 1980
Romilda Vane, born 1981
Ginevra Molly Weasley, born 1981
Ronald Bilius Weasley, born 1980


---


