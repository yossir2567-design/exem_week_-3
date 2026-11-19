import random


class Cards:
    def __init__(self):
        self.h = [(1,"2 h"),(2,"3 h"),(3,"4 h"),(4,"5 h"),(5,"6 h"),(6,"7 h"),(7,"8 h"),(8,"9 h"),(9,"10 h"),(10,"prins h"),(11,"queen h"),(12,"king h"),(13, "A h")]
        self.d = [(1,"2 d"),(2,"3 d"),(3,"4 d"),(4,"5 d"),(5,"6 d"),(6,"7 d"),(7,"8 d"),(8,"9 d"),(9,"10 d"),(10,"prins d"),(11,"queen d"),(12,"king d"),(13, "A d")]
        self.s = [(1,"2 s"),(2,"3 s"),(3,"4 s"),(4,"5 s"),(5,"6 s"),(6,"7 s"),(7,"8 s"),(8,"9 s"),(9,"10 s"),(10,"prins s"),(11,"queen s"),(12,"king s"),(13, "A s")]
        self.c = [(1,"2 c"),(2,"3 c"),(3,"4 c"),(4,"5 c"),(5,"6 c"),(6,"7 c"),(7,"8 c"),(8,"9 c"),(9,"10 c"),(10,"princ c"),(11,"queen c"),(12,"king c"),(13, "A c")]
        self.list_player = []
        self.list_computer = []
        self.main_list = self.h + self.d + self.s + self.c
        self.main_list.append((14, "Joker Red"))
        self.main_list.append((14, "Joker Black"))


    def shuffling_cards(self):
        self.list_player = []
        self.list_computer = []
        for i in range(1000):
            random_index = random.randrange(len(self.main_list))
            val = self.main_list.pop(random_index)
            self.main_list.insert(0, val)
        list_player = []
        for card in self.main_list:
            if len(list_player) == len(self.main_list):
                break 
            list_player.append(card)
            self.main_list.remove(card)
        list_computer = self.main_list
        self.updating_lists(list_player, list_computer)

    def dealing_cards_player(self):
        return self.list_player
    def dealing_cards_computer(self):
        return self.list_computer


    def updating_lists(self, list_of_player, list_of_computer):
        self.list_player = list_of_player
        self.list_computer = list_of_computer


