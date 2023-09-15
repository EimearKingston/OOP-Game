from typing import ClassVar
import random
import sys

class Enemy: 
    '''
    Class generates random enemy for player to duel
    Makes:
        -name
        -status(how powerful)
        -Spell used
        -score/lives
    '''
    import random
    #Define variables 
    __names:ClassVar[list]=["Merula", "Huxley", "Corvina" ]
    __status:ClassVar[list]=["powerful", "almost invincible", "near unbeatable"]
    __spells:ClassVar[list]=["D", "P", "A"]
    __escore:ClassVar[int]=3
    def __init__(self):
        '''Initializes class'''
        #Choose random enemy name
        self.name=random.choice(self.__names)
        #Choose random enemy spell
        self.spell=random.choice(self.__spells)
        #Choose random enemy status
        self.status=random.choice(self.__status)
        self.score=self.__escore
        pass
    def get__names(self):
        '''gets private variable 'names' '''
        return self.__names
    def set__names(self, names:list):
        '''sets private variable 'names' '''
        self.__names=names
    names=property(get__names, set__names) 
    def get__status(self):
        '''gets private variable 'status' '''
        return self.__status
    def set__status(self, status:list):
        '''sets private variable 'status' '''

        self.__status=status
    status=property(get__status, set__status)
    def get__escore(self):
        '''gets private variable 'escore' '''
        return self.__escore
    def set__escore(self, escore:int):
        '''sets private variable 'escore' '''
        self.__escore=escore
    escore=property(get__escore, set__escore)
    def __eq__(self, other):
        '''checks if two objects are of the same class'''
        if isinstance(other, Enemy): #isinstance checks for equality
            return "Are they equal?: " + str(True)
        return "Are they equal?: " + str(False)
     
    def __ne__(self, other):
        '''checks if two objects are not of the same class'''
        if not isinstance(other, Enemy): #not isinstance checks for inequality
            return "Are they not equal?: " + str(True)
        return "Are they not equal?: " + str(False)
    def docstring(self):
        return self.__class__.__doc__      
class Duel:
    '''
    Class hosts duel between player and generated enemy
    '''
    #Define variables
    __name:ClassVar[str]
    __type:ClassVar[str]
    score:ClassVar[int]=3
    __spell_guide:ClassVar[str]="Spell guide: D=disarm P=protect A=attack" 
    result:ClassVar[str]=""
    def __init__(self, name:str, type:str, **kwargs):
        '''Initializes class'''
        enemy=Enemy() #Get Enemy() class object for this instance of Duel() class
        #Checks for 'lives' in kwargs in case player changes score variable
        if "lives" in kwargs.keys():
            self.score=kwargs["lives"]
        self.__name=name
        self.__type=type
        #print welcome greeting
        print("Welcome, " + f"{self.__name}! A fine " + f"{self.__type} like you is going to have to duel " +\
             f"{enemy.name} who is " + f"{enemy.status}. You have " + f"{self.score} lives." )
        #print all kwargs except 'lives'
        for key, value in kwargs.items():
            
            if key!="lives":
                print(key.capitalize() + ": " + str(value))
        #while loop for duel loops until enemy.score=0 or player score=0
        while self.score>=0:
            
    
            enemy_spells=["D", "P", "A"]
            #Generate enemy spell
            enemy_spell=random.choice(enemy_spells)
            #Exit loop Checks:
            if enemy.score==0:
                
                self.result="\nYOU WIN!!"
                break #end game (exit loop)
            if self.score==0:
                
                self.result="\nYOU LOSE"
                
                break #end game (exit loop)
            print("\n" + self.__spell_guide)
            #Print game prompt
            self.spell=input("Enter a spell: ")
            if self.spell!="D" and self.spell!="P" and self.spell!="A" :
                #print error if input other than E/F/P entered
                raise TypeError("Please enter only D or P or A (case sensitive)")
            #Compare self.spell to enemy_spell and print response 
            if self.spell=="D":
                if enemy_spell=="P":
                    enemy.score=enemy.score-1
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print("You win this round!")
                if enemy_spell=="A":
                    self.score=self.score-1
                    #break
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print(enemy.name + " wins this round!")
                if enemy_spell=="D":
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print("Draw")
                
            if self.spell=="P":
                if enemy_spell=="P":
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print("Draw")
    
                if enemy_spell=="A":
                    enemy.score=enemy.score-1
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print("You win this round!")
                    
                if enemy_spell=="D":
                    self.score=self.score-1
                    
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print(enemy.name + " wins this round!")
            if self.spell=="A":
                if enemy_spell=="P":
                    self.score=self.score-1
                    
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print(enemy.name + " wins this round!")
                    
                    
    
                if enemy_spell=="A":
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print("Draw")
    
                    
                    
                if enemy_spell=="D":
                    enemy.score=enemy.score-1
                    print("Enemy: " + str(enemy.score))
                    print("You: " + str(self.score))
                    print("You win this round!")
                    
                    
        print(self.result)            
        
    def __str__(self):
       
        return self.result
    
    def get__name(self):
        '''gets private variable 'name' '''
        return self.__name
    def set__name(self, name:str):
        '''sets private variable 'name' '''
        self.__name=name
    name=property(get__name, set__name)
    def get__type(self):
        '''gets private variable 'type' '''
        return self.__type
    def set__type(self, type:str):
        '''sets private variable 'type' '''
        self.__type=type
    type=property(get__type, set__type)  
    def __eq__(self, other):
        '''checks if two objects are of the same class'''
        if isinstance(other, Duel):
            return "Are they equal?: " + str(True)
        return "Are they equal?: " + str(False)
    def docstring(self):
        return self.__class__.__doc__
    
        
class Player(Duel): 
    def __init__(self, name:str, type:str, **kwargs): #type=witch/wizard/warlock
        '''Initializes class'''
        
        #sends inputs to parent class
        super().__init__(name, type, **kwargs)  
    def __eq__(self, other):
        return super().__eq__(other)
    def docstring(self):
        return self.__class__.__doc__
    
    pass
class Witch(Player): 
    '''Sets player type to witch
    Passes parameters and attributes to Parent class Player'''
    def __init__(self, name:str, **kwargs): 
        '''Initializes class'''
        #sends inputs to parent class
        super().__init__(name, str(self.__class__.__name__), **kwargs)
    def __eq__(self, other):
        return super().__eq__(other)
    def docstring(self):
        return self.__class__.__doc__
    
    pass
class Wizard(Player): 
    '''Sets player type to wizard
    Passes parameters and attributes to Parent class Player'''
    def __init__(self, name:str, **kwargs): 
        '''Initializes class'''

        
        super().__init__(name, str(self.__class__.__name__), **kwargs)
    def __eq__(self, other):
        return super().__eq__(other)
    def docstring(self):
        return self.__class__.__doc__
    
    pass
class Warlock(Player): 
    '''Sets player type to Warlock
    Passes parameters and attributes to Parent class Player'''
    def __init__(self, name:str, **kwargs): 
        '''Initializes class'''

        
        super().__init__(name, str(self.__class__.__name__), **kwargs)
    def __eq__(self, other):
        '''checks if two objects are of the same class'''
        return super().__eq__(other)
    def docstring(self):
        return self.__class__.__doc__
    
    pass


witch:Witch=Witch("name", abilities="Ice", lives=5, age=20, weapon="Wand") #^^example of Witch object with kwargs
