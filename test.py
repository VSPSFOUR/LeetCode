def exceptSelf(arr : list):
    cummlative_product = 1
    new_arr  = list(range(len(arr)))
    for i in range(len(arr)):
        new_arr[i] = cummlative_product
        cummlative_product*=arr[i]
    print(new_arr)
    cummlative_product = 1
    for j in range(len(arr) -1 , -1, -1):
        new_arr[j] *= cummlative_product
        cummlative_product *= arr[j]
        
        
    return new_arr
# exceptSelf([1, 2, 3, 4])
print(exceptSelf([1, 2, 3, 4]))