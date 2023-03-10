from random import randint
from Score import Score
from Player import Player
from Difficulty import Difficulty
from GameState import GameState


class Game:
    def __init__(self):
        self.difficulty = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]
        self.game_state = GameState()

    def quit_game(self):
        '''
        for quitting the game
        '''
        exit()

    def reset_game(self):
        '''
        Resets the score for the players. Turns off cheat mode
        '''

        for player in self.game_state.score_list:
            player.score.reset_score_object()
        self.game_state.is_cheat_mode = False

    def set_cheat_mode(self):
        '''
        Turns on cheat mode. The player can choose what value the dies should have
        '''
        self.game_state.is_cheat_mode = True
        dice1 = int(input("Enter the desired value for dice 1: "))
        dice2 = int(input("Enter the desired value for dice 2: "))
        return dice1, dice2

    def set_difficulty(self, game_state):
        # implementation for setting the game difficulty based on the game state
        #  should return an ENUM value representing
        game_state.difficulty = difficulty

    def print_score(self):
        '''
        Prints the high score at the end of the game
        '''
        print("High Score:")
        for player, score in self.game_state.score_list.items():
            print(f"{player._get_name()}: {score.get_current_score()}")

    def throw_dice(self):
        '''
        for loop 1 to 6 that returns int
        '''
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        return dice1, dice2

    def play_game(self):
        '''
        The game function. This is our "main" and it is here the player plays the game
        '''
        print("\nWelcome to Pig Game!\n\nThe instructions of the game are simple,you will take turns rolling two six-sided dies. ")
        print("If you roll a 1, your turn ends and you lose all your points.")
        print("If you roll a 2-6, you can choose to roll again or hold your score.")
        print("The first player to reach 100 points wins the game.\n")
        num_players = int(input("How many players are you? "))
        players = []  # Creates list of players
        for i in range(num_players):
            player_name = input(f"Enter name for player {i+1}: ")
            players.append(Player(player_name))

        current_player_index = 0
        while True:
            print(f"\n\n{players[current_player_index]._get_name()}'s turn!")
            print("Current Score:", players[current_player_index].score.get_current_score())
            print("To activate cheat enter C \nTo quit the game enter Q\nTo switch name enter S")
            choice = input("Do you want to roll the dices? (y/n)").lower()
            if choice == "c":
                dice1, dice2 = self.set_cheat_mode()
                points = dice1 + dice2
                players[current_player_index].score.set_current_score(points)

            elif choice == "q":
                self.quit_game()

            elif choice == "s":
                new_name = input("What do you want to switch your name to? ")
                players[current_player_index].change_name(new_name)
                print(f"Name changed to {players[current_player_index]._get_name()}")

            elif choice == "y":
                dice1, dice2 = self.throw_dice()
                print(f"You rolled {dice1} and {dice2}.")

                if dice1 == 1 or dice2 == 1:
                    print("You rolled a 1! Turn is over, no points earned.")
                    players[current_player_index].score.reset_score_object()
                    current_player_index = (current_player_index + 1) % len(players)  # Switches over to the other player

                else:
                    points = dice1 + dice2
                    players[current_player_index].score.set_current_score(points)
                    print(f"You earned {points} points this turn!")

                    if players[current_player_index].score.get_current_score() + self.game_state.score_list.get(players[current_player_index], Score()).get_current_score() >= 100:
                        print(f"\n{players[current_player_index]._get_name()} won the game!")
                        players[current_player_index].score.set_current_score(points) # Add the final points earned in the last round to the score
                        self.game_state.score_list[players[current_player_index]] = players[current_player_index].score # Update the high score list
                        self.print_score()
                        for player in players:
                            players[current_player_index].score.reset_score_object()    # Resets the score after the game

            else:
                print("Turn is over, no points earned.")
                current_player_index = (current_player_index + 1) % len(players)


if __name__ == "__main__":
    game = Game()
    game.play_game()