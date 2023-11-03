TABLE_HEADER = f"{'Date':20}{'Max temp':10}{'Min temp':10}{'Avg temp':10}{'Windspeed':10}{'Humidity':10}{'Rain':10}{'Sunrise':10}{'Sunset':10}"

date = '2023-11-03'
max_temp = '31.9'
min_temp = '21.0'
avg_temp = '25.8'
winspeed = '8.9'
humid = '23.0'
rain = '0'
sunr = '06:41 AM'
suns = '05:44 PM'

print(TABLE_HEADER)
print(f'{date:20}{max_temp:10}{min_temp:10}{avg_temp:10}{winspeed:10}{humid:10}{rain:10}{sunr:10}{suns:10}')
'''
2023-11-04
31.8
21.8
26.1
9.4
21.0
0
06:41 AM
05:43 PM
2023-11-05
32.2
20.0
25.8
8.1
19.0
0
06:42 AM
05:43 PM
'''