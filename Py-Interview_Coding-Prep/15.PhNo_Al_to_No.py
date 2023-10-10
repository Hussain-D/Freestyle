"""
1. All phone numbers will be 10 digits.
2. Two repeating digits will be shortened using the word "double".
   Three repeating digits will be shortened using the word "triple".
   If the digits repeat four or more times, they will be shortened using
   "double" and "triple" multiple times(see example four).
3. The input will be always valid. For example, we won't have a scenario like
   "double double two". The valid case will be "double two double two"
4. The entire input will be in lowercase.

Input: "two one nine six eight one six four six zero"
Output: "2196816460"

Input: "fie one zero two four eight zero double three two"
Output: "5102480332"

Input: "five one zero six triple eight nine six four"
Output: "5106888964"

Input: "five eight double two double two four eight five six"
Output: "5822224856"
"""

def getPhoneNumber(s):
    listStr = list(s.split())
    dicNums = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    numStr = ''
    i = 0
    while(i<len(listStr)):
        if listStr[i]=='double':
            numStr += 2*str(dicNums[listStr[i+1]])
            i += 2
            continue
        if listStr[i]=='triple':
            numStr += 3*str(dicNums[listStr[i+1]])
            i += 2             
            continue
        numStr += str(dicNums[listStr[i]])
        i += 1
    return numStr

s = input()
print(getPhoneNumber(s))

"""
Answer given in ChatGPT

"""
def getPhoneNumber(s):
    dicNums = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    listStr = list(s.split())
    ph_no = []
    i = 0
    while i < len(listStr):
        
        current_word = listStr[i]
        
        if current_word in ['double','triple']:
            count = 2 if current_word=='double' else 3
            repeated_digit = listStr[i+1]
            ph_no.append(str(dicNums[repeated_digit]) * count)
            i += 2
            
        else:
            ph_no.append(str(dicNums[current_word]))
            i += 1
            
    return ''.join(ph_no)

s = input()
print(getPhoneNumber(s))