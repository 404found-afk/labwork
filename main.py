print('Здравствуйте, вас приветствует казино "Удача"! Ваш баланс: 1000')
balance = 1000
wins = 0
loses = 0
b = 0

while True:
    command = input("Введите команду: ").strip().lower()

    if command == "balance":
        print(balance)
    elif command == "history":
        print(f'Всего побед: {wins}, вссего поражений: {loses}')
    elif command == "exit":
        break
    else:
        try:
            commandd, summa, stavka = command.split()
            if commandd == "bet":
                try:
                    summa = int(summa)
                    if summa > balance:
                        print("У вас недостаточно баланса.")
                    else:
                        if stavka == "even":
                            if (wins + loses) % 2 == 0:
                                balance += summa
                                print("Поздравляю, вы выграли.")
                                wins += 1
                            else:
                                balance -= summa
                                print("К сожалению, вы проиграли.")
                                loses += 1
                        elif stavka == "odd":
                            if (wins+loses)%2 == 1:
                                balance += summa
                                print("Поздравляю, вы выграли.")
                                wins += 1
                            else:
                                balance -= summa
                                print("К сожалению, вы проиграли.")
                                loses += 1
                        else:
                            print("Неверная ставка.")
                except TypeError:
                    print("Неверно введена сумма.")
            else:
                print("Команда не найдена.")
        except:
            print("Неверный ввод команды.")