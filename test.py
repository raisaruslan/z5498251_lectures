from http.cookiejar import uppercase_escaped_char

str1 = '''John said: "Let's learn Python together"'''
print(str1)
a = 2.0
print(a)
b = 2.5
print(a + b)
4/2
print(4/2)
i = 1
test = i == 1
print(test)
f = 0.2 + 0.2 + 0.2
print(f)
print(f == 0.6) #True
import math
f = 0.2 + 0.2 + 0.2
print(f)
print(math.isclose(f,0.6))
i = 2
type(i)
print('3' + '2')
print( 3 + 2)
x = 1
print(type(x))
x = str('abc')
xup = str.upper(x)  # str.upper refers that we want to use uppercase
print(xup)          # --> 'ABC' (lower to uppercase)
x = str('raisa')
xup = str.upper(x)
print(xup)          # ---> 'RAISA'
y = 'iqmal'.upper() # second method to transform to uppercase fx
print(y)
baby = 'MaLoveRaisa'
baby = 'MaLoveRaisa'.upper()
print(baby)
baby = 'MALOVERAISA'.lower()
print(baby)
a = True
b = 5
print(f"The value of a is {a} and the value of b is {b}") # method 1 with 'f'
a = True
b = 5
print("The value of a is {} and the value of b is {}".format(a,b)) # method 2 with .format
L1 = True
print(type(L1))
str_ = 'this is a string'
x = str(5)
print(x)
L = 56
W = 33
H = 30.5
volume = L*W*H
print(volume)
Length = 56
Width = 33
Height = 30.5
volume = Length * Width * Height
print(f"the volume of the box is {volume} cubic centimeters.")
lst_a = [1]
lst_a.append(2)
print(lst_a)
lst = [1,"string",True,None,True]
print(f"Original lst is {lst}")
lst.remove(True)
print(f"lst after removing the first True is {lst}")
lst.pop(2)
print(f"lst after removing the element CURRENTLY at index 2 is {lst}")
lst.pop()
print(f"lst after removing the element CURRENT at index 2 is {lst}")
import re
result = re.findall(r'@\w+', 'From firstname.surname@unsw.edu.au Mon Sep 16 10:10:15 2024')
print(result)
domain = 'From firstname.surname@unsw.edu.au Mon Sep 16 10:10:15 2024'.split()[1].split('@')[1]
print(domain)
x = "1788-01-26"
print(x)
uni_coffee_price = 4.5
team_size = 4
num_meetings = 5
total_coffee_cost = uni_coffee_price*team_size*num_meetings
print(total_coffee_cost)
x = "I don't know what a regular expression is"
print(x)
x = True
print(x)
hours = int(input('Enter the number of hours worked'))
Normalrate = 51.48
Overtimerate = 88.9

if hours <= 35:
    Payment = ((hours - 35) * Overtimerate) + (35 * Normalrate)
print(f'Total payment is {Payment} dollars')
numbers = [-2, 3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15, 10]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f'The largest value is {largest}')
print('RAISA, z5498251')

for i in range (1,4):
    for y in range (i,4):
        if i <= y:
            print(i, y)

w = "What"
i = "IS"
c = "CamelCase?"

print (f'{w} {i} {c}')

a = 'This is called'
b = 'problem'
a = f'{a} Parsons {b}'
b = print
b(a

import yfinance as yf

def yf_pr_to_csv(tic, pth, start=None, end=None)
    df = yf.download(tic, start=start, end=end, ignore_tz=True)
    df.to_csv(pth)

tic = 'QAN.AX'
pth = 'qan_stk_prc.csv'
yf_pr_to_csv(tic, pth)
if __name__ == "__main__":
    tic = 'QAN.AX'
    datadir = "/Users/raisa/Desktop/toolkit/data"
    pth = os.path.join(datadir, 'qan_stk_prc.csv')  # Path to save the CSV

    # Call the function to download and save data
    yf_pr_to_csv(tic, pth)

print ('Raisa, z5498251')

import os
import yfinance as yf

# Function to download stock data and save as CSV
def yf_pr_to_csv(tic, pth, start=None, end=None):
    df = yf.download(tic, start=start, end=end, ignore_tz=True)  # Download stock data
    df.to_csv(pth)  # Save data to CSV file

# Main execution
if __name__ == "__main__":
    tic = 'QAN.AX'  # Stock ticker
    datadir = '/Users/raisa/Desktop/toolkit/data'  # The correct path to your data folder
    pth = os.path.join(datadir, 'qan_stk_prc.csv')  # Path to save the CSV file

    # Call the function to download and save the data
    yf_pr_to_csv(tic, pth)

    # Print a success message
    print(f"The stock data for {tic} has been saved to {pth}")
    print('Raisa, z5498251')

for i in range (0, 5):
    print(f"i is now {i}")
for i in range(0, 5, 1):
    print(f"i is now {i}")
for even in range(0, 10, 2):
    print(f"even is {even}")

def my_function(y):
    y = y + x
    x = 2
    y = y + x
    return y

x = 3
y = 10

y = my_function(x)

prc_dic = {
    '3000-01-15': 7.0400,
    '2020-01-14': 7.1100,
    '2020-01-13': 7.0200,
    '2020-01-02': 7.1600,
    '2020-01-03': 7.1900,
    '2020-01-06': 7.0000,
    '2020-01-07': 7.1000,
    '2020-01-08': 6.8600,
    '2020-01-09': 6.9500,
    '2020-01-10': 7.0000,
}

# replace '???' with the correct expression
sorted_keys = [key for key in sorted(prc_dic)]
prc_dic['2020-01-15'] = prc_dic.pop['3000-01-15']

print(sorted_keys)
print(prc_dic)

def count_words_in_file(file_name):
    with open(file_name, 'r') as file:
        word_count = {}

        for line in file:
            words = line.split()

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    return word_count

def find_most_frequent_word(file_name):
    word_count = count_words_in_file(file_name)

    most_frequent_word = None
    highest_count = 0

    for word, count in word_count.items():
        if count>highest_count:
            highest_count = count
            most_frequent_word = word

    print(f"The most frequent word is: '{most_frequent_word}.appear {highest_count} times")
    return most_frequent_word, highest_count

file_name = 'iso.txt'
find_most_frequent_word(file_name)
