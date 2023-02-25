import statistics as st
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

median = st.median(list1)
print(median)

# Alternative Method
sorted_list = sorted(list1)
if len(sorted_list)%2 == 0:
    mid1 = sorted_list[len(sorted_list)//2]
    mid2 = sorted_list[(len(sorted_list)//2) - 1]
    med = (mid1 + mid2) / 2
else:
    med = sorted_list[len(sorted_list)//2]
print(med)