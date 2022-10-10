# Задание №1
# text = b'r\xc3\xa9sum\xc3\xa9'
# decode_1 = text.decode()
# print(decode_1)
# code = decode_1.encode("latin1")
# print(code)
# decode_2 = code.decode("latin1")
# print(decode_2)

# Задание №2
# text_1 = input("Введите первую строку: ")
# text_2 = input("Введите вторую строку: ")
# text_3 = input("Введите третью строку: ")
# text_4 = input("Введите четвёртую строку: ")
# file = open("text.txt", "w")
# file.write(f"{text_1} \n{text_2} \n")
# file.close()
# file = open("text.txt", "a")
# file.write(f"{text_3} \n{text_4}")
# file.close()
# file = open("text.txt", "r")
# print(file.read())

# Задание№3
# import json
#
# list = {
# "000001": ("Kate", 23),
# "000002": ("Ann", 25),
# "000003": ("Ivan", 31),
# "000004": ("Nikita", 29),
# "000005": ("Liza", 27),
# "000006": ("Mark", 26)
# }
#
# with open('data.json', 'w') as file:
#     json.dump(list, file)
#
# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data)
