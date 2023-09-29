"""
Q #5) How to calculate the number of vowels and consonants in a string?

Answer: To calculate the number of vowels and consonants in a string, the below steps are followed:

    Get the string on which count has to be performed.
    Run a loop from 0 to the length of the string.
    Take a single character at a time and verify if they are a part of the group of vowels.
    If the result is true, increase the count of vowels or else increment the count of consonants.

Code snippet:

for (int k = 0; k < text.length(); k++) {

    char c = text.charAt(k);

    if (c == 'a' || c == 'e' || c == 'i' ||

       c == 'o' || c == 'u')

              owls += vowls

else

            consonts += consonts

}

System.out.println("Vowel count is " + vowls);

System.out.println("Consonant count is: " + consonts); 
"""

st = 'abcdefghijklmnopqrstuvwxyz'
vowels = ['a','e','i','o','u']
count = 0
for i in st:
    if i in vowels:
        count += 1
print('Vowels =',count)
print('Consonants = ',len(st)-count)