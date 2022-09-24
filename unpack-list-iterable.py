

from calendar import c


user_record = ('Alberto', 'alberto@example.com', '79525002', '74102551', '71500025')

name, email, *phones = user_record

print(phones)



#tags

records = [
    ('capitals', 'oslo', 'sucre'),
    ('country', 'bolivia', 'argentina', 'noruega'),
    ('capitals', 'buenos aires', 'asuncion')
]

capitals = []
countries = []

for label, *data in records:
    if label == 'capitals':
        capitals += data
    
    if label == 'country':
        countries += data


print(capitals)
print(countries)

#processing strings.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, dir_home, sh = line.split(':')

print(fields, sh)
