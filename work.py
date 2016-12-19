from datetime import datetime
from collections import namedtuple

def main():
    options = ['a', 'b']
    displayOptions = ['Add RD file(s)', 'Print list of RD files']
    for index in range (0, 2):
        print(str(options[index])+') '+displayOptions[index])
    done1 = True
    while done1:
        try:
            done1 = False
            userChoice = input(str('Please choose (a or b) to enter\n'))
            if not userChoice:
                raise ValueError('Empty command. Enter again\n')
                done1 = True
            elif userChoice not in options:
                raise ValueError('Please choose only a or b. Enter again\n')
                done1 = True
        except ValueError as e:
            print(e)

        
