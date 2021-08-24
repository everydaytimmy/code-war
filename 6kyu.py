
###-----------VALID BRACES-----------###

# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False


def validBraces(string):
    stack = []
    for char in string:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True

    
###-----------Multiples of 3 or 5-----------###

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    solution_list = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            solution_list.append(i)
    answer = sum(solution_list)
    return answer

    
    
###-----------Stop gninnipS My sdroW!-----------###
# Description:
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
# Examples:

# spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
# spinWords("This is a test") => "This is a test" 
# spinWords("This is another test") => "This is rehtona test"


###------ MY SOLUTION ------###

def spin_words(sentence):
    breakdown = sentence.split()
    list = []
    for item in breakdown:
        if len(item) > 4:
            list.append(item[::-1])
        else:
            list.append(item)
    solution = " ".join(list)
    return solution

###------ ONE LINE SOLUTION ------###

def spin_words_other(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

