import random


def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(0,len(li)-i-1):
            if li[j]<li[j+1]:
                li[j+1],li[j]=li[j],li[j+1]
    return li

if __name__ == '__main__':
    li=[1,34,5,7,83,3]
    print(bubble_sort(li))
    li_ran=[random.randint(0,1000) for i in range(20)]
    print(li_ran)
    bubble_sort(li_ran)
    print(li_ran)

