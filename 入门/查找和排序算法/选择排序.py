#算法思想
#遍历列表，每次从列表中去除最小的数字，然后添加到新的列表中
import random
def select_simple(li):
    li_new=[]
    for i in range(len(li)):
        min_val=min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new
# 优化之后的选择排序
def select_sort(li):
    for i in range(len(li)-1):
        min_lic=i
        # 这个for循环是为了找到无序区别最小元素的下表
        for j in range(i+1,len(li)):
            if li[j]<li[min_lic]:
                min_lic=j
        li[i],li[min_lic]=li[min_lic],li[i]
if __name__ == '__main__':
    lis=[random.randint(1,100) for i in range(12)]
    # lis=[1,3,4,5,76,8]
    print('没有排序的数组为：',lis)
    # 因为返回的是一个新的数组，所以需要使用一个的新的数组来接受
    new_lis=select_simple(lis)
    print('排序之后的数组为：',new_lis)
    # 使用优化之后的选择排序
    list_1 = [random.randint(1, 100) for i in range(23)]
    print('没有排序的list_1列表',list_1)
    print('优化之后的选择排序')
    select_sort(list_1)
    print('优化之后的选择排序的结果',list_1)