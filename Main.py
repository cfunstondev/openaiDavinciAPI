TOKEN_LIMIT_SAFEGUARD = 1000 # DO NOT MODIFY
RESPONSES_LIMIT_SAFEGUARD = 5 # DO NOT MODIFY

# Project Name: OpenAI Text-Completion Through Terminal
# File Name: Main.py
# Author: Codey Funston
# Created: 28-04-2023
# Updated: 29-04-2023
# Description: Entry point for project

# External libraries
import sys
import shutil

# Project libraries
import APIRequest 

# Globals
MODEL = "text-davinci-003" # IMPORTANT ($$$)
TOKEN_LIMIT = 200 # IMPORTANT ($$$)
RESPONSES_LIMIT = 1 # IMPORTANT ($$$)
TEMPERATURE = 0.7
PRICE_PER_TOKEN = 0.02 / 1000.0

def border(symbol: str) -> None:
    """
    Prints out a terminal-width length string with symbol characters
    """

    for i in range(shutil.get_terminal_size().columns):
        if i != shutil.get_terminal_size().columns:
            print(symbol, end = "")
        else:
            print(symbol)

def errorInfo(error: Exception, symbol: str) -> None:
    """
    Print's caught exception type and information
    """

    border(symbol)
    print(f"\nError: {type(error).__name__}, {error}")
    border(symbol)

def getPrompt() -> str:
    """
    Takes input from user and returns it
    """

    print("\nQUESTION")
    prompt = input()
    return prompt

if __name__ == "__main__":
    if RESPONSES_LIMIT > RESPONSES_LIMIT_SAFEGUARD and TOKEN_LIMIT > TOKEN_LIMIT_SAFEGUARD:
        sys.exit("Global variables: RESPONSES_LIMIT and TOKEN_LIMIT, exceed safeguards.")
    elif RESPONSES_LIMIT > RESPONSES_LIMIT_SAFEGUARD:
        sys.exit("Global variable: RESPONSES_LIMIT, exceeds safeguard.")
    elif TOKEN_LIMIT > TOKEN_LIMIT_SAFEGUARD:
        sys.exit("Global variable: TOKEN_LIMIT, exceeds safeguard.")

    question = getPrompt()
    request_test = APIRequest.APIRequest(MODEL, question, TOKEN_LIMIT, TEMPERATURE, RESPONSES_LIMIT)

    try:
        answer = request_test.make_request()
        print("\nANSWER")
        print(answer, "\n")

        price = request_test.total_tokens * PRICE_PER_TOKEN
        formatted_price = format(price, ",.6f")
        print("PRICE")
        print(f"${formatted_price}", "\n")

    except Exception as e:
        errorInfo(e, "#")
    except openai.error.AuthenticationError as e:
        errorInfo(e, "#")
    except openai.error.RateLimitError as e:
        errorInfo(e, "#")
