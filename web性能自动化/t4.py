# 开始前先启动chrome，启动chrome必须带上参数`--remote-debugging-port=9222`开启远程调试否则无法与chrome交互
import pychrome

browser = pychrome.Browser('http://127.0.0.1:%d' % 9222)
tab = browser.new_tab()
tab.start()
tab.Runtime.enable()
tab.Page.navigate(url='https://testerhome.com/topics/16883')
# 设置等待页面加载完成的时间
tab.wait(10)
# 运行js脚本
timing_remote_object = tab.Runtime.evaluate(
    expression='performance.timing'
)
# 获取performance.timing结果数据
timing_properties = tab.Runtime.getProperties(
    objectId=timing_remote_object.get('result').get('objectId')
)
timing = {}
for item in timing_properties.get('result'):
    if item.get('value', {}).get('type') == 'number':
        timing[item.get('name')] = item.get('value').get('value')
print('performance.timing:{}'.format(timing),'\n','*'*50)


# 获取performance.getEntries()数据
entries_remote_object = tab.Runtime.evaluate(
    expression='performance.getEntries()'
)

entries_properties = tab.Runtime.getProperties(
    objectId=entries_remote_object.get('result').get('objectId')
)
entries_values = []
for item in entries_properties.get('result'):
    if item.get('name').isdigit():
        url_timing_properties = tab.Runtime.getProperties(
            objectId=item.get('value').get('objectId')
        )
        entries_value = {}
        for son_item in url_timing_properties.get('result'):
            if (son_item.get('value', {}).get('type') == 'number' or
                    son_item.get('value', {}).get('type') == 'string'):
                entries_value[son_item.get('name')] = son_item.get('value').get('value')
        entries_values.append(entries_value)
print('performance.getEntries:{}'.format(entries_value)+ '\n'+'*'*50)

