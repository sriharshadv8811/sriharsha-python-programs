import random

options = ["Rock","paper","scissors"]
AI = random.choice(options)
user = raw_input("pick either Rock,paper or scissors:")
user = user.lower()
if user  == 'rock' or 'paper' or 'scissors':
    print ("the computer has drawn %s whilst you have drawn %s" % (AI,user))
       if user == 'rock':
            if AI == "Rock':        print 'Tie Game'
                 elif AI == 'paper':
                      print 'AI wins'
                 else:
                       print 'User wins'
         if user == 'paper':
                 if AI == 'rock':
                    print 'user wins'
                 elif AI == 'paper':
                     print 'Tie Game'
                 else:
                    print 'AI Wins'
          if user == 'scissors':
                 if AI == 'Rock':
                      print 'AI wins'
                 elif AI == 'paper':
                     print 'user wins'
                 else:
                 print 'Tie Game'
                 
