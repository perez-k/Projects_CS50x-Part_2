from sys import argv, exit
import cs50
import csv

if len(argv) != 2:
    print("Usage: python import.py filename.csv")
    exit (1)

open("students.db", "w")
db = cs50.SQL("sqlite:///students.db")

with open(f"{argv[1]}", "r") as data:


    for row in reader:
    print (row[])