שלום יוסף רבינוביץ 211474432


Program Structure:

The main.py file determines whether to start a new game. ->
.
.
The interface.py file manages the game and calls the DataCards class from class_data.py. ->
.
.
The class_data.py file receives commands and provides values ​​upon request (it retrieves the Cards class from class_cards.py). ->
.
.
The class_cards.py file constructs the cards, shuffles them, and creates two lists.

main ->
interface -> data -> cards
cards -> data -> interface