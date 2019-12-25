import requests

url = 'https://www.cnblogs.com/yoyoketang/p/8035428.html'
reponse_time_list =[]
for i in range(10):
    r = requests.get(url)
    # print(r.text)
    reponse_time = r.elapsed.total_seconds()
    # print(r.elapsed)
    reponse_time_list.append(reponse_time)
    print("第{}次".format(i+1),reponse_time)

avg_time = sum(reponse_time_list)/10.00
all_time = sum(reponse_time_list)
print('all_time:{},ave_time:{}'.format(all_time,avg_time))