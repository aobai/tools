#!/usr/local/bin/python3
# coding=utf8

import pandas as pd
import os
import csv
path = '/Users/aobai/Downloads/txy0109.csv'
data = pd.read_csv(path)


xxx = pd.read_csv('/Users/aobai/Downloads/ip_info.csv')

data.columns = ['http_refer1','http_refer2','mid','buvid','ip','fid','fver','roomid','loadtime','buffertimes','result','c_mid','playurl','delta_ts','guid','error_code','is_https','ctime','xxx','xxxxxxxx']

one_data =data[ data['http_refer1'].str.contains('KHTML')]
two_data =data[ data['http_refer1'].str.contains('KHTML') == False] 

one_columns = ['fid','is_https']
two_columns = ['ip','error_code']
one = pd.DataFrame(one_data,columns = one_columns)
two = pd.DataFrame(two_data,columns = two_columns)

one.columns = two_columns


all = pd.concat([one,two],axis = 0)


en  = all[all['ip'].isin(['209.150.148.39'])]

ip = all.ip.unique()
ip = pd.DataFrame(ip)
ip.to_csv('ip_list.csv')
ip.to_csv('ip_list.csv',index=False,header=False)

# province_list = ['上海', '安徽', '山东', '江苏', '浙江', '福建', '广东', '广西', '海南', '内蒙古', '北京',
#        '天津', '山西', '河北', '江西', '河南', '湖北', '湖南', '云南', '四川', '西藏', '贵州',
#        '重庆', '宁夏', '新疆', '甘肃', '陕西', '青海', '吉林', '辽宁', '黑龙江']

# inland =  data[data['province'].isin(province_list)]

# overseas = data[~data['province'].isin(province_list)]


# inland_avg = inland['cartun_times'].sum() / inland['play_sum_durations'].sum()
# overseas_avg = overseas['cartun_times'].sum() / overseas['play_sum_durations'].sum()



'''
classified by  country id 
'''

country_inland  = backup[backup['country'] == 0]
country_overseas = backup[backup['country'] == 1]

country_inland_avg = country_inland['cartun_times'].sum() *60/ country_inland['play_sum_durations'].sum()
country_overseas_avg = country_overseas['cartun_times'].sum() *60/ country_overseas['play_sum_durations'].sum()
