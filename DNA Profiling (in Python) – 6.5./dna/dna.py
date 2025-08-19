import csv
from sys import argv



database_reader = dict()

# Check if command-line arguments (argv) = 3
if len(argv) != 3:
    print("Usage: python dna.py database sequence")
    exit(1)

# Open the csv file and dna squence and read contents into memory
# Open the database CSV file
database_file = open(argv[1], "r")
database_reader = csv.DictReader(database_file)

# Open the DNA sequence text file
sequence_file = open(argv[2], "r")
dna_sequence = sequence_file.read()

# Dictionary to store: key = STR -> values = longest consecutive repeat count in the DNA sequence
str_max_repeats = {}


# For each str in the database header, compute the longest run of consecutive repeats
for str_pattern in database_reader.fieldnames:
    str_length = len(str_pattern)

    current_index = 0
    consecutive_counts = [0]  # List of consecutive counts for current STR
    block_index = 0
    position = 0

    while current_index in range(len(dna_sequence)):
        current_index = position
        end_index = position + str_length

        if dna_sequence[position:end_index] == str_pattern:
            consecutive_counts[block_index] += 1
            position += str_length
        else:
            if consecutive_counts[block_index] > 0:
                block_index += 1
                consecutive_counts.insert(block_index, 0)
                position += 1
            else:
                position += 1

    # Record the maximum consecutive repeat count for the STR
    str_max_repeats[str_pattern] = max(consecutive_counts)

# Remove the "name" field (not an STR)
del str_max_repeats["name"]

sequence_file.close()

# Compare computed STR profile with each person in the database (each row in the csv file)
for person_row in database_reader:
    match_flags = list()
    for str_pattern in str_max_repeats:
        if str_max_repeats[str_pattern] == int(person_row[str_pattern]):
            match_flags.append(1)
        else:
            match_flags.append(0)

    # If all STR counts match, print the person's name and exit
    if all(match_flags):
        print(person_row["name"])
        exit(0)

print("No match")

database_file.close()
