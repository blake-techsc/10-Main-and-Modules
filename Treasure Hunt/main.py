import random
import time
import utilities

locations = ["Dark Cave", "Sandy Beach", "Ancient Ruins"]
difficultyOpiton = ["Easy", "Medium", "Hard"]

difficultySettings = {
    1: {"name": "Easy", "treasure": 10, "trap": -5},
    2: {"name": "Medium", "treasure": 20, "trap": -10},
    3: {"name": "Hard", "treasure": 30, "trap": -20}
}

def displayWelcome():
    """
    Display welcome screen and get player name
    """
    utilities.clearScreen()
    playerName = utilities.getNonEmptyString("Enter your name: ")
    print(f"Welcome to the adventure, {playerName}!")
    utilities.pause()
    
    return playerName

def selectDifficulty():
    """
    Selects the diffuculty settings and choice
    """
    utilities.printNumberedList(difficultyOpiton)
    choice = utilities.getValidInt("Select difficulty (1-3): ", 1, 3)
    return difficultySettings[choice]

def playRound(roundNumber, difficultySettings):
    """
    Shows locations and round number
    """
    utilities.clearScreen()
    print(f"Round {roundNumber} of 5")
    print()
    utilities.printNumberedList(locations)
    print()

    locationChoice = utilities.getValidInt("Enter your choice (1-3): ", 1, 3)
    selectedLocation = locations[locationChoice - 1]
    outcome = random.randint(0, 2)
    
    if outcome == 0:
        points = difficultySettings["treasure"]
        message = f"You found treasure! (score +{points})"
    elif outcome == 1:
        points = difficultySettings["trap"]
        message = f"It was a trap! (score {points})"
    else:
        points = 0
        message = "You found nothing! (score 0)"
    
    print(f"\nYou dig at the {selectedLocation}...")
    print(message)
    
    return points

def displayReport(playerName, roundScores):
    """
    Shows explorer name, round info, and final score
    """
    print()
    print("TREASURE REPORT")
    print()
    print(f"Explorer: {playerName}")
    
    for i, score in enumerate(roundScores, start=1):
        sign = "+" if score >= 0 else ""
        print(f"Round {i}: {sign}{score}")
    
    positives, posCount, negCount, zeroCount = utilities.analyzeNumbers(roundScores)
    
    print(f"\nTreasure Rounds: {posCount} | Trap Rounds: {abs(negCount)} | Empty Rounds: {zeroCount}")
    
    totalScore = sum(roundScores)
    print(f"Total Score: {totalScore}")
    
def playGame(playerName):
    """
    Selects diffuculty, asks for user inputs, and starts the game
    """
    roundScores = []
    difficultySettings = selectDifficulty()
    
    for roundNum in range(1, 6):
        points = playRound(roundNum, difficultySettings)
        roundScores.append(points)
        
        currentTotal = sum(roundScores)
        time.sleep(3)
        utilities.clearScreen()
        print(f"Current Total Score: {currentTotal}")
        utilities.pause()
    
    displayReport(playerName, roundScores)
    
    playAgain = utilities.getValidResponse("Play again? (Y/N): ", ["Y", "N"])
    return playAgain == "y"

def main():
    playerName = displayWelcome()
    
    playing = True
    while playing:
        playing = playGame(playerName)
        if playing:
            print("\nStarting a new adventure!\n")
            utilities.pause("Press Enter to begin...")
    
    utilities.clearScreen()
    print("Goodbye!")

if __name__ == "__main__":
    main()