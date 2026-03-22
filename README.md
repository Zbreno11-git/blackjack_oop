# blackjack_oop
Object-oriented Blackjack with betting, chips and terminal UI.

## Description
Full game: 'Card', 'Deck', 'Player'(chips,bet), 'Dealer', helpers for win/lose, and display functions.
Play until chips run out or you quit.

## Usage
python blackjack_oop.py
- Place bet, Hit or Stand, watch 'show_some'/'show_all' update.
- Chips increase/decrease via 'ganhar'/'perder'. (*portuguese)

## Key components
- **Classes**: Card, Deck, Player, Dealer.
- **Helpers**: ganhar(bet), perder(bet), show_some(), show_all(), hit_stand()
- **Loop**: Bet -> deal -> player turn -> dealer turn -> settle.

## Requirements 
- Python 3

## License
MIT
