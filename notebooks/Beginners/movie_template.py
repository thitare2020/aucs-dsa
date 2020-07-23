import sys


class Movie:
    def __init__(self, id, year, title):
        self.id = int(id)
        # if year == 'NULL':
        #     year = 0
        self.year = int(year)
        self.title = title


for line in sys.stdin:
    data = line.split(',')
    print(data)
    m = Movie(data[0], data[1], data[2])
