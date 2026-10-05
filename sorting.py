'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def selection_sorting(l):
    print(l)
    arr_len = len(l)
    print(arr_len)
    
    swapped_count = 0

    for j in range(0, arr_len):
        print(f" j = {j}")
        smallest = l[j]
        smallest_index = j
        # For loop to identify the smallest number
        for i in range(j, arr_len):
            print(f" i = {i}")

            if l[i] < smallest:
                smallest = l[i]
                smallest_index = i
                swapped_count += 1
        
        print(f"Smallest current = {smallest}")
        l[j], l[smallest_index] = l[smallest_index], l[j]
        
        print(f"Current list:: {l}")
    
    print(f"Total Swapped  = {swapped_count}")
        
            
def bubble_sort(l):
    arr_len = len(l)
    swapped_count = 0
    
    for j in range(1, arr_len):
        # print(f" j = {j}")
        for i in range(arr_len -j):
            print(f" i = {i}")
            if l[i] > l[i+1]:
                print(f"Swapping!! - {l[i]} with {l[i+1]}")
                l[i], l[i+1] = l[i+1], l[i]
                swapped_count += 1
        
        print(f"Curr list  = {l}")
    
    print(f"Total Swapped  = {swapped_count}")
# Online Python compiler (interpreter)
# Write and run Python online using this editor.

    
def merge_sort(l):
    # split the list in 2 halves
    
    arr_len = len(l)
    if arr_len <= 1:
        return l
    elif arr_len == 2 and l[0] > l[1]:
        return [l[1], l[0]]
    elif arr_len == 2 and l[0] <= l[1]:
      return l
    else:
    
        if arr_len % 2 != 0:
            print("in if")
            left_half = l[0:arr_len//2+1]
            right_half = l[(arr_len//2+1):arr_len]
        else:
            print("in else")
            left_half = l[0:arr_len//2]
            right_half = l[((arr_len//2)):arr_len]
        
    print(f"left : {left_half}")
    print(f"right : {right_half}")

    for i in l:
        merge_sort(left_half)
    for j in l:
        merge_sort(right_half)
    

in_l = [7,0,3,4,1,6,2,5,-1,19,6]
# selection_sorting(in_l)
# bubble_sort(in_l) 21

merge_sort(in_l)
