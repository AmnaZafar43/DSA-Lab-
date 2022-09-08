def SearchA(Arr,x):
    for i in range(0,len(Arr)):
        if(Arr[i] == x):
           print('{}{}'.format("Index: ", i))
            
Arr = [22,2,1,7,11,13,5,2,9]
x = input("Enter the number:  ")
x = int(x)
SearchA(Arr, x)