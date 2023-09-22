def binary_search(li,var):
    left=0
    right=len(li)-1
    while left<=right:
        mid=(left+right)//2
        if li[mid]>var:# 目标值在左边
            right=mid-1
        elif li[mid]<var:
            left=mid+1
        elif li[mid]==var:
            return mid
    return None
if __name__ == '__main__':
    li=[1,2,3,4,5,6,7,8,9,10]
    print(li[binary_search(li, 4)])


