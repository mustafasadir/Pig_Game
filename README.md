# Pig_Game
How to start the game:
1. Navigate to a directory where you want to clone our repository
2. git clone https://github.com/mustafasadir/Pig_Game.git
3. Download the requirements.txt
4. To play the game make sure that you are in the Pig_Game and then in the terminal enter: python Game.py  

How to get the code coverage: 
1.	First do the following in the terminal: Pip install coverage
2.	Open up the project file and in the terminal run the following: coverage run --source=. --omit=*/testScore.py,*/testPlayer.py,*/testGame.py Game.py
3.	Play through the game (to quit enter q)
4.	Now run this line in the terminal: 	Coverage report -m   
5.	The code coverage should now be visible in the terminal

Missing part:
The part that are missing in this project is the ability to play against the computer
