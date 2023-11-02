from prettytable import PrettyTable

def get_table(data):
    table = PrettyTable(['Attribute', 'Value'])

    for key, value in data.items():
        table.add_row([key, value])

    return table
    