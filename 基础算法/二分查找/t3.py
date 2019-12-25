def Biseach(list,a):
    s_list=sorted(list)
    max=len(s_list)-1
    min=0
    while min<=max:
        mid=int(max+min)
        if a == s_list[mid]:
            return mid
        elif a>s_list[mid]:
            min=mid+1
        else:
            max=mid-1
    return -1



if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5,6]
    re = Biseach(list1, 5)
    print(re)
