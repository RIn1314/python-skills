from interval import Interval, IntervalSet

'''
    Python 数值区间处理 interval 库的快速入门
    
'''
# 设置一个区间
zoom_2_5 = Interval(2, 5)
print(zoom_2_5)
print(2 in zoom_2_5)
print(6 in zoom_2_5)

# 设置一个区间（开区间、闭区间）
zoom_o2_5 = Interval(2, 5, lower_closed=False)
print(zoom_o2_5)
print(2.01 in zoom_o2_5)

# 设置一个时间区间
officeHours = IntervalSet.between("08:00", "17:00")
officeHours2 = Interval("08:00", "17:00")
print('18:00' in officeHours)
print('18:00' in officeHours2)

# 设置一个IP区间
IP_set = IntervalSet.between("1.1.1.1", "12.12.12.12")
IP_set2 = Interval("1.1.1.1", "12.12.12.12")

print('10.10.10.10' in IP_set)

print('12.12.13.12' in IP_set2)




