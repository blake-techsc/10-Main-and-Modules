def getValidInt(prompt, min=0, max=100):
    """
    Checks to see if the integer is valid, and rehects it if it isn't
    """
    while True:
        try:
            userInput = input(prompt)
            value = int(userInput)
            if min <= value <= max:
                return value
            print(f"Please enter a number between {min} and {max}.")
        except ValueError:
            print("Invalid, enter a valid integer.")

def getValidResponse(prompt, validResponses):
    """
    Checks to see if the response is valid
    """
    normalizedResponses = [resp.lower().strip() for resp in validResponses]
    
    while True:
        userInput = input(prompt).lower().strip()
        if userInput in normalizedResponses:
            return userInput

def getNonEmptyString(prompt):
    """
    Makes sure the input isn't empty
    """
    while True:
        userInput = input(prompt).strip()
        if userInput:
            return userInput
        print("Input cannot be empty. Please enter something.")

def clearScreen():
    """
    Clears the Windows terminal
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(message="Press Enter to continue..."):
    """
    A pause between events
    """
    input(message)

def printNumberedList(items):
    """
    Prints list of itmes
    """
    if not items:
        print("No items to display.")
    else:
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item}")

def filterByLength(items, minLength, maxLength):
    """
    Filters items by their length
    """
    return [item for item in items if minLength <= len(item) <= maxLength]

def analyzeNumbers(numbers):
    """
    Checks to see if the numbers are positive, negative, or zero
    """
    positiveNumbers = [num for num in numbers if num > 0]
    positiveCount = len(positiveNumbers)
    negativeCount = len([num for num in numbers if num < 0])
    zeroCount = len([num for num in numbers if num == 0])
    
    return positiveNumbers, positiveCount, negativeCount, zeroCount