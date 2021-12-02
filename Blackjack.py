print("   Welcome to #Black_Jack #Solitaire #21\n")
import random

J = Q = K = 10
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
dealer = []
player = []
dealer.append(random.choice(cards))
player.append(random.choice(cards))
player.append(random.choice(cards))
dealer.append("*")
print(f"Dealer Cards: {dealer}\nYour Cards: {player}\n")
dealer.pop(1)
dealer.append(random.choice(cards))


def ace(k, lis, i):
    while k != 1 and k != 11:
        k = int(input('Enter "1" or "11" for "ACE": '))
        lis[i] = k
    return k


def start(lis):
    for i in range(0, 2):
        if lis == dealer:
            if lis[i] == "A":
                lis[i] = random.choice([1, 11])
        elif lis[i] == "A":
            lis[i] = ace(0, lis, i)


def fun(lis):
    start(lis)
    if sum(lis) == 21 and lis == dealer:
        print("Dealer's Blackjack!\nYou lose! ")
        exit()
    elif sum(lis) == 21 and lis == player:
        print("Blackjack!\nYou win! ")
        exit()

    while sum(lis) < 22:
        if lis == player:
            I = input('Press "Enter" or "S" to stand: ').lower()
            if I == "s":
                print(f"Your total score: {sum(lis)}")
                break
        k = random.choice(cards)
        if lis == player and k == "A":
            lis.append(k)
            k = ace(k, lis, len(lis) - 1)
        elif lis == dealer and k == "A":
            if sum(dealer) <= 10:
                dealer.append(random.choice([1, 11]))
            else:
                dealer.append(1)
        elif k != "A":
            lis.append(k)
        if lis == player:
            print(f"Your Cards: {lis}\n")
        if sum(lis) > 21:
            if lis == player:
                print(f"Bust! You Lose!\nDealer's Cards:{dealer}")
                exit()
        if lis == dealer and sum(dealer) <= 21:
            if sum(dealer) >= 17:
                if sum(dealer) < sum(player):
                    print("Dealer Cards:", dealer, "\nYou Win!")
                elif sum(dealer) == sum(player):
                    print("Dealer Cards:", dealer, "\nDraw match!")
                elif sum(dealer) > sum(player):
                    print("Dealer Cards:", dealer, "\nYou lose!")
                exit()
        elif lis == dealer and sum(dealer) > 21:
            print(f"Dealer's Cards: {lis}\nDealer Bust! You Win!")
            exit()
    return sum(lis)


P = fun(player)
D = fun(dealer)
