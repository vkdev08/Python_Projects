from random import randint


def calculate_score(hand):
    score = sum(hand)
    ace_cnt = hand.count(11)
    while score > 21 and ace_cnt:
        score -= 10
        ace_cnt -= 1
    return score


# Game setup constants
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
N = len(cards)-1
cards_at_start = 2


# Main Loop: ask the user to start or quit game
while True:
    n = input("Do you want to play the game of BlackJack ? Type 'y or 'n': ")
    if n == 'n':
        print("The game has been successfully ended.")
        break

    # initialize player and dealer hands for a new round
    p1 = []
    comp = []
    for i in range(cards_at_start):
        p1.append(cards[randint(0, N)])
    score_p1 = calculate_score(p1)
    score_comp = 0

    # Dealer draw cards until score_comp is atleast 17 (BlackJack Rule)
    while score_comp < 17:
        new_card_1 = cards[randint(0, N)]
        comp.append(new_card_1)
        score_comp += new_card_1
        score_comp = calculate_score(comp)

    # Show initial player hand and computer first card
    print(f"Your cards: {p1}, current score: {score_p1}")
    print(f"Computer's First Card: {comp[0]}")

    # Player turn: Draw cards if number less that 21 and wants to continue
    while score_p1 < 21:
        n1 = input("Type 'y' to get another card, type 'n' to pass: ")
        if n1 == 'y':
            new_card = cards[randint(0, N)]
            p1.append(new_card)
            score_p1 += new_card
            score_p1 = calculate_score(p1)
            print(f"Your cards: {p1}, current score: {score_p1}")
        else:
            break

    # Final hands and result evaluation
    print(f"Your final cards: {p1}, final score: {score_p1}")
    print(f"Computer final cards {comp}, final score: {score_comp}")

    if (score_p1 > 21):
        if not score_comp > 21:
            print("You went over. You lose!")
        else:
            print("Double busted!!")
    else:
        if score_comp > 21:
            print("Computer Busted!")
        elif score_comp < score_p1:
            print("You win")
            if score_p1 == 21:
                print("You got a BlackJack!")
        elif score_comp == score_p1:
            print("It's a draw!!")
        else:
            print("You lose!")
            if score_comp == 21:
                print("Computer got a BlackJack!")
