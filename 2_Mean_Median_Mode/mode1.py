list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency[i] = frequency.get(i, 0) + 1
print(frequency)
# high = 0
# for key, val in frequency.items():
#     if val > high:
#         high = val
#         highkey = key
# print(highkey)

high = max(frequency, key=frequency.get)
print(high)
