"""
Python program by John Chakauya

This is a python program to get a single string from two given strings, separated by a space and swap the first two
characters of each string.

Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""


def mix_strings(a, b):  # function to mix the two strings
    new_str1 = b[:2] + a[2:]  # using string slicing and assignment to generate and store new value of the first string
    new_str2 = a[:2] + b[2:]  # using string slicing and assignment to generate and store new value of the second string

    return new_str1 + ' ' + new_str2  # returning the new string values as the output


str1, str2 = 'abc', 'xyz'
print('Initial sample string is: ' + str1 + ' ' + str2)  # to display the intial string values before swapping
print('Output Result: ' + mix_strings(str1, str2))  # calling the string mixing function with two sample strings

print('\nEnter a blank to exit...\n')  # informing the user to enter a blank to exit the program loop
while str1 and str2 != "":  # while loop to allow the user to enter string values multiple times
    str1 = input("Enter a value for the first string: \n")  # prompting user to enter value for the first string
    str2 = input("Enter a value for the second string: \n")  # prompting user to enter value for the second string
    if str1 and str2 != "":
        print('Output Result: ' + mix_strings(str1, str2))  # displaying the output for the user entered values
