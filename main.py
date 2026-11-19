from play.class_interface import Game


def main():
    while True:
        val = input("\n1. New game\n2. Exit\nEnter your chice: ")
        if val == "1":
            yossi = Game()
            yossi.run()
        elif val == "2":
            break
        else:
            print("Incorrect choice, try again.")
            continue

if __name__ == "__main__":
    main()
