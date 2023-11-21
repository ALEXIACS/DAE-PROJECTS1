import webbrowser
AdultCatWetFoodList = ["Small Human-Grade Fresh Cat Food", "Tiki Cat Emma Luau Variety Pack", "Purina Pro Plan Prime Plus Adult 7+", "Made by Nacho cuts in Gravy", "Bountiful Beef Recipe Stella & Chewy's", "Instinct Raw Boost Mixers"]
adultCatDryFoodList = ["Hill's Science Diet Adult Chicken Recipe", "Open Farm Homestead Turkey & Chicken", "Orijen Original Recipe High-Protein Cat Food", "Purina Beyond: Wild-Caught Whitefish and Cage-Free Egg Recipe", "Blue Buffalo Chicken Recipe", "Made by Nacho"]
kittenFoodWet = ["Wellness Complete Health Kitten Formula", "Royal Canin Feline Ultra Soft Mousse", "Fancy Feast Tender Ocean Whitefish Feast kitten", "Backcountry Cuts Chicken", "Sheba Kitten Soft Pate", "Purina Pro-Plan kitten", "Tiny Tiger pate", "Fancy Feast Gourmet Naturals for Kittens"]
otherProductsforHealth = ["Cardboard box", "Catnip", "Cat tree", "Scratchers", "Litter Box", "Fur Brush"]
def get_user_name():
    return input("Hi! What's your name? : ")
def greet_user(user_name):
    print("Hi! " + user_name)
    print("Welcome!!")
def cat():
    return input("Do you have a cat " + get_user_name() + " ??  y/n : ").lower() == 'y'
def cat_name():
    return input("What is your cat's name? : ")
def greet_cat(name_cat):
    print(name_cat + "?? What a good name!!")
def question():
    return input(get_user_name() + " would you like to know more about cat products? y/n : ").lower() == 'y'
def question2():
    return input("Would you like to be redirected to a web page that has these products??  y/n : ").lower() == 'y'
def noanswer():
    print("Sorry, " + get_user_name() + " I don't understand your answer :c ")
def question3():
    return input("Sorry " + get_user_name() + ", this is a conversation about cats, would you like to terminate this process??  y/n : ").lower() == 'y'
def answer():
    print("Loading")
    print(". . .")
    print("...")
    print(". . .")
    print("...")
def recomendations_adultcat():
    print("I recommend you these brands and products for adult cats!! :")
    print(adultCatDryFoodList)
    print(AdultCatWetFoodList)
def recomendations_kitten():
    print("I recommend you these products!!")
    print(kittenFoodWet)
def main():
    while True:
        user_name = get_user_name()
        greet_user(user_name)
        if cat():
            name_cat = cat_name()
            greet_cat(name_cat)
            if question():
                print(AdultCatWetFoodList)
                print(adultCatDryFoodList)
                if question2():
                    url = "https://www.amazon.com/Healthy-Cat-Food/s?k=Healthy+Cat+Food"
                    webbrowser.open(url)
                else:
                    while True:
                        if question2() == 'n':
                            print("ok...")
                            answer()
                            break  
            else:
                while True:
                    if question3() == 'n':
                        question()
                    elif question3() == 'y':
                        break
                    else:
                        noanswer()
if __name__ == "__main__":
    main()