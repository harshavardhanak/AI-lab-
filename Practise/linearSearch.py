def linearSearch(list,ele):
    flag = False
    i = 0
    while ( i < len(list) and not flag ):
        if(list[i]==ele):
            flag = True 
        else :
            i+=1
    return flag 
list = []
for i in range(1,10):
    num = input("Number {} : ".format(i))
    list.append(num)
ele = input("Enter the element to be found : ")
found = linearSearch(list,ele)
print("Element found :",found)
