import random

# Constants for maximum betting lines and bet limits
MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

# Slot machine dimensions
ROWS = 3
COLS = 3

# Configuration for symbols: count and payout values
symbol_count = {    
    "A" : 2,  # Symbol 'A' appears 2 times
    "B" : 4,  # Symbol 'B' appears 4 times
    "C" : 6,  # Symbol 'C' appears 6 times
    "D" : 8   # Symbol 'D' appears 8 times
}

symbol_value = {
    "A" : 5,  # Symbol 'A' pays 5x the bet
    "B" : 4,  # Symbol 'B' pays 4x the bet
    "C" : 3,  # Symbol 'C' pays 3x the bet
    "D" : 2   # Symbol 'D' pays 2x the bet
}


# Function to calculate winnings and identify winning lines
def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # Check if all symbols in the same row are identical
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            # If all symbols match, calculate winnings
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
    return winnings, winning_lines
                

# Function to simulate a slot machine spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    # columns = [[1], [2], [3]]
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            # Randomly select a symbol and remove it to avoid duplicates in a column
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns



# Function to display the slot machine in a readable format
# Transposing    
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end= " | ")
            else:
                print(col[row], end= "")
        
        print()        


# Function to get the deposit amount from the user
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("The amount must be greater then 0.")
            else:
                break
        else:
            print("Please enter a valid number.")
    
    return amount


# Function to get the number of lines to bet on
def get_lines():
    while True:
        line = input(f"Number of lines you want to bet on: (1 - {MAX_LINE})? ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINE:
                break
            else:
                print("Please enter a valid number of lines!")
        else:
            print("Please enter a valid number.")
    
    return line         


# Function to get the bet amount per line
def get_bet():
    while True:
        bet_amount = input("How much you want to bet on each line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"The bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
        
    return bet_amount
 

# Function to handle a single round of the game
def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"Insufficient Balance! Your current balance is ${balance}")
        else:
            break
        
    print(f"You are beting ${bet} on {lines} lines.")
    print(f"Your total bet is: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)

    if winnings > 0:
        print(f"You won ${winnings}!")    
        print(f"You won on lines:", *winning_lines)
    else:
        print(f"You lost ${total_bet}")
        
    return winnings - total_bet
    

# Main game loop
def main():
    balance = deposit()
    while True:
        
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with ${balance}")

# Run the game    
main()
