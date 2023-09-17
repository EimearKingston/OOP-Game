# OOP-Game  
There are 6 classes – Enemy, Duel, Player, Witch, Wizard, Warlock.

The Enemy Class creates an enemy object for the player to ‘duel’. It picks a random name, status i.e. description of how powerful it is and a random spell for the enemy to use each round.

The Duel Class runs the code for the actual game between the player and the enemy. It prints the
player attribute inputs in a welcome greeting, including name, type(witch, warlock, wizard etc.) and
various kwargs depending on player input. There are also getters and setters for private variables
and an equality function to test if an object is of the same class as another object. There is a docstring function that when called returns the class docstring.

The Player class is a child class of Duel(). It creates a ‘player’ object and passes name, type and kwarg
attributes using super() to parent class Duel.

Witch, Warlock, and Wizard classes are child classes of Player() (grandchild class of Duel()). Contain
the same functions and attributes of Player except type is passed as the name of the class.

How it is called:

        witch:Witch=Witch(“name”) #for object of game to be initialised
        
        print(witch.__str__()) #prints result of game
        
        enemy:Enemy=Enemy() #creates Enemy class object
        
        player: Player=Player("name", "Warlock") #creates player class object
        
        warlock:Warlock=Warlock("name") #creates warlock class object
        
        print(enemy.set__escore(5)) #sets score/lives of enemy object to 5
        
        print(enemy.docstring()) #prints docstring of Enemy class
        
        duel:Duel=Duel("name", "Wizard”) #calls game directly
        
        print(witch==duel) #calls equality function
        
        print(witch==player)
        
        print(witch==warlock)
        
        witch:Witch=Witch("name", abilities="Ice", lives=5, age=20, weapon="Wand") #^^example of
        
        Witch object with kwargs
        
        witch:Witch=Witch("name”, lives=0)

        
        ^set ‘lives’ kwarg=0 if need to bypass game to see results of other functions e.g. __eq__


Example of call: witch:Witch=Witch("name", abilities="Ice", lives=5, age=20, weapon="Wand") 

![image](https://github.com/EimearKingston/OOP-Game/assets/144938447/d63ae142-7f40-4d3b-bd79-af16ef53cd34)


![image](https://github.com/EimearKingston/OOP-Game/assets/144938447/268ddeb8-10db-4dea-a110-ffb107e3ed88)  

![image](https://github.com/EimearKingston/OOP-Game/assets/144938447/72fe5328-e591-49aa-a4a2-c28406801332)  

![image](https://github.com/EimearKingston/OOP-Game/assets/144938447/493f45a7-36d8-4913-a1bf-b392ff4dbd7b)





        


