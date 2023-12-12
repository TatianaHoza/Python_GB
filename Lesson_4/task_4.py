'''Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
'''
from random import randint

lst = [2, 8, 7, 1, 3, 9]


def bubble_sort(nums):
    n = 1
    while n < len(nums):
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        n += 1
    return nums
print(bubble_sort(lst))
def quick_sort(nums, start = 0, end = 1):
    if end == -1:
        end = len(nums)-1
    if start >= end:
        return

    i,j = start,end
    pivot = nums[randint(start,end)]

    while i <= j:
        while nums[i] < pivot:
            i+=1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i],nums[j] = nums[j],nums[i]
            i,j = i+1,j-1
    quick_sort(nums,start,j)
    quick_sort(nums,i, end)

print(quick_sort(lst))

