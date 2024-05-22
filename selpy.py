# lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def limit(lists, min_list = None, max_list = None):
#     cheak_min = lambda val: True if min_list is None else (min_list >= val)
#     cheak_max = lambda val: True if max_list is None else (max_list <= val)
    
#     return [val for val in lists if cheak_min(val) and cheak_max(val)]


# print(limit(lst, 4, 9))
# anw = 7

# que = [lst.index(i) for i in lst if i == anw]
# print(que)




# def limit(lists, min_list = None, max_list = None):
#     cheak_min = lambda val: True if min_list is None else (min_list >= val)
#     cheak_max = lambda val: True if max_list is None else (max_list <= val)
    
#     return [val for val in lists if cheak_min(val) and cheak_max(val)]



# print(limit(lists, 3, 3))3



# def limit(lst, min = None, max = None):
#     cheak_min = lambda val: True if min  is None else (val >= min) 
#     cheak_max = lambda val: True if max is None else (val <= max)
    
#     return[val for val in lst if cheak_min(val) and cheak_max(val)]

# print(limit(lists, max=6))



# def limit(lst, min = None, max = None):
#     l = []
#     if min:
#         for val in lst:
#             if val >= min:
#                 l.append(val)
                
#     if max:
#         for val in lst:
#             if val <= max:
#                 l.append(val)

#     print(l)
    
    
# limit(lists, min=5)    





# def limit(lst, min=None, max=None):
#     cheak_min = lambda val: True if min is None else (val >= min)
#     cheak_max = lambda val: True if max is None else (val <= max)
    
    
#     return[val for val in lst if cheak_max(val) and cheak_min(val)]


# print(limit(lists, min=5))













# def limit(lst, min = None, max = None):
#     cheak_min = lambda val: True if min is None else (val >= min) 
#     cheak_max = lambda val: True if max is None else (val <= max)
    
    
#     return[val for val in lst if cheak_min(val) and cheak_max(val)]  


# print(limit(lists, min = 5, max= 8))



















# sentence = [1, 1, 2, 2, 3, 8, 8, 8, 8, 8, 8, 6, 7, 8, 0, 0, 0, 2, 2, 
#             5, 2, 3, 4, 5, 6]

# count = {}
# f_val = 0
# result = []
# for index in sentence:
#     if index in count:
#         count[index] += 1
#     else:
#         count[index] = 1
    
# # anw = sorted(count.items(),key= lambda kw:kw[1], reverse=True)

# f_val = max(count.values())

# for i in count.keys():
#     if count[i] == f_val:
#         result.append(i)
        

# print(result)





# print([val for val in count])
# print([val for val in count if val > 2 ])






from string import ascii_letters



def encrypt(abs:str, key:int) -> str:
    alpha = ascii_letters    
    result = ''
    
    for i in abs:
        if i not in alpha:
            result += i
        else:
            new_key = alpha.index(i) + key            
            result += alpha[new_key]
            
    return(result)


def decrypt(abs:str, key:int) -> str:
    key *= -1
    return encrypt(abs, key)


def brute_force(abs: str) -> dict:
    alpha = ascii_letters
    key = 1
    result = ''
    burte_force_data = {}
    
    while key <= len(alpha):
        result = decrypt(abs, key)
        burte_force_data[key] = result
        result = ''
        key += 1
        
    return(burte_force_data)           
    
print(sorted(brute_force("Alislm1241").items(),reverse=True))








