from sys import argv, exit
import cs50

# CHECK NUMBERS OF COMMAND-LINE AEGUMENTS
if len(argv) != 2:
    print("Usage: python roster.py house'sname")
    exit(1)


open("students.db", "r")
db = cs50.SQL("sqlite:///students.db")                         # Setup a database connexion
Alist = list()
# QUERY DATABASE FOR ALL STUDENTS IN HOUSE GIVEN IN COMMAND-LINE ARGUMENT (SORTED ALPHABETICALLY BY LAST  THEN FIRST NAME)
Alist = db.execute(f"SELECT first, middle, last, birth FROM students WHERE house = '{argv[1]}' ORDER BY last, first")
# db.execute(...) return a list of Python dictionnary store in Alist; each dict represent a row in the table

# PRINT EACH STUDENT's FULL NAME AND BIRTH YEAR
i = 0
for i in range(len(Alist)):                                     # For each student
    Xdic = dict()
    Xdic = Alist[i]

    if Xdic["middle"] == None:                                  # If no middle name, print first and lastname and birth year
        F = Xdic["first"]
        L = Xdic["last"]
        B = Xdic["birth"]

        print(f"{F} {L}, born {B}")

    else:                                                       # Else if middle name, print first, middle and lastname and birth year
        F = Xdic["first"]
        M = Xdic["middle"]
        L = Xdic["last"]
        B = Xdic["birth"]

        print(f"{F} {M} {L}, born {B}")
