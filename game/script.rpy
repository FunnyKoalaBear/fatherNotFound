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
    main "Here I gooo"

    scene In_gstore
    main "wow i love the grocery store"
    menu:
        "Find dad":
            jump groceryconc
            

        "get distracted":
            main "I have some leftover pocket money this week"
            #show cash balance

            main "I'd love to eat some chocolates"
            main "But I would also love to play in the arcade"
            menu:

                "Go to Arcade (50$)":
                    jump arcade1
                "Go buy chocos (20$)":
                    jump chocos1
    label groceryconc:
        main "I should probably ask the store clerk about my dad"
    label arcade1:
        main "time to go to the arcade"
        #deduct money
        #play super fun game

        main "wow that was fun"

    
    label chocos1:
        main "I love me some chocos"
        #deduct money
        

        #in the end
        main "why was I here again??"
        main "omg I need to find my father"
        main "I need to get going"

        jump groceryconc








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
