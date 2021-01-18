import random 

"""
This is Henry's amazing code. 

 0 = "Rock" 
 1 = "Scissors" 
 2 = "Lizard" 
 3 = "Paper" 
 4 = "Spock" 
"""



def name_to_number(name):
    if name == "Rock":
        return 0
    elif name == "Scissors":
        return 1
    elif name == "Lizard":
        return 2
    elif name == "Paper":
        return 3
    elif name == "Spock":
        return 4
    else:
        return "Pick a name" 
  
def number_to_name(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Scissors"
    elif number == 2:
        return "Lizard"
    elif number == 3:
        return "Paper"
    elif number == 4: 
        return "Spock"
    else:
        return "Pick a nuber between 0 and 4" 
a1 = (number_to_name(2))

def rpsls(choice):
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        score = (name_to_number(choice) - comp_number)%5
        print("Player chose " + str(choice))
        print ("Computer chose " + str(comp_choice))
        if score == 0:
               return "tie"
        elif score == 1: 
               return "The computer won :(" 
        elif score == 2: 
               return "The computer won :(" 
        elif score == 3: 
               return "You won" 
        elif score == 4:
               return "you won" 
        else:
               "Something went wrong :<"
               
print (rpsls("Rock"))
print ()
print ("--------------------------------------------------------")
print ()
print (rpsls("Scissors"))
print ()
print ("--------------------------------------------------------")
print ()
print (rpsls("Lizard"))
print ()
print ("--------------------------------------------------------")
print ()
print (rpsls("Paper"))
print ()
print ("--------------------------------------------------------")
print ()
print (rpsls("Spock"))
print ()
print ("--------------------------------------------------------")
print ()

    
    
    
    
    
    
    
    
    
    
    
    
