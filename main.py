import casino_data as data

print('Здравствуйте, вас приветствует казино "Удача"! Ваш баланс: 1000')
balance = 1000
wins = 0
loses = 0
in_streak = False

while True:
    command = input("Введите команду: ").strip().lower()

    if command == "balance":
        print(f"Ваш текущий баланс: {balance}")
    elif command == "help":
        data.show_help()
    elif command == "history":
        print(f'Всего побед: {wins}, всего поражений: {loses}')
    elif command == "exit":
        print("Спасибо за игру! До свидания.")
        break
    else:
        try:
            commandd, amount_str = command.split()
            if commandd == "bet":
                try:
                    amount = int(amount_str)

                    new_balance = data.make_bet(balance, amount)
                    if new_balance is not None:
                        balance = new_balance
                        wins, loses, balance, in_streak = data.spin(wins, loses, balance, amount, in_streak)
                except ValueError:
                    print("Неверно введена сумма. Введите целое число.")
            else:
                print("Команда не найдена. Введите 'help' для списка команд.")
        except ValueError:
            print("Неверный ввод команды. Введите 'help' для списка команд.")