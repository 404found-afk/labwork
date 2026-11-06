import random

TEXTS = {
    "win": "Поздравляю, вы выиграли! (x2)",
    "lose": "К сожалению, вы проиграли.",
    "jackpot": "ДЖЕКПОТ! Вы сорвали куш! (x5)",
    "streak_start": "ЧЕРЕДА НЕУДАЧ! Вы проиграли.",
    "streak_loss": "ЧЕРЕДА НЕУДАЧ продолжается! Вы снова проиграли."
}

PROBABILITIES = {
    "jackpot": 5,
    "win": 40,
    "streak": 5,
    "lose": 50
}


def show_help():
    text = (
        "balance: Показует текущий баланс",
        "history: Показывает историю игр на текущий момент",
        "bet (amount): Совершает ставку",
        "exit: Выход из игры"
    )
    for i in range(len(text)):
        print(text[i])


def make_bet(balance, amount):
    if amount <= 0:
        print("Ставка должна быть больше нуля.")
        return None
    if amount > balance:
        print("У вас недостаточно средств.")
        return None
    return balance - amount


def random_result():
    rand_num = random.randint(1, 100)

    if rand_num <= PROBABILITIES["jackpot"]:
        return 'jackpot'
    elif rand_num <= PROBABILITIES["jackpot"] + PROBABILITIES["win"]:
        return 'win'
    elif rand_num <= PROBABILITIES["jackpot"] + PROBABILITIES["win"] + PROBABILITIES["streak"]:
        return 'streak'
    else:
        return 'lose'


def spin(wins, loses, balance, amount, in_streak=False):
    if in_streak:
        balance -= amount
        print(TEXTS["streak_loss"])
        loses += 1
        return wins, loses, balance, False

    play = random_result()

    if play == 'jackpot':
        balance += amount * 5
        print(TEXTS["jackpot"])
        wins += 1
    elif play == 'win':
        balance += amount * 2
        print(TEXTS["win"])
        wins += 1
    elif play == 'streak':
        balance -= amount
        print(TEXTS["streak_start"])
        loses += 1
        return wins, loses, balance, True
    elif play == 'lose':
        balance -= amount
        print(TEXTS["lose"])
        loses += 1

    return wins, loses, balance, False