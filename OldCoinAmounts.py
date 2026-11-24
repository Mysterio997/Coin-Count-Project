Coins =   ("£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p")
Weight = ("12.00", "8.75", "8.00", "5.00", "6.50", "3.25", "7.12", "3.56")
BagWeight = ("120", "175", "160", "250", "325", "325", "356", "356")

VolunteerName = input("What is your name? ")

CoinValidated = False

while CoinValidated == False:
    CoinType = input("What coin type is the bag full of? Please add £ to the start of your input or p to the end if in pence. ").replace(" ","")
    if ("£") not in CoinType and CoinType not in Coins or ("p") not in CoinType and CoinType not in Coins:
        print("You have not put a valid coin input in, please try again.")
    elif CoinType in Coins:
        CoinValidated = True
        print(CoinType)
    else: 
        print("Coin Type Validation Error, Lines 11 - 19")

RequiredWeightCalculation = False

while CoinValidated == True and RequiredWeightCalculation == False:
    ListPosition = Coins.index(CoinType)
    RequiredWeight = BagWeight[ListPosition]
    RequiredWeightCalculation = True
    RequiredWeight = int(float(RequiredWeight))
    print(RequiredWeight)

ValidWeight = False

# Fix weight validation to ensure if weight is either over or under that it is possible to resolve with more or less coins (Check for foreign objects)
while ValidWeight == False:
    Weight = int(input("What is the weight of the bag?"))
    Weight[ListPosition] = int(Weight[ListPosition])
    if Weight == RequiredWeight:
        ValidWeight = True
        print(f"The bag is the correct weight, thanks {VolunteerName}")
    elif Weight > RequiredWeight:
        CoinsToBeRemoved = RequiredWeight - Weight
        CoinsToBeRemoved = CoinsToBeRemoved / Weight[ListPosition]
        print(f"You must remove {CoinsToBeRemoved}, {Coins[ListPosition]} coins in order to have the correct bag weight.")
    elif Weight < RequiredWeight:
        CoinsToBeAdded = Weight - RequiredWeight
        CoinsToBeAdded = CoinsToBeAdded / Weight[ListPosition]
        print(f"You must add {CoinsToBeAdded}, {Coins[ListPosition]} coins in order to have the correct bag weight.")
    else: 
        print("Valid Weight Error Validation")


