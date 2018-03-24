import requests

main_page = requests.get('https://114.by/')
assert main_page.status_code == 200
print (main_page.status_code)

route_1 = requests.get('https://114.by/route/5081-minsk-av-tsentralnyj-stolin-av/')
assert route_1.status_code == 200
print(route_1.status_code)

route_2 = requests.get('https://114.by/route/3612-gomel-av-karlsrue-av/')
assert route_2.status_code == 200
print(route_2.status_code)

route_3 = requests.get('https://114.by/route/5973-minsk-av-tsentralnyj-lelchitsy-as/')
assert route_3.status_code == 200
print(route_3.status_code)

route_4 = requests.get('https://114.by/item/kontakty/')
assert route_4.status_code == 200
print(route_4.status_code)

route_5 = requests.get('https://114.by/item/statistika-poiska/')
assert route_5.status_code == 200
print(route_5.status_code)

route_6 = requests.get('https://114.by/route/3636-gomel-av-keln-av/')
assert route_6.status_code == 200
print(route_6.status_code)

route_6 = requests.get('https://114.by/route/15587-rogachev-av-knjazhinka/')
assert route_6.status_code == 200
print(route_6.status_code)

route_7 = requests.get('https://114.by/route/1007-minsk-av-tsentralnyj-gomel-av/')
assert route_7.status_code == 200
print(route_7.status_code)

route_8 = requests.get('https://114.by/bus/station/krasnitsa-4/')
assert route_8.status_code == 200
print(route_8.status_code)

route_9 = requests.get('https://114.by/route/15549-rogachev-av-gomel-av/')
assert route_9.status_code == 200
print(route_9.status_code)

route_10 = requests.get('https://114.by/route/12385-mogilev-av-gomel-av/')
assert route_10.status_code == 200
print(route_10.status_code)

route_10 = requests.get('https://114.by/route/12385-mogilev-av-gomel-av/')
assert route_10.status_code == 200
print(route_10.status_code)

