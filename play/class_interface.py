from .class_data import DataCards

class Game:
    def __init__(self):
        self.game = DataCards()

    def run(self):

        self.game.shuffling()
        print("\n==== The game begins ====")
        while True:
            val = input("• 1. Play turn\n• 2. Exit\nEnter choice: ")
            if val == "1":
                card_of_player, card_of_computer = self.game.brings_tow_cards()
                if card_of_player == 0:
                    print("\nGame Over, Computer is the Winner\n")
                    break
                elif card_of_computer == 0:
                    print("\nGame Over, Player is the Winner\n")
                    break
                else:                
                    
                    num_card_p, name_card_p = card_of_player
                    num_card_c, name_card_c = card_of_computer

                    if num_card_p > num_card_c:
                        self.game.results_update(card_of_player, card_of_computer, "player")
                        len_player, len_computer = self.game.return_len_lists()
                        print("\n================ TURN ================")
                        print(f"Player: {name_card_p}")
                        print(f"Computer: {name_card_c}")
                        print("Player won the round!")
                        print(f"Player cards: {len_player} | Computer cards: {len_computer}")
                        print("======================================\n")
                        continue

                    elif num_card_c > num_card_p:
                        self.game.results_update(card_of_player, card_of_computer, "computer")
                        len_player, len_computer = self.game.return_len_lists()
                        print("\n================ TURN ================")
                        print(f"Player: {name_card_p}")
                        print(f"Computer: {name_card_c}")
                        print("Computer won the round!")
                        print(f"Player cards: {len_player} | Computer cards: {len_computer}")
                        print("======================================\n")
                        continue
                        
                    else:
                        self.game.results_update(card_of_player, card_of_computer, "None") 
                        len_player, len_computer = self.game.return_len_lists()
                        print("\n================ TURN ================")
                        print(f"Player: {name_card_p}")
                        print(f"Computer: {name_card_c}")
                        print("It's a draw!")
                        print(f"Player cards: {len_player} | Computer cards: {len_computer}")
                        print("======================================\n")
                        continue

            elif val == "2":
                print("\nThe game stopped in the middle.\n")
                break
            else:
                print("Incorrect choice, try again.")
                continue
        
