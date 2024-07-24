# import random


# # def insertion_sort(x):
# #     for i in range(0, len(x)):
# #         min = x[i]
# #         pos = i
# #         for j in range(i, len(x)):
# #             if x[j] > min:
# #                 min = x[j]
# #                 pos = j
# #         x.pop(pos)
# #         x.insert(0, min)


# # x = []
# # for p in range(0, 5):
# #     x.append(random.randint(random.randint(0, 9), 19))

# # print(x)

# # insertion_sort(x)
# # print(x)


# # def binary_search(x, i, j, e):
# #     if i < j and i != 0 and j != 0:
# #         m = (i+j)//2
# #         if x[m] < e:
# #             i = m
# #         elif x[m] > e:
# #             j = m
# #         else:
# #             return m
# #         x = binary_search(x, i, j, e)

# def binary_search(x, i, j, e):
#     if i > j:  # Base case: element not found
#         return -1

#     m = (i + j) // 2

#     if x[m] < e:
#         i = m+1
#     elif x[m] > e:
#         j = m-1
#     else:
#         return m

#     return binary_search(x, i, j, e)


# x = [4, 7, 11, 12, 13, 17]
# print(binary_search(x, 0, 5, 7))
