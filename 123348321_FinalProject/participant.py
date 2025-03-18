import random  # importing the random module for random selection 


class TrialParticipant:

    instances_of_participants = 0
    words = { 
        1: 
        {
            'english': ['girl', 'panda', 'tree', 'dog'], 
            'non-english': ['gyrl', 'panda', 'trop', 'dog']
        }, 
    
        2: 
        {
            'english': ['tram', 'farm', 'help', 'shop'], 
            'non-english': ['terg', 'farm', 'hilp', 'shyp']}, 
    
        3: 
        {
            'english': ['jump', 'rain', 'worm', 'dark'], 
            'non-english': ['jump', 'roim', 'warm', 'durh']
        }, 
    
        4: 
        {
            'english': ['pull', 'draw', 'fork', 'kick'], 
            'non-english': ['pull', 'yruw', 'fjrc', 'kick']
        }, 
    
        5: 
        {
            'english': ['harsh', 'storm', 'spoon', 'light'], 
            'non-english': ['hyrth', 'storm', 'spuun', 'light']
        }, 
    
        6: 
        {
            'english': ['green', 'viola', 'flour', 'drain'], 
            'non-english': ['green', 'vaeph', 'flour', 'dyyyn']
        }
    }

    def __init__(self, first_name, last_name):  # defines the class variables
        self.first_name = first_name 
        self.last_name = last_name
        TrialParticipant.instances_of_participants += 1   # incrementing the instances 
        self.participant_num = TrialParticipant.instances_of_participants  # particant number becomes the instance 
        self.possible_selections = {"english": "y", "non-english": "n"} # dictionary of possible chocies
        self.position = 1
        self.correct_choices = 0
        self.incorrect_choices = 0
        self.word_type = ["english", "non-english"]
        self.selection= random.randint(0,1) # selects random option from the 2 options englis or non english

    def __str__(self):
        desc = """This code creates a game where the user must choose whether a set of words are english or not english words. The code tracks the players correct and incorrect choices and outputs them at the end of the game. 
        The code increments the rounds and stops when rounds reaches six. When the user gets a choice wrong information is given on the users choice and the right answer. The code takes a set of words from the nested dictionary
        and outputs it to the player to play the game with those words and this increments for each round of the game. This class also gives the option to set a new dictionary of words to play the game with."""
        return desc

    def get_correct(self):
        return self.correct_choices  # returns the number of correct choices player made
    

    def get_incorrect(self):
        return self.incorrect_choices   # returns the number of incorrect choices player made
    
    def increment_correct(self):
        self.correct_choices = self.correct_choices + 1  # increments correct choice number by 1 when player gets question correct
        return self.correct_choices   

    def increment_incorrect(self):
        self.incorrect_choices = self.incorrect_choices + 1  # increments incorrect choice number by 1 when player gets question incorrect
        return self.incorrect_choices
    
    def increment_position(self): # ---- positional argument needed for position
        self.position = self.position + 1 # increments position by 1
        if self.position > 6:  # limits max rounds to 6
            return False
        return True

 
    def response(self, selection):
        type = self.word_type[self.selection] # english or non english chosen from the list "word_type" randomly  
        #key_association = self.possible_selections[selection] # stores value of the right answer
        if selection == "y":  # if selection is yes then the key is english
            key = "english"
        else:                # if no then key is non english 
            key = "non-english"
        if type == key:  # if word type is englsih then its correct return true
            print("The participant selected: %s" % selection)
            #print("the current word type is: %s" % key)
            #print("The correct response for this was: %s" % type)
            return True
        else:
            print("The participant selected: %s" % selection)
            #print("the current word type is: %s" % key)
            #print("The correct response for this was: %s" % type)
            return False  
        
    def select_words(self):
        #print("The current word type is: %s " % self.word_type[self.selection]) 
        self.selection= random.randint(0,1)
        type = self.word_type[self.selection]
        words_at_type = self.words[self.position][type] # finds list of words from the nested dictionary "words"
        print(words_at_type)
        return words_at_type # return s the list of words

 
    def reset(self):
        self.position = 1 # resets position to 1
    
    def get_firstname(self):
        return self.first_name 
    
    def set_firstname(self, new_firstname):
        new_firstname = input("enter new first name: ")
        return new_firstname # sets new first name 
    
    def get_lastname(self):
        return self.last_name
    
    def set_lastname(self, new_lastname):
        new_lastname = input("enter new last name: ")
        return new_lastname
    
    def set_words(self, new_words):
        self.position = 1 #restarts game with new words 
        self.incorrect_choices = 0 # resets correct and incorrect counters
        self.correct_choices = 0 
        invalid = False  # check for debug
        if type(new_words) == dict: # verifies if word set is a dictionary
            for key, value in new_words.items(): # loops through the keys in the dictionary
                #key = int(key)
                if type(key) == int and type(value) == dict:  # ensures keys are integers and values are a dictionary to conform to nested dict format
                    for nested_key, nested_value in value.items(): # loops through the nested keys and values in the value dictionary
                        if type(nested_key) == str and type(nested_value) == list and (len(nested_value) >=2): # ensures nested key is string and nested value 
                                                                    # is a list and that there is at least 2 values in the lists. 
                            invalid = False                                               
                        else:
                            invalid = True
                            break                       
                else:
                    invalid = True    
        else:
            invalid = True
        if invalid == True:
            print("invalid set of words")
        elif invalid == False:
            TrialParticipant.words = new_words # sets the game words as the new words 
            #print(new_words)

                        
    def updated_response(self, selection):
        type = self.word_type[self.selection] # english or non english chosen from the list "word_type" randomly  
        #key_association = self.possible_selections[selection] # stores value of the right answer
        if selection == "n":  # if selection is no then the key is english 
            key = "english"
        else:                # if yes then key is non english 
            key = "non-english"
        if type == key:  # if word type is englsih then its correct return true
            print("The participant selected: %s" % selection)
            return True
        else:
            print("The participant selected: %s" % selection)
            return False                   
                
                    
                
    
    def get_position(self): 
        return self.position 




new_words = { 
        1: 
        {
            'english': ['hand', 'power', 'great', 'dot'], 
            'non-english': ['frrl', 'panda', 'frop', 'dog']
        }, 
    
        2: 
        {
            'english': ['grim', 'fathom', 'pale', 'slop'], 
            'non-english': ['terg', 'falt', 'odop', 'vrip']}, 
    
        3: 
        {
            'english': ['run', 'pain', 'chore', 'bark'], 
            'non-english': ['rjni', 'roim', 'warm', 'dumb']
        }, 
    
        4: 
        {
            'english': ['push', 'hollow', 'cork', 'attack'], 
            'non-english': ['pgjl', 'plus', 'fjrc', 'gack']
        }, 
    
        5: 
        {
            'english': ['hash', 'palm', 'spun', 'light'], 
            'non-english': ['hyrth', 'strem', 'spuun', 'ljudt']
        }, 
    
        6: 
        {
            'english': ['yellow', 'leaf', 'flour', 'drain'], 
            'non-english': ['yillow', 'defh', 'flour', 'dyyyn']
        }
    }     

