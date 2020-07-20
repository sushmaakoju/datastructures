from dynamicarray import DynamicArray

#Dynamic Array
arr = DynamicArray()
arr.append("first")
arr.append("second")
arr.append("fifth")
arr.append("sixth")
arr.append("seventh")
arr.insert_at(2, "fourth")
arr.insert_at(0, "zeroeth")
arr.insert_at(3, "third")
print(len(arr))
for i in range(0,len(arr)):
    print(i)
for i in range(0,len(arr)):
    print(arr.get(i))
arr.remove("second")
for i in range(0,len(arr)):
    print(arr.get(i))
arr.remove_at(4)
for i in range(0,len(arr)):
    print(arr.get(i))
arr.clear()
print(len(arr))