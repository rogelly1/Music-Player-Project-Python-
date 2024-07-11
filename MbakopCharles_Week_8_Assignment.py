import time
from datetime import datetime
import random

# This program is a simple music player that lets users add and play songs, adjust volume, and check the date/time.

def displayName():
    # Displays my name, class, and the date for submission purposes.
    print("Charles Mbakop")
    print("CMSC 105 7380")
    print("05/03/2024")

def displayDateTime():
    # Shows the current date and time in a specified format.
    currentDateTime = datetime.now()
    formattedDate = currentDateTime.strftime("%#d %b, %Y")
    formattedTime = currentDateTime.strftime("%A, %H:%M:%S")
    print("\nToday's date: ", formattedDate)
    print("Current time: ", formattedTime)

def PlayOneSong(song, author, songtime):
    import time
    #This function will simulate playing one song.
    #It will loop and display "--- playing song: xxx" based on the vlaue of songtime
    #Input(Args):   song - name of one song
    #               author - author/singer of the song 
    #               songtime - length of song in mins (1 to 6)
    #Return:        None
	
    #Caclulate delay time an loop.
	
    
    delay = .5			#delay time (secs) between print statements
    loops = songtime    	#simulate songtime by looping 

    #Validate songtime input value, force to 6 if invalid
    if (loops < 1 or loops > 6):
        loops = 6
        
    loopcnt = 1
    while (loopcnt <= loops):
        print("--- playing song:", song)
        print("\t\t\t --- by ...:", author)    
        time.sleep(delay)
        loopcnt = loopcnt + 1
        
#testing/execute ... This is not part of the code.
#song = "Yellow Submarine"
#author = "Beatles"
#songtime = 6

#PlayOneSong(song, author, songtime)       

def addSongs(songs, authors):
    # Adds new songs and authors to their respective lists after user input.
    song = input("Enter the name of the song: ")
    author = input("Enter the author/singer of the song: ")
    songs.append(song)
    authors.append(author)

def displaySongs(songs, authors):
    # Lists all songs and their corresponding authors.
    for song, author in zip(songs, authors):
        print(f"{song} by {author}")

def playAllSongs(songs, authors):
    # Shuffles and plays all songs, asking for user input on play duration.
    songAuthorPairs = list(zip(songs, authors))
    random.shuffle(songAuthorPairs)
    for song, author in songAuthorPairs:
        while True:
            try:
                songTime = int(input(f"Enter playtime for {song} by {author} (1-6 mins): "))
                if 1 <= songTime <= 6:
                    break
                else:
                    print("Invalid input. Please enter a value between 1 and 6 minutes.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        PlayOneSong(song, author, songTime)

def adjustVolume(volume):
    # Adjusts the volume based on user input, with visual feedback.
    print("\nCurrent volume:", volume)
    print("*" * (volume * 2))
    while True:
        try:
            newVolume = int(input("Enter new volume (0-9, -1 to exit): "))
            if newVolume == -1:
                break
            elif 0 <= newVolume <= 9:
                volume = newVolume
                print("New volume set:", volume)
                print("*" * (volume * 2))
            else:
                print("Invalid volume. Please enter a value between 0 and 9.")
        except ValueError:
            print("Please enter a valid integer.")
    return volume

def getMenuOption():
    # Displays a menu and handles user selection, ensuring valid input.
    menuText = """
    a) Add songs and authors
    b) Display all songs
    c) Play all songs
    d) Display date/time
    e) Adjust volume
    f) Quit
    """
    print(menuText)
    options = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6'}
    while True:
        option = input("Select an option (a-f): ").strip().lower()
        if option in options:
            return options[option]
        print("Invalid option. Please choose a valid option.")

def main():
    # Initializes lists for songs and authors, handles user interactions.
    songs = []
    authors = []
    volume = 3  # Initial volume setting
    while True:
        option = getMenuOption()
        if option == '1':
            addSongs(songs, authors)
        elif option == '2':
            displaySongs(songs, authors)
        elif option == '3':
            playAllSongs(songs, authors)
        elif option == '4':
            displayDateTime()
        elif option == '5':
            volume = adjustVolume(volume)
        elif option == '6':
            print("Exiting program.")
            displayName()
            break

if __name__ == "__main__":
    main()
