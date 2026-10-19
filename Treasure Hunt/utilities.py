def getValidInt(prompt, min=0, max=100):
    """
    """
    while True:
        try:
            user_input = input(prompt)
            value = int(user_input)
            if min <= value <= max:
                return value
            print(f"Please enter a number between {min} and {max}.")
        except ValueError:
            print("Invalid, enter a valid integer.")

def getValidResponse(prompt, validResponses):
    """
    """
    normalized_responses = [resp.lower().strip() for resp in validResponses]
    
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in normalized_responses:
            return user_input

def getNonEmptyString(prompt):
    """
    """
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please enter something.")

def clearScreen():
    """
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(message="Press Enter to continue..."):
    """
    """
    input(message)

def printNumberedList(items):
    """
    """
    if not items:
        print("No items to display.")
    else:
        for index, item in enumerate(items, start=1):
            print(f"{index}. {item}")

def filterByLength(items, minLength, maxLength):
    """
    """
    return [item for item in items if minLength <= len(item) <= maxLength]

def analyzeNumbers(numbers):
    """
    """
    positive_numbers = [num for num in numbers if num > 0]
    positive_count = len(positive_numbers)
    negative_count = len([num for num in numbers if num < 0])
    zero_count = len([num for num in numbers if num == 0])
    
    return positive_numbers, positive_count, negative_count, zero_count