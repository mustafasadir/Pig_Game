# Pig_Game

How to get the code coverage: 
1.	First do the following in the terminal: Pip install coverage
2.	Open up the project file and in the terminal run the following: coverage run --source=. --omit=*/testScore.py,*/testPlayer.py,*/testGame.py Game.py
3.	Play through the game (to quit enter q)
4.	Now run this line in the terminal: 	Coverage report -m   
5.	The code coverage should now be visible in the terminal
