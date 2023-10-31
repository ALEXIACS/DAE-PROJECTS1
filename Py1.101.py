while True: 
  userName = input ("Hi! What is your name? ")
  print ("Hi! " + userName)
  answer = input("Would you like to study? (◍＞◡＜◍) (y/n)  ") .lower()
  if answer == 'y':
    answer2 = input("What would you like to study?? Biology? math? literature?") .lower()
    if answer2 == 'Biology':
#simulating loading bar till added
      print ("PREPARING MATERIALS...")
      print ("Redirecting...")
      print ("...")
      print ("redirecting")
      import webbrowser
      url1= "https://www.khanacademy.org/science/ap-biology"
      webbrowser.open(url1)
      break
    if answer2 == 'Math':
      print ("PREPARING MATERIALS...")
      print ("Redirecting...")
      print ("...")
      print ("redirecting")
      import webbrowser
      url2= "https://www.khanacademy.org/math/ap-calculus-ab"
      webbrowser.open(url2)
      break
    else:
      print("You'll get bad grades ಠ╭╮ಠ ")
      answer3 = input("Do you want to proceed? >:c ? (y/n) ") .lower()
    #answer 3 answers 
      if answer3 == "y":
        print("Redirecting...")
        print("...")
        print("...")
        print ("Process couldn't be completed due to an unexpected error...")    
      else:
        print ("Process couldn't be completed due to an unexpected error...")
#repeat to line 4
      break