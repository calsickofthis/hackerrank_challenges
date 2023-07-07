import re

def validate(UID):
    #more thatn two uppercase letters
    if len(re.findall(r'[A-Z]',UID)) > 2:
        #contains at least 3 digits
        if len(re.findall(r'[0-9]',UID)) >= 3:
            #checks if string is alphanumeric
            if UID.isalnum():

                #check if any characters repeated
                for char in UID:
                    # if char.isalpha():
                    if UID.count(char) > 1:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False

'''answer for UID checker'''
if __name__ == "__main__":

    T = int(input())

    for i in range(0,T):
        UID = input()
        if validate(UID) == False:
            print('Invalid')
        else:
            print('Valid')
