"""
Q #6) How do you prove that the two strings are anagrams?

Answer: Two strings are called anagrams if they accommodate a similar group of characters in a varied sequence.

To check if two strings are anagrams, the below steps are followed:

    Initialize two strings in two variables.
    Check if the length of the two strings is similar, if not then the strings are not an anagram.
    If the result is true, take the two strings and store them in a character array.
    Sort the two character arrays, then check if the two sorted arrays are alike.
    If the result is true, the two strings are anagram else, not anagram.

Code snippet:

if (str1.length() != str2.length()) { 

       System.out.println(str1 + " and " +str2 + " not anagrams string"); 

}else{

        char[] anagram1 = str1.toCharArray(); 

         char[] anagram2 = str2.toCharArray();

         Arrays.sort(anagram1); 

         Arrays.sort(anagram2);

          anagrmstat = Arrays.equals(anagram1, anagram2);

}

if (anagrmstat == true) {

     System.out.println(str1 + " and " +str2 + " anagrams string"); 

}else{

    System.out.println(str1 + " and " +str2 + " not anagrams string"); 

        }

}
"""

s1 = input('1 --> ')
s2 = input('2 --> ')

def ana(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        l1 = [i for i in s1.lower()]
        l2 = [i for i in s2.lower()]
        l1.sort()
        l2.sort()
        print(l1,l2)
        return True if (l1==l2) else False
    
print(ana(s1,s2))