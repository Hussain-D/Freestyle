"""
Q #4) How to get the non-matching characters in a string?

Answer: To get the non-matching characters in a string, the below steps are followed:

    Hash Map data structure is taken which works with the key-value pair.
    Loop the string, character by character, and verify if that character of the string exists in the hash map or not.
    If the result is true, the counter for the character in the hash map is increased or else then put a count as 1.
    Once the loop ends, then the Hash map is traversed and print the characters with a count equal to 1.

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

     if(c==1){

        System.out.println(ch+ " - " + c);

     }

}
"""

"""#--> 1 dictionaries"""
# s1 = 'abcdef'
# s2 = 'bsdkef'
# l1 = [i for i in s1]
# l2 = [i for i in s2]
# di = {}
# non_mat = []
# for i in l1:
#     if i not in di:
#         di[i] = 1
#     else:
#         di[i] += 1
# for i in l2:
#     if i not in di:
#         di[i] = 1
#     else:
#         di[i] += 1
# for i in di.keys():
#     if di[i]==1:
#         non_mat.append(i)
# print(l1)
# print(l2)
# print(di)
# print(non_mat)

"""#--> 2 sets"""
# s1 = 'abcdef'
# s2 = 'bsdkef'
# set1 = set(i for i in s1)
# set2 = set(i for i in s2)
# print(set1&set2)
# print((set1-(set1&set2))|(set2-(set1&set2)))