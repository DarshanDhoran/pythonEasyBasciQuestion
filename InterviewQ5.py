# Q1. Reverse a string:-
def reverse_string(s):
    return s[::-1]
print(reverse_string("Darshan"))

# Q2. find the largest element from the list;
def largest_list(list):
    return max(list)
print(largest_list([1,2,3,4,53,44,11]))

# Q3. Check for the palindrome
def palindrome(s):
    return s == s[::-1]
print(palindrome("madam")) # True
print(palindrome("Darshan")) # false

# Q4. Count the number of vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count 
print(count_vowels("Hello Darshan "))

# Q5. Remove duplicates from the list :
def remove_dupicates_list(list):
    return set(list)
print(remove_dupicates_list([1,2,3,4,4,4,4,4,4,4,4,5]))

# Q5, Find the intersection of two list 
def intersection(lst1,lst2):
    return list(set(lst1) & set(lst2))
print(intersection([1,2,3,4,5],[4,5,6,7]))
    
# Q6. Implement a simple calculator
def calculator(a,b,operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else :
        return "Invalid Operator"
print(calculator(4,2,'+'))
print(calculator(4,2,'/'))

# Q7 Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
