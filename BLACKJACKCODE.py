import random
print("WELCOME TO THE GAME OF BLACKJACK!")
rules=input('Do you know how to play? If you want the rules to play, type "yes" or else type "no"' )
if rules=='yes':
    print("""Blackjack hands are scored by their point total. The hand with the highest total wins as long as it doesn't exceed 21; a hand with a higher total than 21 is said to bust. Cards 2 through 10 are worth their face value, and face cards (jack, queen, king) are also worth 10. An ace's value is 11 unless this would cause the player to bust, in which case it is worth 1. A hand in which an ace's value is counted as 11 is called a soft hand, because it cannot be busted if the player draws another card.

The goal of each player is to beat the dealer by having the higher, unbusted hand. Note that if the player busts he loses, even if the dealer also busts (therefore Blackjack favors the dealer). If both the player and the dealer have the same point value, it is called a "push", and neither player nor dealer wins the hand. 

The minimum bet is printed on a sign on the table and varies from casino to casino, and even table to table. The most common minimum in the U.S. is $5 although these games can be difficult to find on the Strip in Las Vegas, especially on weekends. The Barbary Coast has $3 minimums on weekdays. After initial bets are placed, the dealer deals the cards, either from one or two hand-held decks of cards, known as a "pitch" game, or more commonly from a shoe containing four or more decks. The dealer gives two cards to each player, including himself. One of the dealer's two cards is face-up so all the players can see it, and the other is face down. (The face-down card is known as the "hole card". In European blackjack, the hole card is not actually dealt until the players all play their hands.) The cards are dealt face up from a shoe, or face down if it is a pitch game.

A two-card hand of 21 (an ace plus a ten-value card) is called a "blackjack" or a "natural", and is an automatic winner. A player with a natural is usually paid 3:2 on his bet. In 2003 some casinos started paying only 6:5 on blackjacks; although this reduced payout has generally been restricted to single-deck games where card counting would otherwise be a viable strategy, the move was decried by longtime blackjack players.
The play goes as follows:

If the dealer has blackjack and the player doesn't, the player automatically loses.
If the player has blackjack and the dealer doesn't, the player automatically wins.
If both the player and dealer have blackjack then it's a push.
If neither side has blackjack, then each player plays out his hand, one at a time.
When all the players have finished the dealer plays his hand.
The player's options for playing his or her hand are:

Hit: Take another card.
Stand: Take no more cards.
The player's turn is over after deciding to stand, doubling down to take a single card, or busting. If the player busts, he or she loses the bet even if the dealer goes on to bust.

After all the players have finished making their decisions, the dealer then reveals his or her hidden hole card and plays the hand. House rules say that the dealer must hit until he or she has at least 17, regardless of what the players have. 

If the dealer busts then all remaining players win. Bets are normally paid out at the odds of 1:1.
 SUMMARIZING THE RULES OF BETTING
 1)If you lose then you lose all of your money
 2)If you win a blackjack then you win 1.5 times the money you bet
 3)If you win normally then you win the exact amount of money you bet
 4)If you win nor lose then you don't lose any of your money""")
print("NOW SINCE YOU ARE FAMILIAR WITH THE RULES, LET'S START PLAYING!")
money=input("How much money are you betting?(in rupees)")
cards=['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
cards_positionplayer1=random.sample(cards,1)
cards_positionplayer2=random.sample(cards,1)
cards_positionplayer3=random.sample(cards,1)
cards_positioncomputer1=random.sample(cards,1)
cards_positioncomputer2=random.sample(cards,1)
cards_positioncomputer3=random.sample(cards,1)
score_computer=0
score_player=0
a=cards_positionplayer1[0]
b=cards_positionplayer2[0]
d=cards_positioncomputer1[0]
e=cards_positioncomputer2[0]

if a=='1':
    score_player+=1
if a=='2':
    score_player+=2
if a=='3':
    score_player+=3
if a=='4':
    score_player+=4
if a=='5':
    score_player+=5
if a=='6':
    score_player+=6
if a=='7':
    score_player+=7
if a=='8':
    score_player+=8
if a=='9':
    score_player+=9
if a=='10':
    score_player+=10
if a=='J':
    score_player+=10
if a=='Q':
    score_player+=10
if a=='K':
    score_player+=10
if a=='A':
    score_player+=11
if b=='1':
    score_player+=1
if b=='2':
    score_player+=2
if b=='3':
    score_player+=3
if b=='4':
    score_player+=4
if b=='5':
    score_player+=5
if b=='6':
    score_player+=6
if b=='7':
    score_player+=7
if b=='8':
    score_player+=8
if b=='9':
    score_player+=9
if b=='10':
    score_player+=10
if b=='J':
    score_player+=10
if b=='Q':
    score_player+=10
if b=='K':
    score_player+=10
if b=='A':
    score_player+=11

if d=='1':
    score_computer+=1
if d=='2':
    score_computer+=2
if d=='3':
    score_computer+=3
if d=='4':
    score_computer+=4
if d=='5':
    score_computer+=5
if d=='6':
    score_computer+=6
if d=='7':
    score_computer+=7
if d=='8':
    score_computer+=8
if d=='9':
    score_computer+=9
if d=='10':
    score_computer+=10
if d=='J':
    score_computer+=10
if d=='Q':
    score_computer+=10
if d=='K':
    score_computer+=10
if d=='A':
    score_computer+=11

print("You are given the following two cards..."+a+' and '+b)
print("Your dealer has..."+d)
if score_player==21:
    print("The dealer's hidden card is " + e)
    if e == '1':
        score_computer += 1
    if e == '2':
        score_computer += 2
    if e == '3':
        score_computer += 3
    if e == '4':
        score_computer += 4
    if e == '5':
        score_computer += 5
    if e == '6':
        score_computer += 6
    if e == '7':
        score_computer += 7
    if e == '8':
        score_computer += 8
    if e == '9':
        score_computer += 9
    if e == '10':
        score_computer += 10
    if e == 'J':
        score_computer += 10
    if e == 'Q':
        score_computer += 10
    if e == 'K':
        score_computer += 10
    if e == 'A':
        score_computer += 11

    if score_computer==21:
        print("THE DEALER GOT A BLACKJACK! YOU LOSE ALL YOUR MONEY!")
        exit()
    else:
        a1=1.5*float(money)
        print("YOU GOT A BLACKJACK! YOU WIN "+str(a1)+" rupees!")
        exit()
while 1<2:
    draw = input("Do you want to 'hit' or 'stand'? ")
    c = random.sample(cards,1)
    if draw=='hit':
        print("Your next card is "+c[0])
        #print("The dealer's hidden card is "+e)
        if c[0] == '1':
            score_player += 1
        if c[0] == '2':
            score_player += 2
        if c[0] == '3':
            score_player += 3
        if c[0] == '4':
            score_player += 4
        if c[0] == '5':
            score_player += 5
        if c[0] == '6':
            score_player += 6
        if c[0] == '7':
            score_player += 7
        if c[0] == '8':
            score_player += 8
        if c[0] == '9':
            score_player += 9
        if c[0] == '10':
            score_player += 10
        if c[0] == 'J':
            score_player += 10
        if c[0] == 'Q':
            score_player += 10
        if c[0] == 'K':
            score_player += 10
        if c[0] == 'A':
            if score_player>10:
                score_player+=1
            else:
                score_player+=11


        if score_player>21:
            print("YOUR SCORE EXCEEDED 21! YOU LOSE ALL YOUR MONEY!")
            exit()

    elif draw=='stand':
        break
print("The dealer's hidden card is " + e)
if e == '1':
    score_computer += 1
if e == '2':
    score_computer += 2
if e == '3':
    score_computer += 3
if e == '4':
    score_computer += 4
if e == '5':
    score_computer += 5
if e == '6':
    score_computer += 6
if e == '7':
    score_computer += 7
if e == '8':
    score_computer += 8
if e == '9':
    score_computer += 9
if e == '10':
    score_computer += 10
if e == 'J':
    score_computer += 10
if e == 'Q':
    score_computer += 10
if e == 'K':
    score_computer += 10
if e == 'A':
    score_computer += 11
while score_computer<17:
    f = random.sample(cards,1)
    print("The dealer's new card is " + f[0])
    if f[0] == '1':
        score_computer += 1
    if f[0] == '2':
        score_computer += 2
    if f[0] == '3':
        score_computer += 3
    if f[0] == '4':
        score_computer += 4
    if f[0] == '5':
        score_computer += 5
    if f[0] == '6':
        score_computer += 6
    if f[0] == '7':
        score_computer += 7
    if f[0] == '8':
        score_computer += 8
    if f[0] == '9':
        score_computer += 9
    if f[0] == '10':
        score_computer += 10
    if f[0] == 'J':
        score_computer += 10
    if f[0] == 'Q':
        score_computer += 10
    if f[0] == 'K':
        score_computer += 10
    if f[0] == 'A':
        if score_computer > 10:
            score_computer += 1
        else:
            score_computer += 11
    if score_computer > 21:
        print("THE DEALER'S SCORE EXCEEDED 21! YOU WIN "+money+" rupees!")
        exit()

if score_computer < score_player:
    print("YOUR SCORE IS MORE THAN THE DEALER'S SCORE! YOU WIN "+money+" rupees!")
    exit()
if score_computer > score_player:
    print("YOUR SCORE IS LESS THAN THE DEALER'S SCORE! YOU LOSE ALL YOUR MONEY!")
    exit()
if score_computer == score_player:
    print("YOUR SCORE IS EQUAL TO THE DEALER'S SCORE! NEITHER OF YOU WIN! YOU DO NOT WIN OR LOSE ANY MONEY!")
    exit()