
# -- DAY FOUR ------

'''
1. Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1.
'''
#--- using a function only
def array_product(a,b):
    c = []
    for i in range(len(a)):
        for i in range(len(b)):
            c.append(a[i]*b[i])
        return c


x1 = 1,2,3,4,5
x2 = 6,7,8,9,10
print(array_product(x1, x2))

# -- using a function with list comprehension
def array_dot_product(a,b):
    return[i*j for i,j in zip(a,b)]

print(array_dot_product(x1, x2))

'''
2. Write a short Python function that counts the number of vowels in a given
character string.
'''
def count_vowels(string):
    '''
    Count the number of vowels in a string

    param string: string input
    return: the number of vowels in the string
    '''
    vowels = ['a','e','i','o','u']
    count = 0
    for i in string.lower():            # convert the string to lower case
        if i in vowels:
            count += 1
        else:
            pass
    print("No of vowels in {} are:".format(string), count)

count_vowels('admin')
count_vowels('Automatically')
count_vowels("INDEPENDENCE")
count_vowels("Psst")

# --- to get the number of specific vowels in the string ---

def count_specific_vowels(str):
    ''' 
    Count the number of specific vowels in a string

    param string: string input
    return: dictionary with specific number of vowels in the string
    ''' 
    vowels = ['a','e','i','o','u']
    count_dict = {}
    for i in str.lower():
        if i in vowels:
            count = str.lower().count(i)
            count_dict[i] = count
    print(count_dict)

count_specific_vowels("Francise")
count_specific_vowels("Interdenominational")

'''
3. Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
'''

# -- Method One ---
def remove_punctuation(s):
    ''' 
    Removes punctuations from a sentence.

    param s: string sentence
    return: the sentence without any punctuation
    ''' 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in s:
        if char not in punctuations:
            no_punct =  no_punct + char
    print(no_punct)

remove_punctuation("K'onyango: A young man, old.")

# -- Method Two ---
def remove_punct(s):
    ''' 
    Removes punctuations from a sentence.

    param s: string sentence
    return: the sentence without any punctuation
    ''' 
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for punct in s:
        if punct in punctuations:
            s = s.replace(punct,"")
    print(s)

remove_punct("Edward, Fred and David: Very good buddies!")
