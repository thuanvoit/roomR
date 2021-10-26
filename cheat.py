import re
lst = ['10:30pm Wednesday, November 3, 2021 - N518 - Available',
'11:00pm Wednesday, November 3, 2021 - N518 - Available',
'11:30pm Wednesday, November 3, 2021 - N518 - Available']

for item in lst:
    if re.search('2021', item):
        print(item)