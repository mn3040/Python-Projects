# Author: <Matthew Nunez>

import random

FACE_CARD_VALUE = 10
ACE_VALUE = 1
CARD_LABELS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
BLACKJACK = 21
DEALER_THRESHOLD = 16


####### DO NOT EDIT ABOVE ########

def deal_card():
    """Evaluates to a character representing one of 13
    cards in the CARD_LABELS tuple
    :return: a single- or double-character string representing a playing card
    >>> random.seed(13)
    >>> deal_card()
    '5'
    >>> deal_card()
    '5'
    >>> deal_card()
    'J'
    """
    card = random.choice(CARD_LABELS)
    return card

def get_card_value(card_label):
    """Evaluates to the integer value associated with
    the card label (a single- or double-character string)

    :param card_label: a single- or double-character string representing a card
    :return: an int representing the card's value

    >>> card_label = 'A'
    >>> get_card_value(card_label)
    1
    >>> card_label = 'K'
    >>> get_card_value(card_label)
    10
    >>> card_label = '5'
    >>> get_card_value(card_label)
    5
    """

    if card_label == "A":
        return ACE_VALUE

    # need to fix this
    elif card_label == "2":
        return 2
    elif card_label == "3":
        return 3
    elif card_label == "4":
        return 4
    elif card_label == "5":
        return 5
    elif card_label == "6":
        return 6
    elif card_label == "7":
        return 7
    elif card_label == "8":
        return 8
    elif card_label == "9":
        return 9
    elif card_label == "10" or card_label == "J" or card_label == "Q" or card_label == "K":
        return FACE_CARD_VALUE

def deal_cards_to_player():
    """Deals cards to the player and returns the card
    total

    :return: the total value of the cards dealt
    """
    draw1 = deal_card()
    draw2 = deal_card()
    total_of_draws = get_card_value(draw1) + get_card_value(draw2)
    print("Player drew " + str(draw1) +" and " +str(draw2)+".")
    print("Player's total is "+ str(total_of_draws) + ".\n")
    hit_or_stay = input("Hit (h) or Stay (s)? ")

    while hit_or_stay == "h":
        x = deal_card()
        get_card_value(x)
        total_of_draws += get_card_value(x)
        print("\nPlayer drew "+str(x)+".")
        print("Player's total is "+str(total_of_draws)+".\n")
        if total_of_draws > (BLACKJACK-1):
            return total_of_draws
        hit_or_stay = input("Hit (h) or Stay (s)? ")

    if hit_or_stay == "s":
        print()
        return total_of_draws

    while not hit_or_stay == "h" and not hit_or_stay == "s":
        hit_or_stay = input("\nHit (h) or Stay (s)? ")
    return total_of_draws


def deal_cards_to_dealer():
    """Deals cards to the dealer and returns the card
    total

    :return: the total value of the cards dealt
    """

    dealer_draw1 = deal_card()
    dealer_draw2 = deal_card()
    total_of_draws = get_card_value(dealer_draw1) + get_card_value(dealer_draw2)
    print("The dealer has "+str(dealer_draw1)+" and "+str(dealer_draw2)+".")
    print("Dealer's total is "+str(total_of_draws)+".\n")

    while not total_of_draws > DEALER_THRESHOLD:
        x = deal_card()
        get_card_value(x)
        total_of_draws += get_card_value(x)
        print("Dealer drew "+str(x)+".")
        print("Dealer's total is "+str(total_of_draws)+".\n")
        if total_of_draws > BLACKJACK:
            return total_of_draws
    return total_of_draws

def determine_outcome(player_total, dealer_total):
    """Determines the outcome of the game based on the value of
    the cards received by the player and dealer. Outputs a
    message indicating whether the player wins or loses.

    :param player_total: total value of cards drawn by player
    :param dealer_total: total value of cards drawn by dealer
    :return: None
    """
    if player_total > dealer_total or dealer_total > BLACKJACK and not (player_total > BLACKJACK):
        print("YOU WIN!\n")
    else:
        print("YOU LOSE!\n")

def play_blackjack():
    """Allows user to play Blackjack by making function calls for
    dealing cards to the player and the dealer as well as
    determining a game's outcome

    :return: None
    """
    print("Let's Play Blackjack!\n")

    player = deal_cards_to_player()

    if player > BLACKJACK:
        print("YOU LOSE!\n")
    else:
        dealer = deal_cards_to_dealer()
        determine_outcome(player, dealer)

    play_again = input("Play again (Y/N)?")

    while play_again != "Y" and play_again != "N":
        play_again = input("\nPlay again (Y/N)?")
    while play_again == "Y":
        print()
        player = deal_cards_to_player()
        if player > BLACKJACK:
            print("YOU LOSE!\n")
        else:
            dealer = deal_cards_to_dealer()
            determine_outcome(player, dealer)
        play_again = input("\nPlay again (Y/N)?")
    if play_again == "N":
        print("\nGoodbye.")




def main():
    """Runs a program for playing Blackjack with one player
    and a dealer
    """

    # call play_blackjack() here and remove pass below
    play_blackjack()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == "__main__":
    #Remove comments for next 4 lines to run doctests
    #print("Running doctests...")
    #import doctest
    #doctest.testmod(verbose=True)

    #print("\nRunning program...\n")

    main()
