# write a function 
# for a str passed in
# returns the maximum num of equal parts

# Your code here
    #initial thought
    #1.break s into [a,b,c,...]
    #2.suppose X is the pattern of alphabet being repeated, test each possible number as lenOfX
    #divide array.length by lenOfX
    
    
    #for loop:
    #for i, i++

#method 1: using index of string
# first just for test case 1:
def helper(s):
    letter_1 = s[0]
    for j in range(len(s)):
        letter_2 = s[j]
        if letter_1 == letter_2:
            return j
        else:
            j += 1
# def solution(s):
#     index = helper(s)
#     if s[0:index] == s[index:2*index] and s[index:2*index] == s[2*index:3*index] and  s[2*index:3*index] == s[3*index:4*index]:# and i*index<len(s) is probably included
#         return 4
#     else:
#         return 0 #meaning the given str cannot be divided 


#test case 1
#input
str = 'abcabcabcabc'

# print(solution(str))
#output
# 4

#Next: I could just google the problem now..
# Method 2: separate as i parts 
# 
# Method 3: see if from left onwards and from right onwards I can use s[index]. So also needs two pointers for indexes.
#  and assume str is dividable
def solution(s):
    #case where the given str cannot be divided 
    if len(s) < 0:
        return 0
    #define pointers
    pointer_1 = 0
    pointer_2 = len(s) - 1

    #set storage variables
    str_1 = ''
    str_2 = ''

    #loop for pointers to move from two ends of str
    while pointer_1 < pointer_2:
        str_1 += s[pointer_1]
        str_2 = s[pointer_2] + str_2
        #activate if statement for when str_1 is equal to str_2 && str_1 is equal to the str of same length right after the first index
        if str_1 == str_2 and str_1 == s[pointer_1+1:(pointer_1+len(str_1)+1)]: # +1 is just to offset machine starting from 0
            return len(s)/len(str_1)
        pointer_1 +=1
        pointer_2 -=1
    # if left and right does not equal at all, leave loop at midpoint
    return 1

#test case
#input
str= 'abccbaabccba'
print(solution(str))

#output
#2.0 # decimal, no matter if I write return len(s)/len(str_1)