# Reading From File

Use `input()` to read from the program's standard input.

```python
x = input('Your Name')
y = input()
```

`input()` reads until the end of line (EOL) is found. If we run our program (ex my_prog.py) at the console. The program will wait keyboard inputs until the Enter key is pressed.
```
python my_prog.py
```
However, it is not efficient to type the same input everytime we test the program. In this case, we can have all the inputs in one file (ex data01.in) and feed it into the program directly.

For example
```
python my_prog.py < data01.in
```
`input()` returns a string. If we wish to process a series of numbers, we need to `split()` and convert the data type.
`split()` returns a list of string delimitted by white spaces (spaces and tabs).
```python
alist = input().split()
```
Converting each element in the list into, for example, integer, let python do the trick with.
```python
alist = input().split()
int_list = [int(x) for x in alist]
```
or shorten it with
```python
int_list = [int(x) for x in input().split()]
```

# Exercise
Given a data file, the first line is N, the second line is M, and the rest are M lines of data in [X,Y]list. Write a Python program to read from the data file into designated variables.
```
2
5
1 3
5 9
4 1
6 7
1 4
```
