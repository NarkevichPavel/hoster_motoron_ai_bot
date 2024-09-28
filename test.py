from datetime import datetime

date_sale = '2024-08-22'
date_object = datetime.strptime(date_sale, '%Y-%m-%d')
formatted_date = date_object.strftime('%d.%m.%Y')

print(formatted_date)
