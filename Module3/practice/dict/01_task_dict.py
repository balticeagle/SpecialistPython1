# Дан словарь, содержащий данные о товаре из магазина
# "price" - цена товара в валюте "currency"
# "count" - количествотовара в магазине
# Считая,что курс доллара равен dollar_rate
# Вычислите стоимость всех товаров с названием "name" в долларах

item = {"name": "Кроссовки", "price": "7540.5", "currency": "usd", "count": "20"}
dollar_rate = 74.12
value = 0
if item["currency"]=="usd":
    value = int(item["count"])*float(item["price"])
print(value)
