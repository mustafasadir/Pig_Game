from enum import Enum
from random import randint
from Score import Score
from Player import Player
from Difficulty import Difficulty
from GameState import GameState




class Game:
    def __init__(self):
        self.difficulty = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]
        self.game_state = GameState()
        
    def quitGame(self):
        # implementation for quitting the game
        exit()

    def resetGame(self):
        for player in self.game_state.highScoreList:
            player.score.resetScoreObject()

        self.game_state.isCheatMode = False

    def setCheatMode(self):
        self.game_state.isCheatMode = True
        dice1 = int(input("Enter the desired value for dice 1: "))
        dice2 = int(input("Enter the desired value for dice 2: "))
        return dice1, dice2

    def setDifficulty(self, game_state):
        # implementation for setting the game difficulty based on the game state
        #  should return an ENUM value representing
        game_state.difficulty = difficulty
        

    def printScore(self):
        print("High Score:")
        for player, score in self.game_state.highScoreList.items():
            print(f"{player._getName()}: {score.getCurrentScore()}")
            
        

    def throwDice(self):
        # for loop 1 to 6 that returns int
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        return dice1, dice2
    
    def playGame(self):
        print("Welcome to Pig Game!\n\nThe instructions of the game are simple, blab blab bla\n")
        num_players = int(input("How many players? "))
        players = []
        for i in range(num_players):
            player_name = input(f"Enter name for player {i+1}: ")
            players.append(Player(player_name))
        
        current_player_index = 0
        while True:
            print(f"\n\n{players[current_player_index]._getName()}'s turn!")
            print("Current Score:", players[current_player_index].score.getCurrentScore())
            print("To active cheat enter C \nTo quit the game enter Q")
            choice = input("Do you want to roll the dice? (y/n)").lower()
            if choice == "c":
                dice1, dice2 = self.setCheatMode()
                points = dice1 + dice2
                players[current_player_index].score.setCurrentScore(points)
                
            elif choice == "q":
                self.quitGame()
            elif choice == "y":
                dice1, dice2 = self.throwDice()
                print(f"You rolled {dice1} and {dice2}.")


                if dice1 == 1 or dice2 == 1:
                    print("You rolled a 1! Turn is over, no points earned.")
                    players[current_player_index].score.resetScoreObject()
                    current_player_index = (current_player_index + 1) % len(players)  # Switches over to the other player
                    

                else:
                    points = dice1 + dice2
                    players[current_player_index].score.setCurrentScore(points)
                    print(f"You earned {points} points this turn!")

                    if players[current_player_index].score.getCurrentScore() + self.game_state.highScoreList.get(players[current_player_index], Score()).getCurrentScore() >= 100:
                        print(f"{players[current_player_index]._getName()} won the game!")
                        players[current_player_index].score.setCurrentScore(points) # Add the final points earned in the last round to the score
                        self.game_state.highScoreList[players[current_player_index]] = players[current_player_index].score # Update the high score list
                        self.printScore()
                        #No break statement, the game will keep running until the player manually quits

            else:
                print("Turn is over, no points earned.")
                current_player_index = (current_player_index + 1) % len(players)
            
        
if __name__ == "__main__":
    game = Game()
    game.playGame()
        
        
        