database = [
            ['stephen', '123'],
            ['stan', '222'],
            ]

name = raw_input('Enter user name: ')
pwd = raw_input('Enter password: ')

if [name, pwd] in database:
    print 'Access Granted!'