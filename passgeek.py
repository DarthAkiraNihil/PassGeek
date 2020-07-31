import api, info

password = api.Password()
print(f'Passgeek v. {info.version}')
while True:
    print('1. Generate password randomly')
    print('2. Generate password with hash algorithm')
    print('Prees x for exit')
    chioce = input('>')
    if chioce == '1':
        length = int(input('Enter password length: '))
        password.generateRandom(length)
        print(f'Generated password: {password.getPassword()}')
    if chioce == '2':
        print('1. Generate with MD5')
        print('2. Generate with SHA256')
        print('3. Generate with SHA512')
        secondChoice = input('>')
        if secondChoice == '1':
            seed = input('Enter password seed: ')
            password.generateMD5(seed)
        if secondChoice == '2':
            seed = input('Enter password seed: ')
            password.generateSHA256(seed)
        if secondChoice == '3':
            seed = input('Enter password seed: ')
            password.generateSHA512(seed)
        print(f'Generated password: {password.getPassword()}')
    elif chioce == 'x':
        break