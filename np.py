import numpy as np  
arr = np.array([10, 30, 50, 20, 40, 80])
arr_copy = arr.copy()
arr_copy[0] = 99
arr_appended = np.append(arr, [60,70])
arr_inserted = np.insert(arr, 2, 25)
arr_sorted = np.sort(arr)
arr_sorted = np.sort(arr_appended)
arr_deleted = np.delete(arr, 1)
split_arr = np.array_split(arr, 2)
arr2 = ["Syed", "Farhad", "Agha",]
combinwd = np.concatenate((arr.astype(str), arr2))
print("Original Array:", arr)
print("Copied Array:", arr_copy)
print("After Appending:", arr_appended)
print("After Inserting 25 at index 2:", arr_inserted)
print("Sorted Array:", arr_sorted)
print("After Deleting index 1:", arr_deleted)
print("Split Array:", split_arr)
print("Concatenated Array:", combinwd)

arr3 = np.array([1,2,3])
arr4 = np.array([4.1,5.3])
arr5 = np.array(["A", "B"])
arr6 = np.array(["D", "E", "F"])
combinwd = np.concatenate((arr3, arr4, arr5, arr6,))
print("After Combining:", combinwd)
import numpy as np  
arr = np.array([[10, 60, 30], [40, 50, 60]])
np.save('Save.npy', arr)
loaded_arr = np.load('Save.npy')


float_arr = arr.astype(float)

b = np.array([1,2,3])

print("Loaded Array:\n", loaded_arr)
print("Element at row 1, col 2:", arr[1, 2])
print("Values greater than 30:", arr[arr>30])
print("Type casting to float:\n", float_arr)

print("Broadcasting Addition:\n", arr +b)

print(arr)
print("Addition:\n", arr + 5)
print("Subtraction:\n", arr - 10)
print("Multiplication:\n", arr * 2)
print("Division:\n", arr /10)
print("Exponentiation:\n", arr ** 2)
print("Square Root:\n", np.sqrt(arr))
print("Exponential:\n", np.exp(arr))
print("Sine Value:\n", np.sin(arr))
print("Maximum value:", np.max(arr))
print("Mean value:", np.mean(arr))
print("median value:", np.median(arr))
print("Mode value:", np.bincount(arr.flatten()).argmax())
print("Standard Deviation:", np.std(arr))