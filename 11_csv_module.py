# csv = comma separated values

import csv

dir(csv)

# ['Dialect', 'DictReader', 'DictWriter', 'Error', 'QUOTE_ALL', 'QUOTE_MINIMAL', 'QUOTE_NONE', 'QUOTE_NONNUMERIC', 'Sniffer', 'Strin
# gIO', '_Dialect', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', 'excel', 'excel_tab'
# , 'field_size_limit', 'get_dialect', 'list_dialects', 're', 'reader', 'reduce', 'register_dialect', 'unregister_dialect', 'writer'
# ]

stream = """
Title, Year Released, Director
The Godfather, 1972, Francis Ford Coppola
The Shawshank Redemption,1994,Frank Darabont
Citizen Kane,1941,Orson Welles
Rock,,null
"""

path = "D:\\log\\data.csv"
file = open(path)

# for line in file:
#     print line

# Title, Year Released, Director

# The Godfather, 1972, Francis Ford Coppola

# The Shawshank Redemption,1994,Frank Darabont

# Citizen Kane,1941,Orson Welles

# Rock,,null

# lineset = [line.strip().split(',') for line in open(path)]

reader = csv.reader(file)

header = next(reader)   # first line is the header

data = []

for row in reader:
    # string, int, string
    title = row[0]
    year = 1971
    if len(row[1]) > 0:
        year = int(row[1])
    author = row[2]

    data.append([title, year, author])

file1 = open("D:\log\outcome.csv", 'w')
writer = csv.writer(file1)
writer.writerow(["Title", "Year", "Author"])

for i in range(len(data)):
    writer.writerow(data[i])

file1.close()
file.close()