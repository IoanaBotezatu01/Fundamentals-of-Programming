"""
Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k.
For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.
"""


def non_opt(array, k):
    found = 0
    for i in range(len(array)):
        solution = []
        solution.append(array[i])
        if array[i] == k:
            found = 1
            print(solution)
            break
        for j in range(i + 1, len(array)):
            if sum(solution) < k:
                solution.append(array[j])
                if sum(solution) == k:
                    print(solution)
                    found = 1
                    break
            if sum(solution) > k:
                solution.pop()

        if sum(solution) == k:
            found = 1
            break
    if found == 0:
        print("There is no solution for k=", k)


def dynamic_programming(array, k):
    found = 0
    dp_sum = []


    for i in range(len(array)):
        while array[i]>k:
            i=i+1
        p=0
        dp_sum=[]
        solution = []
        solution.append(array[i])
        dp_sum.append(array[i])

        if array[i] == k:  #the element is equal to k
            found = 1
            print(solution)
            print("The 'dynamic-programming' array before printing is:")
            print(dp_sum)
            break

        for j in range(i + 1, len(array)):
            if dp_sum[p] < k:
                solution.append(array[j])
                p = p + 1
                dp_sum.append(dp_sum[p - 1] + array[j])
                print("The 'dynamic-programming' array is:",dp_sum)

                if dp_sum[p] == k:

                    print("The 'dynamic-programming' array before printing is:",dp_sum)

                    found = 1
                    break
            if dp_sum[p] > k:
                solution.pop()
                dp_sum.pop()
                p=p-1  # dp_sum[p] goes back to dp_sum[p-1]
                print("The 'dynamic-programming' array is:", dp_sum)

        if dp_sum[p] == k:
            found = 1
            break
    if found == 0:
        print("There is no solution for k=", k)
    else:
        print(" ")
        print("The solution is:")
        print(solution)



def choose_way():
    print("Choose the way of solving the problem:")
    print("1. Non-Optimized")
    print("2. Dynamic Programming")
    way = int(input("->"))
    array = []
    k = int(input("Choose a number 'k':"))
    s = int(input("Choose the number of the elements of the subset:"))
    print("Choose the elements of the set")

    for i in range(s):
        x = int(input("->"))
        array.append(x)
    sorted(array)
    if way == 1:
        non_opt(array, k)
    else:
        dynamic_programming(array, k)


print(choose_way())
