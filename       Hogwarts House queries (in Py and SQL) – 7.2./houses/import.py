from sys import argv, exit
import cs50
import csv

# CHECK NUMBER OF COMMAND LINE ARGUMENT
if len(argv) != 2:
    print("Usage: python import.py filename.csv")
    exit(1)

open("students.db", "w")                              # Setup a database connexion
db = cs50.SQL("sqlite:///students.db")
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth INTENGER)")

# OPEN CSV FILE GIVEN BY COMMAND LINE ARGUMENT
with open(f"{argv[1]}", "r") as data:                 # Open the csv file

    reader = csv.DictReader(data)
    for row in reader:
        nmsp = row["name"].split()                    # Split the student's name

        if len(nmsp) == 2:                            # If no middle name , declare middle name = None
            nmsp.insert(2, 0)
            nmsp[2] = nmsp[1]
            nmsp[1] = None

        Fnm = nmsp[0]                                 # Firstname
        Mnm = nmsp[1]                                 # Middle name
        Lnm = nmsp[2]                                 # Last name

        # INSERT THE STUDENT's INFORMATION INTO THE students TABLE OF students.db
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",
                   Fnm, Mnm, Lnm, row["house"], row["birth"])