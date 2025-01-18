# Cinnamoroll's Vending Machine! ;D

print(""".★✧.❀ .═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════""")
print(""" 
      
                                                                                                                         ❀                                                    ✩
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣴⠶⠶⠶⠶⠦⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀★⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠾⠟⣿⣿⠾⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⢶⣤⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                 ⠀⠀⠀⠀⢀⣶⢿⣻⡷⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠟⠉⠀⠀⠸⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣀⠈⠙⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ▒█▀▀█ ░▀░ █▀▀▄ █▀▀▄ █▀▀█ █▀▄▀█ █▀▀█ █▀▀█ █▀▀█ █░░ █░░ █ █▀▀ ❀              ⠀ ⢀⣼⣟⡿⣽⣻⢿⡽⣟⡿⣧⡀⠀✩⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀❀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⢀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ▒█░░░ ▀█▀ █░░█ █░░█ █▄▄█ █░▀░█ █░░█ █▄▄▀ █░░█ █░░ █░░ ░ ▀▀█               ⠀⠀⣴⣿⣻⢾⣻⣯⣟⣯⣿⣻⣽⢿⡅⠀⠀⢀⣠⣴⣶⣤⠀⠀⣠⣤⣤⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⢠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     ▒█▄▄█ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀░░░▀ ▀▀▀▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ░ ▀▀▀     ⠀⠀⠀⠀⠀⠀⠀⠀   ⢹⣷⣻⢿⣽⢾⠉⠁⢻⡷⣯⡿⠁⢀⣴⣿⣻⢷⣻⡾⣷⣾⢿⣽⢾⣳⣿⡆⠀⠀                
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀⢀⡿⠁⠀⠀⣰⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠙⠷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                               ⠀⠀⠻⣽⢿⡾⣯⠀⠀⠀⢻⣽⠇⢠⡾⣟⣾⡽⣟⣯⢿⣳⣯⡿⣾⣻⣟⣾⠃⠀⠀❀
⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠐⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⡇⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⣄⡀⠀⠀⠀⠀⠀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀             ⠀⣠⡆⠀⣤⠀⣶⠙⡿⣽⢿⣆⠀⠀⢸⡿⠀⢼⣻⠏⠁⢿⠿⠙⠛⢯⣷⣟⣯⡷⣿⣽⣳⡀⠀
⠀⠀⠀⣀⣴⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠉⠁⠉⠈⠉⠀⠀⠀⠀⠀⠀⣠⢤⣀⠀⠀⠀⠀⠀⠉⠿⠿⠁⡀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⠀⠀⠀   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄          ⠀⠀⢾⣟⣧⠤⠺⡷⢾⠦⣧⣌⣙⢯⢷⡄⠀⠿⠀⣻⠃⠀⠀⠀⠀⠀⣠⣞⣷⢯⡿⣽⡷⣯⠷⠀⠀  
⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣄⠤⠠⠐⢀⡀⠀⠀⠀⠀⠀⠋⠁⠉⠁⠀⠀⠀⠀⠀⠄⠀⠀⠀⢁⠀⠀⣼⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡄⠀                                                                     ★     ⠹⢾⠧⠀⠛⠀⠟⠀⠀⠙⠫⣿⣶⣤⡀⠀⠀⡅⠀⠀⣀⣴⢾⡟⠯⠟⠚⣛⠛⠉⠉⠀⠀⠀⠀
⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠻⢶⣤⣴⡾⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣤⠀⠜⣀⣴⠟⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠀                                                                           ⣠⣤⣤⣶⢶⣶⣶⣤⣦⣤⣀⠀⠈⠺⣷⣻⣆⠀⠀⠀⠐⠛⣉⣤⣴⣶⢿⣻⣟⣿⣻⣷⢶⡄⠀⠀
⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀⣿⠃⠀⠀⢸⡟⠳⠶⠶⠶⢦⣶⣴⣶⣴⣶⣶⣿⠉⠀⠹⣷⣿⣿⣥⣄⡀⠀⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇                                                                      ⠀⢀⣾⣟⣷⣻⡾⣟⠗⠉⠈⠁⠛⠙⠋⠀⠀⠙⢷⣻⠇⠀⠀⠀⠛⠉⠉⠈⢉⣿⣻⢾⣳⡿⣞⣿⣽⡀⠀
⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⢿⣆⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⠀⢀⣿⠟⠉⠉⠉⠛⣷⡄⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇     ❀                                                                ⣀⣼⣟⣾⡽⣷⣟⣿⣣⣀⣀⣠⠤⡴⣶⣦⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠘⠋⠟⣿⣽⣻⣽⢷⣯⣧⡀
⠘⢷⣄⡀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠟⠃⠀⠀⠀⠀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠿⣷⡀⠀⠀⣀⠀⠈⣿⡄⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⣀⣼⠏⠀                                                                      ⠻⣟⡾⣯⣟⡷⣿⣞⣯⡿⠝⠁⣀⣴⡟⠀⠀⠀⠀⣴⡀⣽⢿⠄⠀⠀⠠⣄⡀⠀⠀⣸⡷⣯⣟⡿⣾⡽⣿
⠀⠀⠉⠛⠷⠶⠶⠶⠶⠾⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣴⠏⠀⠀⣽⡇⠀⠀⠀⠈⠛⠿⠶⠶⠶⠶⠿⠋⠁⠀⠀                                                                      ⠀⠀⠀⢻⣯⢿⣳⣯⠗⢁⣴⣾⣻⣽⣄⠀⠀⠀⠀⢻⡃⢸⣿⣳⣦⣤⣼⣻⣽⢿⣻⣯⣟⣷⢿⣽⡷⣟⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⣴⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                            ⠀⠈⠛⠛⠉⠁⣴⢿⣻⡾⣽⡾⣽⣻⣧⠀⠀⣸⣧⠀⢻⣷⣻⣞⣷⢯⣟⣯⣷⣟⣾⡯⠿⠾⠝⠉⠀★
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀★⠀⠀⠀⠀⠀⠀⠹⣷⡾⠋⠀⠁⠀⠀⠀⠀⠀⢀⣾⠛⠉⠙⠓⠀⠀⢀⣴⠟⠛⠿⠾⠿⠛⠉⠀⠀⠀✩⠀⠀❀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                ⠀⢿⣯⡷⣿⢯⣟⣿⣳⢿⣻⣟⣯⣟⣇⠀⠹⣷⣻⡾⣟⣯⣟⣾⡝⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠐⢶⣶⣶⣶⣶⣾⣿⡀⠀⠀⢶⡶⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                  ⠀⠑⠛⢫⣿⣻⣞⣯⣿⣻⢾⣽⣾⣻⠀⠀⠈⠓⠿⣻⠽⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⣀⣠⡿⠁⠀⠀⠀⠀⢹⣇⡀⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                     ⠀⠀⢳⣯⣟⡷⣯⣟⣯⣷⢯⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                                                        ⠀⠈⠿⣞⣿⣽⠏⠃⠉⠀⠀⠀⠀★⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
print(""" ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════. ❀.✧★.""")

# Cinnamoroll is my favorite Sanrio Character and I dedicate making a vending machine menu based off him and his lore.

print("""
                                                ╭────────────────────────────────────────────────────────────────────────────────────────────────────────╮
                                                │                                       ꧂♡┊ Cinnamoroll's Menu ┊♡꧂                                       | 
                                                │╭──NO:─────────────Snacks─────────────────╮│╭─────────Price──────────╮│╭─────────────Stocks────────────╮|
                                                ││• C1 ✿ Cinnamoroll's Blueberry Cheesecake       ❀   19 DHS                     ★   20                 ││
                                                ││• C2 ✿ Cinnamon Rolls Bites♡‧₊˚                 ❀   15 DHS                     ★   25                 ││
                                                ││• C3 ✿ Cinnamoroll's Butter Cookies             ❀   28 DHS                     ★   23                 ││
                                                ││• C4 ✿ Chocolate Almond Coins                   ❀   21 DHS                     ★   20                 ││
                                                ││• C5 ✿ Mocha's Chocolate Banana Muffin          ❀   19 DHS                     ★   25                 ││
                                                ││• C6 ✿ Mocha's Honey Bun Cake                   ❀   25 DHS                     ★   20                 ││
                                                ││• C7 ✿ Chocolate Chip Coffee Cake               ❀   18 DHS                     ★   23                 ||
                                                ││• C8 ✿ Cinnamoroll's Steam Bun                  ❀   18 DHS                     ★   25                 ││
                                                ││• C9 ✿ Cinnamoroll Vanilla Mochi                ❀   15 DHS                     ★   25                 ││
                                                ││• C10✿ Cinnamoroll's Limited PEPERO Box         ❀   23 DHS                     ★   25                 ││                                                           
                                                │╰──────────────────────────────────────────────────────────────────────────────────────────────────────||
                                                ╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯""")
print("""
                                                ╭────────────────────────────────────────────────────────────────────────────────────────────────────────╮
                                                │                                       ꧂♡┊ Cinnamoroll's Menu ┊♡꧂                                       |
                                                │╭──NO:─────────────Drinks─────────────────╮│╭─────────Price──────────╮│╭─────────────Stocks────────────╮|
                                                ││• D1 ✿ Pumpkin Spice Latte                      ❀   24 DHS                     ★   23                 ││
                                                ││• D2 ✿ Hot Cocoa with Marshmallows              ❀   19 DHS                     ★   23                 ││
                                                ││• D3 ✿ Chocolate Chai                           ❀   15 DHS                     ★   22                 ││
                                                ││• D4 ✿ Deluxe Espresso                          ❀   19.50 DHS                  ★   24                 ││
                                                ││• D5 ✿ Classic Boba Tea                         ❀   23.70 DHS                  ★   25                 ││
                                                ││• D6 ✿ Cafè Machiatto                           ❀   28.30 DHS                  ★   23                 ││
                                                ││• D7 ✿ White Chocolate Cappuccino               ❀   17 DHS                     ★   25                 ||
                                                ││• D8 ✿ Creamy Americano                         ❀   15 DHS                     ★   23                 ││
                                                ││• D9 ✿ Classic Iced Coffee                      ❀   19 DHS                     ★   25                 ││
                                                ││• D10✿ Cinnamoroll's Limited Fizzy Pop          ❀   10.25 DHS                  ★   24                 ││                                                           
                                                │╰──────────────────────────────────────────────────────────────────────────────────────────────────────||
                                                ╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯""")


# list of snacks
cinnamoroll_sweets = {
    "C1" : {"Name" : "Cinnamoroll's Blueberry Cheesecake", "Price" : 17, "Stock" : 20},
    "C2" : {"Name" : "Cinnamon Rolls Bites", "Price" : 15, "Stock" : 25},
    "C3" : {"Name" : "Cinnamoroll's Butter Cookies", "Price" : 28, "Stock" : 23},
    "C4" : {"Name" : "Chocolate Almond Coins", "Price" : 28, "Stock" : 20},
    "C5" : {"Name" : "Mocha's Chocolate Banana Muffin", "Price" : 21, "Stock" : 25},
    "C6" : {"Name" : "Mocha's Honey Bun Cake", "Price" : 19, "Stock" : 20},
    "C7" : {"Name" : "Chocolate Chip Coffee Cake", "Price" : 25, "Stock" : 23},
    "C8" : {"Name" : "Cinnamoroll's Steam Bun with Chicken Filling", "Price" : 18, "Stock" : 25},
    "C9" : {"Name" : "Cinnamoroll's Limited PEPERO Box", "Price" : 15, "Stock" : 25},
    "C10" : {"Name" :"Cinnamoroll Vanilla Mochi, 3 pieces", "Price" : 23.50, "Stock" : 25},
}

# list of drinks
cinnamoroll_drinks = {
    "D1": {"Name": "Pumpkin Spice Latte", "Price": 24, "Stock": 23},
    "D2": {"Name": "Hot Cocoa with Cinammoroll Marshmallows", "Price": 19, "Stock": 23},
    "D3": {"Name": "Chocolate Chai", "Price": 15, "Stock": 22},
    "D4": {"Name": "Deluxe Espresso", "Price": 19.50, "Stock": 24},
    "D5": {"Name": "Classic Boba Tea", "Price": 23.70, "Stock": 25},
    "D6": {"Name": "Cafè Machiatto", "Price": 28.50, "Stock": 23},
    "D7": {"Name": "White Chocolate Cappuccino", "Price": 17, "Stock": 25},
    "D8": {"Name": "Creamy Americano", "Price": 15, "Stock": 23},
    "D9": {"Name": "Classic Iced Coffee", "Price": 19, "Stock": 25},
    "D10":{"Name": "Cinnamoroll's Limited Fizzy Pop", "Price": 10.25, "Stock": 24}
}

Menus = {**cinnamoroll_sweets, **cinnamoroll_drinks}


print("                                                      Welcome to Cinnamoroll's Vending Machine. With all his favourite delights and drinks in one go!")
object = str(input("                                                                                 What would you like to purchase?: "))


# 
if object in Menus:
    selected_Menus = Menus[object]
    print("                                                                                ==========°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･°❀⋆.ೃ࿔*:･==========")

    print(f"                                                                                   You have purchased {selected_Menus['Name']}!")
    print("                                                                               ___________________________________________________")
    amount = selected_Menus['Price']
else:
    print("That's not available in Cinnamoroll's Vending Machine. Please enter and select items within the Menus.")


#
while amount > 0:
        payment = float(input(f"                                                                                       Please insert an amount ${amount:.2f}: "))
        if payment >= amount:
            change = payment - amount
            print(f"                                                                    Thank you for your purchase! Please come again next time! Your change is ${change:.2f}.")

            selected_Menus['Stock'] -= 1
            print(f"                                                                    There's currently {selected_Menus['Stock']} remaining stocks of {selected_Menus['Name']}.")
            break
        else:
            print("Insufficient payment. Please insert more.")
            amount -= payment

print("""                                                                                                       
                                                    ▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ █░█ 　 █░░█ █▀▀█ █░░█ 　 █▀▀ █▀▀█ █▀▀█ 　 █░░█ █▀▀ ░▀░ █▀▀▄ █▀▀▀ 　 █▀▀█ █░░█ █▀▀█ 
                                                    ░▒█░░ █▀▀█ █▄▄█ █░░█ █▀▄ 　 █▄▄█ █░░█ █░░█ 　 █▀▀ █░░█ █▄▄▀ 　 █░░█ ▀▀█ ▀█▀ █░░█ █░▀█ 　 █░░█ █░░█ █▄▄▀ 
                                                    ░▒█░░ ▀░░▀ ▀░░▀ ▀░░▀ ▀░▀ 　 ▄▄▄█ ▀▀▀▀ ░▀▀▀ 　 ▀░░ ▀▀▀▀ ▀░▀▀ 　 ░▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀ 　 ▀▀▀▀ ░▀▀▀ ▀░▀▀ 

                                                    █▀▀ █▀▀ █▀▀█ ▀█░█▀ ░▀░ █▀▀ █▀▀ 　 █▀▀█ █▀▀▄ █▀▀▄ 　 █▀▀ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀█ ░▀░ █▀▀▄ █▀▀▀ 　 █▀▀▄ █░░█ █ 
                                                    ▀▀█ █▀▀ █▄▄▀ ░█▄█░ ▀█▀ █░░ █▀▀ 　 █▄▄█ █░░█ █░░█ 　 ▀▀█ ░░█░░ █░░█ █░░█ █░░█ ▀█▀ █░░█ █░▀█ 　 █▀▀▄ █▄▄█ ▀ 
                                                    ▀▀▀ ▀▀▀ ▀░▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ▀▀▀ 　 ▀░░▀ ▀░░▀ ▀▀▀░ 　 ▀▀▀ ░░▀░░ ▀▀▀▀ █▀▀▀ █▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀▀ 　 ▀▀▀░ ▄▄▄█ ▄""")
#finishedd 