AdultCatWetFoodList = ["Small Human-Grade Fresh Cat Food", "Tiki Cat Emma Luau Variety Pack","Purina Pro Plan Prime Plus Adult 7+","Made by Nacho cuts in Gravy","Bontiful Beef Recipe Stella & Chewy's","Instinct Raw Boost Mixers"]
adultCatDryFoodList = ["Hill's Science Diet Adult Chicken Recipe", "Open Farm Homestead Turkey & Chicken", "Orijen Original Recipe High-Protein Cat Food", "Purina Beyond: Wild-Caugh Whitefish and Cage-Free Egg Recipe", "Blue Buffalo Chicken Recipe", "Made by Nacho"]
kittenFoodWet = ["Wellness Complete Health Kitten Formula", "Royal Canin Feline Ultra Soft Mousse", "Fancy Feast Tender Ocean Whitefish Feast kitten", "Backcountry Cuts Chicken", "Sheba Kitten Soft Pate", "Purina Pro-Plan kitten", "Tiny Tiger pate", "Fancy Feast Gourmet Naturals for Kittens"]
otherProductsforHealth = ["Cardboard box", "Catnip", "Cat tree", "Scratchers", "Litter Box", "Fur Brush"]
while True: 
  userName = input ("Hi! What is your name? ")
  print ("Hi! " + userName)
  answer1 = input(" Do you have a cat? (y/n)  ") .lower()
  if answer1 == 'y':
# If user has a Cat, then ask Cat's name
    answer = input ("What is your cat's name??! ")
    print ( answer + "?  What a beautiful name!!" )
    answer3 = input ("Is " + answer + " your first cat? (y/n)  ")
    if answer3 == 'y':
      print ("Oh, nice, here we will teach you everything you need to know to take good care of your cat! Like what food is good depending on the cat's age, or what the cat's need to have a helthy life!!")
      answer2 = input(" Is it a kitten? (y/n) ") .lower()
      if answer2 == 'y': 
        answer3 = input("How months old is your cat? (answer in #)  ")
        adult = '12'
        if answer3 <= adult:
          print ("Awww, so young")
        answer4 = input("Hey! " + userName + " do you still want to know the best cat products??  (y/n)  ")
        if answer4 == 'y':
          print ("ok...")
          print("I recomend you this brands/products:")
          print(kittenFoodWet)
          print("Another products that I recomend you are:")
          print(otherProductsforHealth)
          answer5 = input("Would you like to be redirectioned onto a web page that sells this products??  (y/n)")
          if answer5 == 'y':
            print("You will be redirectioned shortly")
            print("Loading.........")
            print("Loading............")
            print("Loading...............")
            print("Loading...")
            import webbrowser
            url1 = "https://www.amazon.com/Healthy-Kitten-Food/s?k=Healthy+Kitten+Food"
            webbrowser.open(url1)
            break
          else:
            print("Oh, ok... ")
            break
      else:
#close page,
        print("ok...")
        break
    else:
#print("We will redirect you to your preferences!!! ")
      print("Oh! nice!!")
      answer6 = input("Would you like information on the best cat food??  (y/n)  ")
      if answer6 == 'y':
        print("ok, so we recomend you:")
        print(adultCatDryFoodList)
        print(AdultCatWetFoodList)
        print("Is also important that cats have:")
        print(otherProductsforHealth)
        answer7 = input("Would you like to be redirectioned onto a web page that sells this products??  (y/n)")
        if answer7 == 'y':
          print("Ok!!")
          print("You will be redirectioned shortly")
          print("Loading.........")
          print("Loading............")
          print("Loading...............")
          print("Loading...")
          import webbrowser
          url2 = "https://www.amazon.com/Healthy-Cat-Food/s?k=Healthy+Cat+Food"
          webbrowser.open(url2)
          break
      else:
        print("Oh, ok...")
        break
  else:
    print ("Then why are you searching for cat food??! ")
  answer2 = input ("Are you planning on having a cat??  (y/n)  ") .lower ()
  if answer2 == 'n':
    print ("Oh! so the page will close automatically")
    print ("Closing...")
    print("...")
    print("Loading.........")
    print("Loading............")
    print("Loading...............")
    print("Loading...")
    break
  else:
    print("Oh! ok so...")
#redirect to line 4 ************** To complete ***************