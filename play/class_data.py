from .class_cadrs import Cards


class DataCards():
    def __init__(self):
        self.data = Cards()


    def shuffling(self):
        self.data.shuffling_cards()

    def brings_tow_cards(self):
        list_of_player = self.data.dealing_cards_player()
        list_of_computer = self.data.dealing_cards_computer()
        if len(list_of_player) == 0:
            return 0, 1
        elif len(list_of_computer) == 0:
            return 1, 0
        card_of_player = list_of_player.pop()
        card_of_computer = list_of_computer.pop()

        self.data.updating_lists(list_of_player, list_of_computer)

        return card_of_player, card_of_computer
        

    def results_update(self, card1, card2, win):
        list_of_player = self.data.dealing_cards_player()
        list_of_computer = self.data.dealing_cards_computer()
        if win == "player":
            list_of_player.insert(0 , card1)
            list_of_player.insert(0, card2)
        elif win == "computer":
            list_of_computer.insert(0, card1)
            list_of_computer.insert(0, card2)
        else:
            list_of_player.insert(0, card1)
            list_of_computer.insert(0, card2)

        self.data.updating_lists(list_of_player, list_of_computer)

    def return_len_lists(self):
        list_of_player = self.data.dealing_cards_player()
        list_of_computer = self.data.dealing_cards_computer()
        return len(list_of_player), len(list_of_computer)



    

