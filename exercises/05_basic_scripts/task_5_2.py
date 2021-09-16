# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_net = input('Введите сеть:')
ip, prefix_mask = ip_net.split('/')
oct1, oct2, oct3, oct4 = ip.split('.')
prefix_mask = int(prefix_mask)
zero = 32 - prefix_mask
mask = str(prefix_mask * '1' + zero * '0')
moct1, moct2, moct3, moct4 = mask[:8], mask[8:16], mask[16:24], mask[24:]


print(f'''
Network:
{int(oct1):<10}{int(oct2):<10}{int(oct3):<10}{int(oct4):<10}
{int(oct1):>08b}  {int(oct2):>08b}  {int(oct3):>08b}  {int(oct4):>08b}''')

print(f'''
Mask:
{'/' + str(prefix_mask)}
{int(moct1, 2):<10}{int(moct2, 2):<10}{int(moct3, 2):<10}{int(moct4, 2):<10}
{moct1:<8}  {moct2:<8}  {moct3:<8}  {moct4:<8}''')