import random

class FileReader:

    def __init__(self, filename): 
        self.__filename = None
        self.set_filename(filename)
        print("instance of FileReader class created!")

    def read_all(self):
        try:
            file_1 = open(self.__filename)
            lines = file_1.readlines()
            file_1.close()
            return lines
        except:
            print("file not opened. Terminating method")
            return False

    def line_count(self):
        lines = self.read_all()
        line_amount = len(lines)
        return line_amount   

    def get_filename(self):
        return self.__filename

    def set_filename(self, new_filename):
        if type(new_filename) == str:
            self.__filename = new_filename 

class WordFileReader(FileReader): 
            
    def display_filename(self):
        print(f"the file name is : {self.get_filename}")

    def all_words(self):
        all_words = FileReader.read_all(self) # opening the file from the parent class using read_all method
        
        self.full_dict = {}  # initialising empty dictionary to input the keys and nested dictionaries further into the code 
        for line in all_words: # this loop iterates through the lines in the text file to isolate each line 
            strip_line = line.strip() # this lines removes the /n in each line this is done to keep only the game-relevant text
            #print(strip_line)
            line_split = strip_line.split(",") # this seperates the text file by commas to extract the keys and values for the dictionary
            #print(line_split)
            key = int(line_split[0]) #the first index of the split line will be the main dictionary keys (round numbers)
            nested_key = line_split[1] # the next index refers to "incorrect" or "correct" keys for the nested dictionary key
            if nested_key == "incorrect":
                nested_key = "non-english"
            elif nested_key == "correct":
                nested_key = "english" 
            nested_values = line_split[2:] # the rest of the text file indexes are the game words and these will be made the values of the nested dictionary
        
            if key not in self.full_dict:  #ensures there is no duplicate keys 
                self.full_dict[key] = {} # inputs keys into the empty dictionary
            
            self.full_dict[key][nested_key] = nested_values  # inputs the nested keys and nested values into the main dictionary as keys of the round number keys
        #print(self.full_dict)
            
        return self.full_dict

    def __str__(self):
        instance_desc = f"The name of the text file being read is {FileReader.get_filename(self)} and this class reads a text file and converts it to a dictioary so the lexical decision task can be played ith different word dictionaries"
        return instance_desc #ask about string rep
        
    def get_rounds_at(self, round_num_list):
        count = 0 # the count variable ensures that the num list keys 1,2,3 will be attributed the values of whatever rounds are in the list
        round_num_dict = {} # empty dictionary for the specific rounds 
        for key in self.full_dict:  # iterates through the full dictionary to check which keys from the list need to be included 
            if int(key) in round_num_list: #converts to integer so can be checked against the round list
                count += 1  #counter increments each key will be key, key+1 etc (1,2,3...)
                round_num_dict[count] = self.full_dict[key] # this creates a new dictionary with the round number list as the only main keys
        #print(round_num_dict)
        return (round_num_dict)
            
    def get_round_range(self, ran_rounds):
        line_count = FileReader.line_count(self) 
        round_total = (line_count / 2)  # gets the total number of rounds from the lines in the text file as correct and incorrect is 2 lines in the text file
        count = 0 #resets counter
        round_range_dict = {} # initialises empty dict
        round_range_start = ran_rounds[0] #stores num of the first index of the range as a start value
        round_range_end = ran_rounds[1] #stores num of the last index of the range as a stop value
        round_range = list(range(round_range_start, round_range_end + 1)) #creates new list with the start value and end value and all values in between, +1 so end value is included
        if round_range_start < round_total or round_range_end <= round_total: #this line checks to make sure range is within boundaries of the total number of rounds 
            if round_range_start >= 0 or round_range_end >= 0: #ensures list parameters are psotive numbers 
                if len(ran_rounds) == 2: # ensures list total is 2 so theres only a start and stop value
                    if ran_rounds[0] < ran_rounds[1]: # ensures start value is less than stop value
                        for key in self.full_dict: 
                            if int(key) in round_range:  #if the key is in the range of numbers 
                                count += 1 
                                round_range_dict[count] = self.full_dict[key] #add to new dictionary of the round range
                        #print(round_range_dict)
                        return(round_range_dict)
                    else:
                        print("invalid start round number")
                else:
                    print("invalid round range")
            else:
                print("Range cannot be negative numbers")
        else:
            print("invalid round range - outside of existing rounds")
     
    def random_rounds(self):
        line_count = FileReader.line_count(self)
        round_total = (line_count / 2)
        count = 0 
        round_range_dict = {}

        round_range_end = random.randint(1,round_total + 1)  #creates random stop value between 1 and the total number of rounds
        round_range_start = random.randint(1,round_range_end) #creates random start value between 1 and the end value -1
        round_range = list(range(round_range_start, round_range_end + 1)) # creates list range of between these two values
        
        if round_range_start <= round_range_end: 
            for key in self.full_dict:
                if int(key) in round_range:
                    count += 1
                    round_range_dict[count] = self.full_dict[key]
                    #print(round_range_dict)
            return(round_range_dict)
        else:
            print(f"start value = {round_range_start} end value = {round_range_end}")
            print("invalid start round number")
            
     
    def exclude_rounds_at(self, rounds_nums_list):
        count = 0
        excluded_dict = {} #creates empty dict for non excluded rounds
        for key in self.full_dict: 
            if int(key) not in rounds_nums_list:
                count += 1
                excluded_dict[count] = self.full_dict[key] #inputs values not excluded as a dictionary
        #print(round_num_dict)
        return (excluded_dict)

    def exclude_round_range(self, ran_rounds):
        line_count = FileReader.line_count(self)
        round_total = (line_count / 2)
        count = 0 
        excluded_range_dict = {}
        excluded_range_start = ran_rounds[0]
        excluded_range_end = ran_rounds[1]
        excluded_range = list(range(excluded_range_start, excluded_range_end + 1))
        if type(ran_rounds) == list: # checks if ran_rounds is type list
            if type(excluded_range_start) == int and type(excluded_range_end) == int: #checks that the start and stop values are both integers
                #if ran_rounds[0] < ran_rounds[1]:
                    for key in self.full_dict:
                        if int(key) not in excluded_range:
                            count += 1
                            excluded_range_dict[count] = self.full_dict[key]
                #print(round_range_dict)
                    return(excluded_range_dict)
            else:
                print("Error - range values are not integers")
        else:
            print("invalid type - should be list")
    

#if __name__ == "__main__":
file_1 = WordFileReader("words.txt")
#print(file_1.all_words())