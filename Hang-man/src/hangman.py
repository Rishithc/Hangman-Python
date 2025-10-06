# ===============================
# Imports
# ===============================
import turtle
import random
import os
import time

# ===============================
# Utility Functions
# ===============================
def clear():
    """Clears the console screen in a cross-platform way."""
    os.system("cls" if os.name == "nt" else "clear")

# ===============================
# Themed Modules
# ===============================
Movie = [
    "Avatar", "Puss in Boots", "KungFu Panda", "Avengers Endgame", "The Godfather",
    "The Lord of the Rings", "Titanic", "Star Wars", "The Outsiders", "Home Alone",
    "TopGun Maverick", "Jurassic World", "Lion King", "Finding Nemo", "Frozen", "Shrek",
    "Extra Terrestrial", "Toy Story", "Jumanji", "Harry Potter", "Aladdin", "Fast and Furious",
    "Inside Out", "The Matrix", "Casablanca", "The Ten Commandments", "Back to the Future",
    "Gone with the Wind", "Indiana Jones", "Wizard of Oz", "Beauty and the Beast",
    "Transformers", "Terminator", "The Sound of Music"
]

Tv_show = [
    "Breaking Bad", "The Walking Dead", "Better Call Saul", "Game of Thrones", "The Office",
    "Peaky Blinders", "Modern Family", "Family Guy", "The Simpsons", "The Big Bang Theory",
    "Stranger Things", "13 Reasons Why", "Greys Anatomy", "The Flash", "Umbrella Academy",
    "South Park", "Bunk'd", "Henry Danger", "Homeland", "Lost", "Fear the Walking Dead",
    "New Girl", "Gotham", "How I Met Your Mother", "Narcos", "Teen Wolf", "Supernatural",
    "American Horror Story", "Sherlock"
]

Marvel_char = [
    "Thor", "Hulk", "Spider Man", "Iron Man", "Wolverine", "Antman", "Wasp", "Loki",
    "Doctor Strange", "Thanos", "Black Widow", "Venom", "Rocket Racoon", "Starlord",
    "Punisher", "Gamora", "Groot", "Nick Fury", "Miles Morales", "Clint Barton", "X-23",
    "Carol Danvers", "Wade Wilson", "Deadpool", "Namor", "Spiderwoman", "Cable",
    "Human Torch", "Bucky Barnes", "Odin", "Vision", "Daisy Johnson", "Professor X",
    "Reed Richards", "Scarlet Witch", "Apocalypse"
]

VidGame_Fran = [
    "Fifa", "Madden", "Elden Ring", "Red Dead Redemption", "Grand Theft Auto",
    "Subway Surfer", "Minecraft", "Fortnite", "Tetris", "Overwatch", "Assassins Creed",
    "Rocket League", "Apex Legends", "Rainbow Six Siege", "Call of Duty", "Forza",
    "Legend of Zelda", "Pacman", "Wii Sports", "Skyrim", "Pokemon Go", "Borderlands",
    "Mario Kart", "Counter Strike", "Playerunknowns Battleground", "League of Legends",
    "Roblox", "Warcraft", "Sim City", "Clash Royale", "Temple Run", "Animal Crossing"
]

Athlete = [
    "Cristiano Ronaldo", "Lionel Messi", "Michael Jordan", "LeBron James", "Muhammad Ali",
    "Mike Tyson", "Usain Bolt", "Michael Phelps", "Roger Federer", "Novak Djokovic",
    "Kobe Bryant", "Neymar Jr", "Tom Brady", "Gareth Bale", "Marcelo", "Marcus Rashford",
    "Erling Haaland", "Bill Russel", "Babe Ruth", "Spencer Strider", "Chipper Jones",
    "Bo Jackson", "Wayne Gretzky", "Wilt Chamberlain", "Jackie Robinson", "Jim Thorpe",
    "Walter Payton"
]

# ===============================
# Hangman Drawing
# ===============================
def hangman():
    hangstand = turtle.Turtle()
    hangstand2 = turtle.Turtle()
    hangstand.color("#241c20")
    hangstand.hideturtle()
    hangstand2.hideturtle()

    hangstand.pensize(5)
    hangstand.penup()
    hangstand.setpos(-20, -208)
    hangstand.pendown()
    hangstand.forward(50)
    hangstand.left(180)
    hangstand.forward(25)
    hangstand.right(90)
    hangstand.forward(100)
    hangstand.right(90)
    hangstand.forward(65)

    hangstand2.color("#241c20")
    hangstand2.pensize(5)
    hangstand2.penup()
    hangstand2.setpos(5, -135)
    hangstand2.pendown()
    hangstand2.left(45)
    hangstand2.forward(35)
    hangstand2.hideturtle()

    hangstand.pensize(3)
    hangstand.right(90)
    hangstand.forward(22)


def hanged_man(num):
    """Draws parts of the hangman depending on lives left."""
    hanged = turtle.Turtle()
    hanged.hideturtle()
    hanged.pensize(4)
    hanged.penup()
    hanged.setpos(70, -152)
    hanged.pendown()

    if num == 0:
        hanged.clear()
    elif num == 4:
        hanged.circle(10)
    elif num == 3:
        hanged.right(90)
        hanged.forward(30)
    elif num == 2:
        hanged.left(225)
        hanged.forward(30)
        hanged.backward(30)
        hanged.right(270)
        hanged.forward(30)
    elif num == 1:
        hanged.right(90)
        hanged.forward(30)
        hanged.right(45)
        hanged.forward(30)
        hanged.backward(30)
        hanged.left(90)
        hanged.forward(30)

# ===============================
# Game Logic
# ===============================
def menu():
    background.addshape(title_image_path)
    title.shape(title_image_path)
    title.penup()
    title.setpos(40, 0)
    title.pendown()

    User_play = input("Which gamemode would you like to play? ").capitalize()
    clear()
    title.hideturtle()
    hangman()

    if User_play == "Singleplayer":
        u1 = input(
            "Modules: Movie, Tv Show, Marvel Character, Video Game, Athlete.\n"
            "Enter the module you wish to use: "
        )
        time_choice = input("Do you want a timed challenge? (Y/N): ").upper()
        game_ops_S(u1, time_choice)

    elif User_play == "Multiplayer":
        u2 = input("Player 1, enter a word for player 2 to guess: ")
        time_choice2 = input("Do you want a timed challenge? (Y/N): ").upper()
        clear()
        game_ops_M(u2, time_choice2)
    else:
        print("Invalid Input!")
        menu()


def game_ops_S(User, times):
    """Singleplayer mode."""
    if times == "Y":
        time_limit = int(input("Enter the amount of time (seconds): "))

    User = User.capitalize()
    module_dict = {
        "Movie": Movie,
        "Tv show": Tv_show,
        "Marvel character": Marvel_char,
        "Video game": VidGame_Fran,
        "Athlete": Athlete
    }

    module = module_dict.get(User)
    if not module:
        print("Invalid module! Returning to menu.")
        menu()
        return

    word = random.choice(module)
    word_template = [" " if x == " " else "_" for x in word]
    print(*word_template, sep="")

    user_lives = 5
    start = time.time() if times == "Y" else None

    while "_" in word_template and user_lives > 0:
        if times == "Y":
            time_spent = time.time() - start
            time_limit -= time_spent
            if time_limit <= 0:
                print("Time over! You lost.")
                print("The word was:", word)
                break
            print(f"Time left: {int(time_limit)} seconds")
            start = time.time()

        user_guess = input("Enter letter: ")[0]
        checkpoint, save_life = 0, 0

        for x in word:
            if user_guess.lower() == x.lower():
                word_template[checkpoint] = x
                save_life = 1
            checkpoint += 1

        if not save_life:
            user_lives -= 1
            hanged_man(user_lives)

        print(*word_template, sep="")

    if "_" not in word_template:
        print("You won!")
    elif user_lives <= 0:
        print("You lose! The word was:", word)

    cont_yn = input("Play again? (Y/N): ").lower()
    if cont_yn == 'y':
        clear()
        background.reset()
        hangman()
        U1 = input("Enter module: ")
        Time_Choice = input("Timed challenge? (Y/N): ").upper()
        game_ops_S(U1, Time_Choice)
    else:
        menu()


def game_ops_M(user, mul_time):
    """Multiplayer mode."""
    if mul_time == "Y":
        time_limit2 = int(input("Enter time limit (seconds): "))

    word_template = [" " if x == " " else "_" for x in user]
    print(*word_template, sep="")

    user_lives = 5
    start = time.time() if mul_time == "Y" else None

    while "_" in word_template and user_lives > 0:
        if mul_time == "Y":
            time_spent2 = time.time() - start
            time_limit2 -= time_spent2
            if time_limit2 <= 0:
                print("Time over! You lost.")
                print("The word was:", user)
                break
            print(f"Time left: {int(time_limit2)} seconds")
            start = time.time()

        user_guess = input("Enter letter: ")[0]
        checkpoint, save_life = 0, 0

        for x in user:
            if user_guess.lower() == x.lower():
                word_template[checkpoint] = x
                save_life = 1
            checkpoint += 1

        if not save_life:
            user_lives -= 1
            hanged_man(user_lives)

        print(*word_template, sep="")

    if "_" not in word_template:
        print("You won!")
    elif user_lives <= 0:
        print("You lose! The word was:", user)

    cont_yn = input("Play again? (Y/N): ").lower()
    if cont_yn == 'y':
        clear()
        background.reset()
        hangman()
        U2 = input("Enter a word for the other player: ")
        time_choice2 = input("Timed challenge? (Y/N): ").upper()
        game_ops_M(U2, time_choice2)
    else:
        menu()

# ===============================
# Image Paths
# ===============================
# Get the folder where this script is located
current_dir = os.path.dirname(__file__)

# Construct full paths to the images
title_image_path = os.path.join(current_dir, "../Images/Titlee.gif")
background_image_path = os.path.join(current_dir, "../Images/Evening.png")

# Verify that files exist
if not os.path.isfile(title_image_path):
    raise FileNotFoundError(f"Title image not found: {title_image_path}")
if not os.path.isfile(background_image_path):
    raise FileNotFoundError(f"Background image not found: {background_image_path}")


# ===============================
# Homepage
# ===============================
background = turtle.Screen()
background.bgpic(background_image_path)
background.title("The Hangman Game")

title = turtle.Turtle()
background.addshape(title_image_path)
title.shape(title_image_path)
title.penup()
title.setpos(-100, 0)
title.pendown()

print("Welcome, player!")
print("The game is simple: guess the hidden word before you lose all 5 lives.")
print()
print("Gamemodes:")
print(" - Singleplayer: Choose from 5 themed modules (Movie, TV Show, etc.)")
print(" - Multiplayer: Player 1 enters a word; Player 2 guesses.")
print()
menu()
