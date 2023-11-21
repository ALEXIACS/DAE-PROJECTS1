AdultCatWetFoodList = ["Small Human-Grade Fresh Cat Food", "Tiki Cat Emma Luau Variety Pack", "Purina Pro Plan Prime Plus Adult 7+", "Made by Nacho cuts in Gravy", "Bontiful Beef Recipe Stella & Chewy's", "Instinct Raw Boost Mixers"]
adultCatDryFoodList = ["Hill's Science Diet Adult Chicken Recipe", "Open Farm Homestead Turkey & Chicken", "Orijen Original Recipe High-Protein Cat Food", "Purina Beyond: Wild-Caught Whitefish and Cage-Free Egg Recipe", "Blue Buffalo Chicken Recipe", "Made by Nacho"]
kittenFoodWet = ["Wellness Complete Health Kitten Formula", "Royal Canin Feline Ultra Soft Mousse", "Fancy Feast Tender Ocean Whitefish Feast kitten", "Backcountry Cuts Chicken", "Sheba Kitten Soft Pate", "Purina Pro-Plan kitten", "Tiny Tiger pate", "Fancy Feast Gourmet Naturals for Kittens"]
otherProductsforHealth = ["Cardboard box", "Catnip", "Cat tree", "Scratchers", "Litter Box", "Fur Brush"]
import webbrowser
while True:
    def get_user_name():
        return input("Hi! What's your name? : ")
    def greet_user(user_name):
        print("Hi! " + user_name)
        print("Welcome!!")
    def cat():
        return input( "Do you have a cat " + get_user_name() + " ??  y/n : " ) .lower() == 'y'
    def cat_name():
        return input("What is your cat's name? : ")
    def greet_cat(cat1):
        return print( cat1 + "?? what a good name!!")
    def  want_cat():
        return input( get_user_name() + "Are you planning on having a cat??  y/n : ") .lower()
    def question():
        return input( get_user_name() + " would you like to know more about cat products? y/n : ") .lower()
    def question2():
        return input("Would you like to be redirected to a web page that has this products??  y/n : ") .lower() == 'y'
    def noanswer():
        print("Sorry, " + get_user_name() + " I dont undertand your answer :c ")
    def question3():
        return input( "Sorry " + get_user_name() + ", this is a conversation about cats, would you like to terminate this process??  y/n : ")
    def recomendations_adultcat():
        print("I recomend you this brand's and products for adult cats!! :")
        print(adultCatDryFoodList)
        print(AdultCatWetFoodList)
    def recomendations_kitten():
        print("I recomend you this products!!")
        print(kittenFoodWet)
    def answer():
        print("Loading")
        print(". . .")
        print("...")
        print(". . .")
        print("...")
    def main():
           def main():
                user_name = get_user_name()
                greet_user(user_name)
                if cat():
                    name_cat = cat_name()
                    greet_cat(name_cat)
                    if question() == 'y':
                        question2()
                        if question2() == 'y':
                            url = "https://www.amazon.com/Healthy-Cat-Food/s?k=Healthy+Cat+Food"
                            webbrowser.open(url)
                        if question2() == 'n':
                            while True:
                                if question2() == 'n':
                                    print("ok...")
                                    answer()
                                else:
                                    noanswer()
                                break
                        else:
                            while True:
                                noanswer()
                                break
                            print(" This chat will close...")
                    else:
                        while True:
                            if question3() == 'n':
                                question()
                            elif question3() == 'y':
                                break
                            else:
                                noanswer()
                            break
                        break
    if __name__ == "__main__":
        main()