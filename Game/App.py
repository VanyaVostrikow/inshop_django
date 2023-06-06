import random
################
def answer():
    ans = [0, 0, 0, 0]
    all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(ans)):
        ans[i] = random.choice(all)
        all.remove(ans[i])
    list_of_str = [str(n) for n in ans]
    ans.clear
    ans = list_of_str
    return ans

##############
def insert(var1):
    var1 = str(var1)
    var1 = list(var1)
    return var1

################

def check(ans, var1):
    result = (0, 0) 
    as_list = list(result)
    for a in range(len(ans)):
            if ans[a] == var1[a]:
                as_list[0] = as_list[0] + 1
            if any(element in var1[a] for element in ans):
                as_list[1] = as_list[1] + 1
    
    return as_list

