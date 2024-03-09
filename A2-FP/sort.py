def bubblesort(v,step):
    n=len(v)
    nr=0
    ok=0

    for i in range(n-1):
        for j in range(0,n-i-1): #Last i elements will be sorted after i steps

            if v[j]>v[j+1]:
                nr=nr+1
                ok=1
                v[j],v[j+1]=v[j+1],v[j]
                if nr==step:
                    print("The array after ",step," steps:",v)
                    nr=0

        if ok==0:
             break  #if we don't have to make a swap,it means the array is sorted


    print("The sorted array is:",v)



def shellsort(v,step):
    n=len(v)
    gap=n//2
    nr=0
    while gap >0:
        j=gap
        while j<n:
            i=j-gap
            while i>=0:
                if v[i]<v[i+gap]:
                    break
                else:
                    v[i],v[i+gap]=v[i+gap],v[i]
                    nr=nr+1
                    if nr==step:
                        print("The array after ",step," steps:",v)
                        nr=0
                i=i-gap #we have to check left side
            j+=1
        gap=gap//2

    print("The sorted array is:",v)



def choosesort():
    a=int(input("Choose a method for sorting the array:"))
    step=int(input("step="))
    n=int(input("Number of elements:"))
    v=[]
    for i in range (n):
        x=int(input('->'))
        v.append(x)
    print("Unsorted list is:",v)


    if a==1:
        print(bubblesort(v,step))
    elif a==2:
        print(shellsort(v,step))
    else:
        print("Choose the number 1 or 2.")

print(choosesort())





