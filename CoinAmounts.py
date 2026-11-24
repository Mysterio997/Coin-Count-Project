Data = open("Volunteer_Data.txt", "r")

Coin_Options = ("£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p")
Coin_Weight = ("12.00", "8.75", "8.00", "5.00", "6.50", "3.25", "7.12", "3.56")
Bag_Weight = ("120.00", "175.00", "160.00", "250.00", "325.00", "325.00", "356.00", "356.00")

Volunteer_Name = input("What is your name? ")

# Name Validation, Check Data for pre-existing logs, 

Coin_Validated = False # Defining Initial Coin Validation

while Coin_Validated == False:
    Coin = input("What coin type is the bag full of? Please add £ to the start of your input or p to the end if in pence. ").replace(" ","")
    if Coin in Coin_Options:
        Coin_Validated = True
        Weight_Calculation = False
    elif Coin not in Coin_Options:
        print("You have not put a valid coin input in, please try again.")
    else: 
        print("Stage 1: Coin Validation Error")

# Defining List Position And Required Weight

while Weight_Calculation == False:
    ListPosition = Coin_Options.index(Coin)
    Required_Weight = Bag_Weight[ListPosition]
    Required_Weight = int(float(Required_Weight))
    Weight_Calculation = True
    Weight_Validation = False

# First Weight Validation 1/2 (Checking if coins can be added or removed)
Valid_Input = False
Valid_Weight = False

while Weight_Validation == False:
    Weight = int(input("What is the weight of the bag?"))
    print(Required_Weight, ListPosition, Coin)
    Weight_Validation = True
    if Weight % 2 == 0:
        Valid_Input = True
        if Valid_Input == True and Weight < Required_Weight:
            Add_Coins = Weight - Required_Weight
            Add_Coins = Add_Coins / Coin_Weight[ListPosition]
            print(f"You must add {Add_Coins} coins to have a valid weight.")
        elif Valid_Input == True and Weight > Required_Weight:
            Remove_Coins = Weight - Required_Weight
            Remove_Coins = Remove_Coins / Coin_Weight[ListPosition]
            print(f"You must remove {Remove_Coins} coins to have a valid weight.")
        elif Weight == Required_Weight:
            Weight_Validation = True
            Valid_Weight = True
    else:
        print("Weight cannot be resolved by adding or removing coins, please check for foreign objects.")
else:
    ("Weight_Validation Error")


