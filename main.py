import EnDeCode


# BAR for select command
def mainBar():
    flagForExit = True
    commands = ['exit', 'help', 'encode', 'decode']
    while flagForExit:
        askString = input("Enter command: ")

        if askString == commands[0]:
            flagForExit = False

        elif askString == commands[1]:
            print(F'Команда {commands[2]} - режим шифрования')
            print(F'Команда {commands[3]} - режим расшифрования')
            print(F'Команда {commands[1]} - помощь')
            print(F'Команда {commands[0]} - выйти из программы')


        # Begin program
        elif askString == commands[2]:
            EnDeCode.encode()

        elif askString == commands[3]:
            EnDeCode.decode()

        else:
            print('Command not found')

# MAIN
if __name__ == '__main__':
    mainBar()