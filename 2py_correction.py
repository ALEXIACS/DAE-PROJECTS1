import webbrowser
AdultCatWetFoodList = ["Small Human-Grade Fresh Cat Food", "Tiki Cat Emma Luau Variety Pack", "Purina Pro Plan Prime Plus Adult 7+", "Made by Nacho cuts in Gravy", "Bountiful Beef Recipe Stella & Chewy's", "Instinct Raw Boost Mixers"]
adultCatDryFoodList = ["Hill's Science Diet Adult Chicken Recipe", "Open Farm Homestead Turkey & Chicken", "Orijen Original Recipe High-Protein Cat Food", "Purina Beyond: Wild-Caught Whitefish and Cage-Free Egg Recipe", "Blue Buffalo Chicken Recipe", "Made by Nacho"]
kittenFoodWet = ["Wellness Complete Health Kitten Formula", "Royal Canin Feline Ultra Soft Mousse", "Fancy Feast Tender Ocean Whitefish Feast kitten", "Backcountry Cuts Chicken", "Sheba Kitten Soft Pate", "Purina Pro-Plan kitten", "Tiny Tiger pate", "Fancy Feast Gourmet Naturals for Kittens"]
otherProductsforHealth = ["Cardboard box", "Catnip", "Cat tree", "Scratchers", "Litter Box", "Fur Brush"]

#function to get name
def get_user_name():
    return input("Hi! What's your name? : ")

#function to greet user
def greet_user(user_name):
    print("Hi! " + user_name)
    print("Welcome!!")

#question the user if it has a cat
def cat(user_name):
    return input("Do you have a cat " + user_name + " ??  y/n : ").lower()

#get cat name
def cat_name(user_name):
    return input( user_name + " what is your cat's name? : ")

#make compliment to the cat
def greet_cat(name_cat):
    print(name_cat + "?? What a good name!!")

#get to know cat products
def question(user_name):
    return input(user_name + " would you like to know more about cat products? y/n : ").lower()

#web page redirection
def question2():
    return input("Would you like to be redirected to a web page that has these products??  y/n : ").lower()

#if the answer is not understandable
def noanswer(user_name):
    print("Sorry, " + user_name + " I don't understand your answer :c ")

#terminate process
def terminate(user_name):
    return input( user_name + " would you like to end this process??  y/n  :"). lower()

#end process question
def question3(user_name):
    return input("Sorry " + user_name + ", this is a conversation about cats, would you like to terminate this process??  y/n : ").lower()

#finished code
def no_updated(user_name):
    print("Sorry " + user_name + " this function hasn't beeen developed yet!!")

#loading 'bar'
def answer():
    print("Loading")
    print(". . .")
    print("...")
    print(". . .")
    print("...")

#adult cat food recomendation
def recomendations_adultcat():
    print("I recommend you these brands and products for adult cats!! :")
    print(adultCatDryFoodList)
    print(AdultCatWetFoodList)

#kitten food recomendation
def recomendations_kitten():
    print("I recommend you these products!!")
    print(kittenFoodWet)

# START
def main():
    while True:
        user_name = get_user_name()
        greet_user(user_name)
#Asking if the user has a cat
        if cat(user_name) == 'y':
#get cat name
            cat_name(user_name)
            name_cat = cat_name(user_name)
            greet_cat(name_cat)
#Asking if the user wants to know more about cat food
            if question(user_name) == 'y':
                print(AdultCatWetFoodList)
                print(adultCatDryFoodList)
                if question2(user_name) == 'y':
                    answer()
                    url = "https://www.amazon.com/Healthy-Cat-Food/s?k=Healthy+Cat+Food"
                    url1 = "https://www.amazon.com/Healthy-Kitten-Food/s?k=Healthy+Kitten+Food"
                    webbrowser.open (url1)
                    webbrowser.open(url)
                    break
                else:
                    answer()
                    noanswer(user_name)
                    terminate()
                    if terminate() == 'y':
                        answer()
                        break
                    if terminate() == 'n': 
                        no_updated()
                        answer()
                        break
                    else:
                        noanswer(user_name)
                        answer()
                        terminate()
                        if terminate() == 'y':
                            answer()
                            break
                        else:
                            answer()
                            no_updated(user_name)
                            answer()
                            break
            else:
                while True:
                    if question2() == 'n':
                        print("ok...")
                        answer()
                        break  
        if cat(user_name) == 'n':
            question3(user_name)
            if question3(user_name) == 'y':
                break
            if question3(user_name) == 'n':
                no_updated(user_name)
                answer()
                break
if __name__ == "__main__":
    main()