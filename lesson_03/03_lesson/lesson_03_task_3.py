from address import Address
from mailing import Mailing

# Адрес отправителя
from_addr = Address("123456", "Москва", "Тверская", "10", "25")
# Адрес получателя
to_addr = Address("654321", "Санкт-Петербург", "Невский проспект", "20", "5")

# Почтовое отправление
mail = Mailing(to_addr, from_addr, 500, "RU123456789CN")

# Вывод в требуемом формате
print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
      f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
      f"{mail.to_address.house} - {mail.to_address.apartment}. Стоимость {mail.cost} рублей.")