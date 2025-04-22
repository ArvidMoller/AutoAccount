# Move out of folder to test

import os
import glob

def choose_dataset():
    user_input = input("Load which dataset (.csv)? \n")
    os.chdir(f"{os.getcwd()}/dataset")
    acceptedInput = glob.glob("*.csv")
    
    while not user_input in acceptedInput:
        user_input = input("Load which dataset? \n")

    return f"dataset/{user_input}"

print(choose_dataset())