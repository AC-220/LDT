from filereader import WordFileReader
from participant import TrialParticipant

file_1 = WordFileReader("words.txt") # instance of WordFilereader is created using the words.txt text file
new_dict = file_1.all_words()

 
trial_participant = TrialParticipant("Alex","Cunningham")
trial_participant.set_words(new_dict)
run_game = True 
print("\n"*5)
print(f"Welcome, to the Lexical Decision Task, {trial_participant.get_firstname()} {trial_participant.get_lastname()}")
print("In this task, you will be presented with four words.")
print("Your task is to select whether all four words are of the English language!")
print("---")
print("\n"*1)
run_game = True
consent = input("Do you consent to participate in this game? (y/n): ")
if consent == "n":  # this asks user for consent and stops game loop if user says no
    run_game = False
    print("You have chosen to not participate in the game.")
else:
    pass

  
  
while run_game == True:
    print("The word position is now at: %s" % trial_participant.get_position()) # displays the current word position
    print(f"Particpant: {trial_participant.get_firstname()} {trial_participant.get_lastname()}") # prints particpant name
    print(f"Particpant Numbers: {TrialParticipant.instances_of_participants}") # print part. number 
    print(f"Correct: {trial_participant.get_correct()} Incorrect: {trial_participant.get_incorrect()}")
    words = trial_participant.select_words()
    participant_selection = input("Select 'y' or 'n' to move to the next position.") # user inputs whether to move to next position 
    
    if participant_selection.lower() != "y" and participant_selection.lower() != "n": # checks if input is valid
        print("\n"*5)
        print("Please select a valid response...")
    else: 
        hard = False
        # Additional Feature 2: Changing response keys after 3 correct guesses
        if trial_participant.get_correct() == 3 and hard != True:
            hard_mode = (input("Would you like to make it harder? (y/n): "))
            if hard_mode == "y":
                hard = True
                test = trial_participant.updated_response(participant_selection) # runs the new response function to change the response options if correct too many times
                if test == True:
                    trial_participant.increment_correct()  # calls methods to keep track of incorrect or correct choices
                elif test == False:
                    trial_participant.increment_incorrect()
            
            else:
                pass
        else:
            hard = False    
            test = trial_participant.response(participant_selection) # runs the response function to test the users response
            if test == True:
                trial_participant.increment_correct()  # calls methods to keep track of incorrect or correct choices
            elif test == False:
                trial_participant.increment_incorrect()   
   
        next = trial_participant.increment_position() # increments position to continue game
        
            
        print("\n"*1)
        
        if next == False:
            run_game = False
            print("\n"*5)
            print("There are no more selections available. The experiment has ended.")
            print(f"You got {trial_participant.get_correct()} answer(s) correct and {trial_participant.get_incorrect()} answer(s) incorrect.")
            # Additional Feature 1: Changing word set
            change_words = str(input("Would you like to change the words? (y/n): ")) # allows users to change word type, allowing code reuse by calling new instance and using the same methods
            if change_words == "y":
                file_2 = WordFileReader("new_words.txt") # creates new instance with new word file so the class methods can be called and used
                changed_dict = file_2.all_words()   #stores new dict in changed_dict variable
                trial_participant.set_words(changed_dict) #sets dictionary as playable
                run_game = True #continues game
            else:
                pass



