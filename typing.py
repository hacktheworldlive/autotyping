import pyautogui
import time
import random

# Function to read text from a file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to simulate human-like typing
def auto_type_text(text):
    for line in text.splitlines():
        for char in line:
            pyautogui.typewrite(char)
            time.sleep(random.uniform(0.1, 0.2))  # Random delay between keystrokes
        pyautogui.press('enter')
        time.sleep(random.uniform(0.5, 1.5))  # Random delay between lines

# Main function
def main():
    # Delay to switch to the target application (e.g., Visual Studio Code)
    print("Switch to the target window in 10 seconds...")
    time.sleep(10)  # Increased time to switch to Visual Studio Code

    # Path to the text file
    file_path = 'text.txt'

    # Read the text from the file
    text = read_text_file(file_path)

    # Type the text into the active window with human-like typing
    auto_type_text(text)

if __name__ == "__main__":
    main()
