from netschool import NetSchool

client = NetSchool('', '')

client.login()

print(client.work('2024-12-23','2024-12-27'))

client.logout()

