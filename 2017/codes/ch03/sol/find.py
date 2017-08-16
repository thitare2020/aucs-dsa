# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from random import randint
from time import time


def find(S, val):
    """Return index j such that S[j] == val, or -1 if no such element."""
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j          # a match was found at index j
        j += 1
    return -1


n = 20
DATA = [randint(0, n)] * n
DATA = [randint(0, n) for x in range(n)]
DATA.sort()
print('DATA:', DATA)
DATA[n - 1] = n + 1
print('DATA:', DATA)

key = randint(0, n)
key = DATA[n - 1]
print('key:', key)

start_time = time()
index = find(DATA, key)
end_time = time()

print('index:', index)
elapsed = end_time - start_time
print('Time:', elapsed)
