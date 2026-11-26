class bcolors:
    OKGREEN = '\033[92m'
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

Data = open("Volunteer_Data.txt", "r")

Coin_Options = ("£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p")
Coin_Weight = ("12.00", "8.75", "8.00", "5.00", "6.50", "3.25", "7.12", "3.56")
Bag_Weight = ("120.00", "175.00", "160.00", "250.00", "325.00", "325.00", "356.00", "356.00")

Volunteer_Name = input(bcolors.OKBLUE + "What is your name? " + bcolors.ENDC).replace(" ","")

# Name Validation, Check Data for pre-existing logs, 

Coin_Validated = False 

while Coin_Validated == False:
    Coin = input(bcolors.OKBLUE + "What coin type is the bag full of? Please add £ to the start of your input or p to the end if in pence. " + bcolors.ENDC).replace(" ","")
    if Coin in Coin_Options:
        Coin_Validated = True
        Weight_Calculation = False
    elif Coin not in Coin_Options:
        print(bcolors.WARNING + "You have not put a valid coin input in, please try again." + bcolors.ENDC)
    else: 
        print(bcolors.WARNING + "Stage 1: Coin Validation Error" + bcolors.ENDC)

while Weight_Calculation == False:
    ListPosition = Coin_Options.index(Coin)
    Required_Weight = Bag_Weight[ListPosition]
    Required_Weight = int(float(Required_Weight))
    Weight_Calculation = True
    Weight_Validation = False

Valid_Input = False
Valid_Weight = False

Weight = None

while Weight_Validation == False:
    try:
        Weight = int(input(bcolors.OKBLUE + "What is the weight of the bag?" + bcolors.ENDC))
    except ValueError:
        print(bcolors.WARNING + "You must input a proper weight, please try again." + bcolors.ENDC)
        Weight_Validation = False
    if Weight == None:
        print(bcolors.WARNING + "Invalid Weight Input, please try again." + bcolors.ENDC)
        Weight_Validation = False
    elif Weight < 0:
        print(bcolors.WARNING + f"Total weight must be at least {Coin_Weight[ListPosition]} for a bag of {Coin_Options[ListPosition]} coins. You have inputted a negative, please try again." + bcolors.ENDC)
        Weight_Validation = False
    elif Weight % float(Coin_Weight[ListPosition]) == 0:
        Valid_Input = True
        if Valid_Input == True and Weight < Required_Weight:
            Add_Coins = Required_Weight - Weight
            Add_Coins = Add_Coins / float(Coin_Weight[ListPosition])
            Add_Coins = int(Add_Coins)
            print(bcolors.OKGREEN + f"You must add {Add_Coins} {Coin_Options[ListPosition]} coins to have a valid weight." + bcolors.ENDC)
            Weight_Validation = True
        elif Valid_Input == True and Weight > Required_Weight:
            Remove_Coins = Weight - Required_Weight
            Remove_Coins = Remove_Coins / float(Coin_Weight[ListPosition])
            Remove_Coins = int(Remove_Coins)
            print(bcolors.OKGREEN + f"You must remove {Remove_Coins} {Coin_Options[ListPosition]} coins to have a valid weight." + bcolors.ENDC)
            Weight_Validation = True
        elif Weight == Required_Weight:
            print(bcolors.OKGREEN + f"The bag is the correct weight, thanks {Volunteer_Name}" + bcolors.ENDC)
            Weight_Validation = True
            Valid_Weight = True
    else:
        print(bcolors.WARNING + "Weight cannot be resolved by adding or removing coins, please check for foreign objects." + bcolors.ENDC)
else:
    (bcolors.WARNING + "Weight_Validation Error" + bcolors.ENDC)

# Name Validation and updating
# List of total bags checked and total value, option to see it.
# List of volunteers, bags counted and overall accuracy.