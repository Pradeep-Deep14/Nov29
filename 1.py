def counter(start=0):
    count=start
    def increment():
        nonlocal count
        count+=1
        return count
    return increment

count1=counter(5)
count2=counter()

result=count1()+count2()
print(result)