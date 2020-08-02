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
        usingShake = True if input('Using shake?(y/n)') == 'y' else False
        usingLoops = True if input('Using loops?(y/n)') == 'y' else False
        loops = 0
        if usingLoops:
            loops = int(input('Enter loops value: '))
        if secondChoice == '1':
            seed = input('Enter password seed: ')
            if usingLoops:
                password.loopGenMD5(seed, loops)
            elif usingShake:
                password.generateShakeMD5(seed)
            elif usingLoops and usingShake:
                password.loopGenShakeMD5(seed, loops)
            else:
                password.generateMD5(seed)
        if secondChoice == '2':
            seed = input('Enter password seed: ')
            if usingLoops:
                password.loopGenSHA256(seed, loops)
            elif usingShake:
                password.generateShakeSHA256(seed)
            elif usingLoops and usingShake:
                password.loopGenShakeSHA256(seed, loops)
            else:
                password.generateSHA256(seed)
        if secondChoice == '3':
            seed = input('Enter password seed: ')
            if usingLoops:
                password.loopGenSHA512(seed, loops)
            elif usingShake:
                password.generateShakeSHA512(seed)
            elif usingLoops and usingShake:
                password.loopGenShakeSHA512(seed, loops)
            else:
                password.generateSHA512(seed)
        print(f'Generated password: {password.getPassword()}')
    elif chioce == 'x':
        break