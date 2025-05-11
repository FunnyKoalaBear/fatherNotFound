# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define main = Character("Bancat")
define dad = Character("dad")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show m happy

    # These display lines of dialogue.


    #pujithas starting scene
    scene house
    dad "gonna get milk"
    main "ok"

    #mithuns flashback scene
    scene flashback
    main "oh my gosh"

    
    #dillips first grocery store scene 
    scene outside_gstore

    main "Grocery store should be where dad is at"
    main "Here I gooo huhuhu"

    scene In_gstore

    main 






    # This ends the game.

    return
