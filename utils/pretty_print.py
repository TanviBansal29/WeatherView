import datetime
from prettytable import PrettyTable

def get_table(data):
    table = PrettyTable(['Attribute', 'Value'])

    for key, value in data.items():
        if key == 'sunrise':
            timestamp = data['sunrise']
            datetime_obj = datetime.datetime.fromtimestamp(timestamp)
            value = str(datetime_obj.strftime('%H:%M:%S')) + ' A.M.'
        if key == 'sunset':
            timestamp = data['sunset']
            datetime_obj = datetime.datetime.fromtimestamp(timestamp)
            value = str(datetime_obj.strftime('%H:%M:%S')) + ' P.M.'
        if key == 'max_temp':
            key = 'max_temp(°C)'
        if key == 'min_temp':
            key = 'min_temp(°C)'
        if key == 'temp':
            key = 'temp(°C)'
        if key == 'feels_like':
            key = 'feels_like(°C)'
        if key == 'wind_speed':
            key = 'wind_speed(m/s)'
        table.add_row([key, value])

    return table
    