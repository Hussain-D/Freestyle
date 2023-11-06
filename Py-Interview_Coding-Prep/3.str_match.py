"""
Q #3) How to get the matching characters in a string?
Answer: To get the matching characters in a string, the below steps are followed:

    Hash Map data structure is taken which works with the key-value pair.
    Loop the strings, character by character, and verify if that character of the string exists in the hash map or not.
    If the result is true, the counter for the character in the hash map is increased or else then put a count as 1.
    Once the loop ends, then the Hash map is traversed and print the characters with more than 1 count.

Code snippet:

HashMap<Character, Integer> mp = new HashMap<> ();

   for (int j = 0; j<text.length (); j++) {

       char ch = text.charAt(j);

          if(mp.containsKey(ch)){

                int cnt = mp.get(ch);

             mp.put(ch, ++cnt);

         }else{

            mp.put(ch, 1);

          }

}

Set<Character> charct = map.keySet();

for (Character ch: charct){

     int c= mp.get(ch);

     if(c>1){

        System.out.println(ch+ " - " + c);

     }

}
"""

"""#--> 1 Naive approach"""
# st1,st2 = 'abcd','bsdk'
# list_of_chars = []
# for i in st1:
#     if i in st2:
#         list_of_chars.append(i)
# print(list_of_chars)

"""#--> 2 list compre"""
# st1,st2 = 'abcdef','bsdkef'
# list_of_chars = [i for i in st1 if i in st2]
# print(list_of_chars)

"""#--> 3 sets"""
# s = "abcdef"
# ss = "bsdkef"
# l = [i for i in s]
# ll = [i for i in ss]
# print(set(l)&set(ll))