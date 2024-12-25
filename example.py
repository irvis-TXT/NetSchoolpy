from netschool import NetSchool

client = NetSchool('ЕфимовР11', 'EfimowR114')

client.login()

print(client.work('2024-12-23','2024-12-27'))

client.logout()

