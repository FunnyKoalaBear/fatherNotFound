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


    # These display lines of dialogue.


    #pujithas starting scene
    scene house
    show dad happy at left
    show main happy at right
    dad "gonna get milk"
    main "okay"

    #mithuns flashback scene
    scene flashback
    main "oh my gosh"

    
    #dillips first grocery store scene 
    scene outside_gstore

    main "Grocery store should be where dad is at"
    main "Here I gooo huhuhu"

    scene In_gstore

    main "hi"
    main "wasup"



    #at the flower store
    scene flower
    define fso = Character("flower shop owner")
    main "oOoOoOo what pretty flowers, I wonder if papa is in there....."
    menu:
        "go in":
            label flo:
                scene flin
                show main happy at left
                show fso happy at right
                main "wow these flowers smell so nice"
                show main sad at left
                show fso angry at right
                main "uh oh.. !!!!!!"
                fso "grrrrr now you have to pay for those flowers"
                main "nuuuuuuuuuuuu"
                return

        "don't go in":
            show fso happy at left
            show main normal at right
            fso "come on in child, look at all these pretty flowers"
            main "*hesitates*"
            fso "The flowers smell really good, I promise"
            main "oh okay, i suppose a few sniffs wouldn't hurt"

            jump flo





    # This ends the game.

    return
