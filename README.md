# LDT
Lexical Decision Task Python Program

The main.py file implements a lexical decision task where a participant is presented with words and must decide if they are valid English words. The project contains 3 files which cover different aspects of the game. 

Imports: 
  WordFileReader from filereader module: Reads words from a file.
  TrialParticipant from participant module: Manages participant data and responses.
  
Initialization:
  Creates an instance of WordFileReader using words.txt.
  Retrieves all words from the file and stores them in new_dict.
  Creates a TrialParticipant instance with a given name.
  Sets the words for the participant using new_dict.
  
Welcome Message:
  Prints a welcome message and instructions for the task.

Consent:
  Asks the participant for consent to participate. If the participant does not consent (n), the game stops.
  
Main Game Loop:
  Runs while run_game is True.
  Displays the current word position, participant's name, number of participants, and the count of correct and incorrect responses.
  Selects four words for the participant to evaluate.
  Asks the participant to input whether to move to the next position (y or n).
  
Response Handling:
  Validates the participant's input.
  If the participant has three correct guesses, offers to make the task harder by changing the response keys.
  Checks the participant's response and updates the count of correct or incorrect answers.
  Increments the word position.
  
End of Game:
  If there are no more words to evaluate, the game ends.
  Displays the total number of correct and incorrect answers.
  Offers the participant the option to change the word set and continue the game with a new set of words from new_words.txt.
