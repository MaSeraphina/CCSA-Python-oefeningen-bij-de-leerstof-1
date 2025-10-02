# def selection_sort(a):  
#     n = len(a)
#     for i in range(n-1, 0, -1):
#         pos_max = i 
#         max = a[i]
#         for j in range(i-1, -1 , -1):
#             if a[j] > max:
#                 pos_max = j
#                 max = a[j]
#         #nieuw max gevonden
#         a[pos_max], a[i] = a[i], a[pos_max]
#         print(a)



def selection_sort_vooraan(a):
    n = len(a)
    for i in range(n-1):
        pos_min = i 
        mini = a[i]
        for j in range(i+1,n, 1):
            if a[j] > mini:
                pos_min = j
                mini = a[j]
        #nieuw max gevonden
        a[pos_min], a[i] = a[i], a[pos_min]
        print(a)

            




# selection_sort([44,55,88,11,12,90, 201, 1])
# selection_sort_vooraan([44,55,88,11,12,90, 201, 1])

a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)

