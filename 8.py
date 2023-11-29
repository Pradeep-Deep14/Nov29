list1=["1.0","a","0.1","1","-1"]
list2=sorted(list1,key=lambda
             x:float(x) if x.isdigit() else float('inf'))
print(list2)