import sys
from colorama import Fore

helpfile = """
======================
|      COMMANDS      |  
======================
--help : Lists commands.
--color : Requires one argument, prints 'Hello World' in color selected. 
Colors:

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE

"""

nextcolor = False

if len(sys.argv) != 1:
    for argument in sys.argv:
        # print("Argüman:",argument)
        if nextcolor == False:
            if argument == "--help":
                print(helpfile)
            elif argument == "--color":
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "BLACK"):
                    print(Fore.BLACK + "Hello World" + Fore.RESET)
                    nextcolor = not nextcolor
                
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "RED"):
                    print(Fore.RED + "Hello World" + Fore.RESET)
                    nextcolor = not nextcolor
                
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "GREEN"):
                    print(Fore.GREEN + "Hello World" + Fore.RESET)
                    nextcolor = not nextcolor
                
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "YELLOW" ):
                    print(Fore.YELLOW + "Hello World" + Fore.RESET )
                    nextcolor = not nextcolor
                
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "BLUE" ):
                    print(Fore.BLUE + "Hello World" + Fore.RESET )
                    nextcolor = not nextcolor
                
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "MAGENTA" ):
                    print(Fore.MAGENTA + "Hello World" + Fore.RESET )
                    nextcolor = not nextcolor
                
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "CYAN" ):
                    print(Fore.CYAN + "Hello World" + Fore.RESET )
                    nextcolor = not nextcolor
                
                if(sys.argv[int(sys.argv.index(argument)) + 1] == "WHITE" ):
                    print(Fore.WHITE + "Hello World" + Fore.RESET )
                    nextcolor = not nextcolor
        elif argument == "--help":
            print(helpfile)

else:
    print(helpfile)
