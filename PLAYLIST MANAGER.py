import csv

FILENAME = "playlist.csv"
playlist = []

# Load playlist safely without using os
def load_playlist():
    try:
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    playlist.append(row[0])
    except FileNotFoundError:
        # If file does not exist, do nothing
        pass

def save_playlist():
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        for song in playlist:
            writer.writerow([song])

def show_menu():
    print("\n--- Playlist Manager ---")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Search Song")
    print("5. Exit")

def add_song():
    song = input("Enter song name to add: ")
    playlist.append(song)
    save_playlist()
    print(f"'{song}' added to playlist.")

def remove_song():
    song = input("Enter song name to remove: ")
    if song in playlist:
        playlist.remove(song)
        save_playlist()
        print(f"'{song}' removed.")
    else:
        print("Song not found.")

def view_playlist():
    if playlist:
        print("\nYour Playlist:")
        for i, song in enumerate(playlist, 1):
            print(f"{i}. {song}")
    else:
        print("Playlist is empty.")

def search_song():
    song = input("Enter song to search: ")
    if song in playlist:
        print(f"'{song}' is in the playlist.")
    else:
        print("Song not found.")

# Main Program
load_playlist()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_song()
    elif choice == "2":
        remove_song()
    elif choice == "3":
        view_playlist()
    elif choice == "4":
        search_song()
    elif choice == "5":
        print("Exiting Playlist Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")
