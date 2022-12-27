import random

all_suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
all_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
all_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
        
playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = [] 
        for every_suit in all_suits:
            for every_rank in all_ranks:
                self.deck.append(Card(every_suit, every_rank))
    
    def __str__(self):
        complete_deck = ''  
        for every_card in self.deck:
            complete_deck +=  '\n' + '\n' + every_card.__str__()
        return 'The deck has the following cards:' + complete_deck

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        one_card = self.deck.pop()
        return one_card

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0 
    
    def add_card(self,hand_card):
        self.cards.append(hand_card)
        self.value += all_values[hand_card.rank] 
        if hand_card == 'Ace': 
            self.aces = self.aces + 1

    def adjust_for_ace(self):
        while self.value>=21 and self.aces>0:
            self.value = self.value - 10
            self.aces = self.aces - 1

class Chips:
    
    def __init__(self):
        self.bet = 0

        while True:
            try:
                self.total = input("\nPlease select how much money do you want to start with \n" + "\n" + "(Please don't enter any letters, and only integer numbers larger than zero):")
                if self.total.isdigit():
                    self.total=int(self.total)
                    print(f"You start with", self.total, "chips.")
                    break  
            except ValueError:
                print("Please don't enter any letters, and only integer numbers larger than zero. ")

    def win_bet(self):
        self.total = self.total + self.bet
    
    def lose_bet(self):
        self.total = self.total - self.bet


def take_bet(betting_chip):
    total_permitted_bet_value = betting_chip.total
    
    while True:
        
        bet_entered = input("How many chips would you like to bet?")
        if bet_entered.isdigit():
            bet_entered = int(bet_entered)
            if bet_entered <= total_permitted_bet_value and bet_entered > 0:
                betting_chip.bet = bet_entered
                print("You start with", betting_chip.bet, "chips.")
                break
            else:
                print("Sorry, your bet can't exceed ", "$", total_permitted_bet_value)
        else:
            print("Please don't enter numbers larger than ", total_permitted_bet_value, ", smaller than zero, or letters.")


    
        if total_permitted_bet_value <=0:
            print("You have run out of chips. Game over!")
            playing = False
        

def hit(deck_hit,hand_hit):

    single_card = deck_hit.deal()    
    hand_hit.add_card(single_card)
    hand_hit.adjust_for_ace()

def hit_or_stand(deck_hit_or_stand,hand_hit_or_stand):
    global playing  
    while playing:
        user_input = input("Would you like to Hit or Stand? Enter 'H' or 'S'")
        if user_input[0].lower() == 'h':
            hit(deck_hit_or_stand, hand_hit_or_stand)

        elif user_input[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    
    print("\nCroupier's hand:")
    print(dealer.cards[0]) 
    print("\nYou can't see the croupier's second card yet.")
    for every_card in player.cards:
        print("\n" f"Player's hand: ", str(every_card))

def show_all(player,dealer):
    
    for every_card in dealer.cards:
        print("\n" f"Croupier's hand: ", str(every_card))
    print("Croupier hand's value: ", dealer.value)
    for every_card in player.cards:
        print("\n" f"Player's hand: ", str(every_card))
    print("Player hand's value: ", player.value)

def player_busts(player, dealer, chips_played):
    print("You bust! (Exceeded 21 points.)")
    chips_played.lose_bet()

def player_wins(player, dealer, chips_played):
    print("You win!")
    chips_played.win_bet()

def dealer_busts(player, dealer, chips_played):
    print("You win! The croupier busted (exceeded 21 points.)")
    chips_played.win_bet()
    
def dealer_wins(player, dealer, chips_played):
    print("The croupier wins the hand!")
    chips_played.lose_bet()
    
def push(player, dealer):
    print("It's a push! (You have an equal value to the croupier.)")

print("Welcome to Don Jon's Blackjack!")
print("Get as close to 21 as you can without going over!")
print("Dealer hits until it reaches 17. Aces count as 1 or 11.")

player_chips = Chips()

while True:

    game_deck = Deck()
    game_deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(game_deck.deal())
    player_hand.add_card(game_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(game_deck.deal())
    dealer_hand.add_card(game_deck.deal())
    
    take_bet(player_chips)
        
    show_some(player_hand, dealer_hand)
    
    while playing:        
        
        hit_or_stand(game_deck, player_hand)

        show_some(player_hand, dealer_hand)       
        
        if player_hand.value >= 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    
        if player_hand.value <= 21:
        
            while dealer_hand.value < 17:
                hit(game_deck, dealer_hand)    

        show_all(player_hand, dealer_hand) 
    
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand,dealer_hand)       

    print(f"You have: ", player_chips.total, "chips.")

    if player_chips.total <= 0:
        playing=False
        print("You have run out of chips. Game over. Thanks for playing!")
        break
    
    new_game = input("Would you like to play another hand? Enter 'Y' or 'N': ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    if new_game[0].lower()=='n':
        print("Thanks for playing!")
        playing=False
        break
    else:
        if new_game[0].lower()!='y' or new_game[0].lower()!='n':
            print("Please enter 'y' or 'n' ONLY.")
            new_game = input("Would you like to play another hand? Enter 'Y' or 'N': ")
            if new_game[0].lower()=='y':
                playing=True
                continue
            if new_game[0].lower()=='n':
                print("Thanks for playing!")
                playing=False
                break
        else:
            print("Thanks for playing!")
            break
