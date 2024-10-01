import random
import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init()

# Telegram channel URL
CHANNEL_URL = 'https://t.me/amir_hasan_mohamdi'

def generate_iranian_phone_number():
    # Generate a random phone number with the format 09xxxxxxxxx
    return f"09{''.join([str(random.randint(0, 9)) for _ in range(9)])}"

def get_color(index):
    # Choose color based on index
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
    return colors[index % len(colors)]

def print_sim_card():
    # Print a SIM card design with a stylish appearance
    sim_card_art = [
        Fore.YELLOW + Style.BRIGHT + """
 _____________________
|  _________________  |
| |                 | |
| |                 | |
| |    SIM CARD      | |
| |                 | |
| |_________________| |
|_____________________|
"""
        + Style.RESET_ALL,
        Fore.CYAN + Style.BRIGHT + "Generating Iranian phone numbers\n" + Style.RESET_ALL
    ]
    print("\n".join(sim_card_art))

def print_banner():
    # Print the "TOFAN" banner with a stylish appearance
    banner_art = [
        Fore.MAGENTA + Style.BRIGHT + """
 _______  _______  _______  _______  _______  _______ 
|       ||       ||       ||       ||       ||       |
|    ___||   _   ||   _   ||  _____||    ___||  _____|
|   |___ |  | |  ||  | |  || |_____ |   |___ | |_____ 
|    ___||  |_|  ||  |_|  ||_____  ||    ___||_____  |
|   |___ |       ||       | _____| ||   |___  _____| |
|_______||_______||_______||_______||_______||_______|
"""
        + Style.RESET_ALL,
        Fore.CYAN + Style.BRIGHT + f"To view the channel, please visit: {CHANNEL_URL}" + Style.RESET_ALL
    ]
    print("\n".join(banner_art))

def print_storm_message():
    # Print a "STORM" message with a stylish appearance
    storm_art = [
        Fore.RED + Style.BRIGHT + """
   _____  _______      __
  / ____||__   __|    / /
 | (___    | |      __/ / 
  \___ \   | |     / __/  
  ____) | _| |_  / /     
 |_____/ |_____|/_/      
"""
        + Style.RESET_ALL,
        Fore.CYAN + Style.BRIGHT + f"\nTo view the channel, please visit: {CHANNEL_URL}" + Style.RESET_ALL
    ]
    print("\n".join(storm_art))

def get_next_filename():
    # Find the largest existing file number and generate a new name
    base_path = 'tofan'
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    
    i = 1
    while True:
        file_path = os.path.join(base_path, f'phone_numbers_{i}.cvf')
        if not os.path.exists(file_path):
            return file_path
        i += 1

def save_numbers_to_file(numbers):
    # Save numbers to a file with a sequential name
    file_path = get_next_filename()
    with open(file_path, 'w') as file:
        file.write('\n'.join(numbers))
    print(Fore.GREEN + Style.BRIGHT + f"\nNumbers have been saved to {file_path}." + Style.RESET_ALL)

def main():
    numbers = []
    counter = 0
    print_sim_card()
    print_banner()
    try:
        while True:
            phone_number = generate_iranian_phone_number()
            color = get_color(counter // 100)  # Change color every 100 numbers
            print(color + phone_number + Style.RESET_ALL)
            numbers.append(phone_number)
            counter += 1
            time.sleep(0.1)  # Short delay to slow down number generation, you can adjust this
    except KeyboardInterrupt:
        print_storm_message()
        save_numbers_to_file(numbers)

if __name__ == '__main__':
    main()
