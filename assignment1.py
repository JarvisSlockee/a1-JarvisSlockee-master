"""
Replace the contents of this module docstring with your own details
Name: Jarvis Slockee
Date started: 24/04/20
GitHub URL:
"""

import csv

from operator import itemgetter

FILE_NAME = "songs.csv"
LEARNED = "l"
UNLEARNED = "u"
MENU = "Menu\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n>>>"


def main():
    """..."""
    print("Songs to Learn 1.0 - by Jarvis Slockee")
    songs_list = load_songs()
    user_input = input(MENU).upper()
    while user_input != "Q":
        if user_input == "L":
            display_songs_list(songs_list)
        elif user_input == "A":
            add_song(songs_list)
        elif user_input == "C":
            display_songs_list(songs_list)
            learned_song(songs_list)
        elif user_input == "":
            print("Input can not be blank")
        else:
            print("Invalid menu choice")
        user_input = input(MENU).upper()
    save_program(songs_list)


def display_songs_list(songs_list):
    songs_learned = 0
    songs_list.sort(key=itemgetter(3))
    songs_list.sort(key=itemgetter(2))
    for counter, songs in enumerate(songs_list):
        songs = [count for count in songs]
        if songs[3] == LEARNED:
            learned_status = ""
            songs_learned += 1
        else:
            learned_status = "*"
        print("{:2} {:>2}  {:<25} - {:<30} {:<40}".format(learned_status, counter+1, songs[0], songs[1], songs[2], songs[3]))
    print("{} songs learned, {} songs still to learn".format(len(songs_list) - songs_learned, len(songs_list)))


def load_songs():
    open_file = open(FILE_NAME, "r")
    csv_open_file = csv.reader(open_file, delimiter=",")
    song_list = list(csv_open_file)
    print("{} songs loaded from {}".format(len(song_list), FILE_NAME))
    open_file.close()
    return song_list


def add_song(songs_list):
    title = get_title_name("Title:")
    artist = get_artist_name("Artist:")
    year = get_year("Year:")
    songs_list.append([title, artist, year, UNLEARNED])
    print("{} by {} ({}) added to song list".format(title, artist, year))


def get_title_name(title_variable):
    title_name = input("{}".format(title_variable))
    while title_name == "":
        print("Input can not be blank")
        title_name = input("Title: ")
    return title_name


def get_artist_name(artist_variable):
    artist_name = input("{}".format(artist_variable))
    while artist_name == "":
        print("Input can not be blank")
        artist_name = input("Artist: ")
    return artist_name


def get_year(year_variable):
    valid_input = False
    while not valid_input:
        try:
            year = input("{}".format(year_variable))
            if int(year) <= 0:
                print("Numbr must be >= 0")
            elif year == "":
                print("Invalid input; enter a valid number")
            else:
                valid_input = True
                return year
        except ValueError:
            print("Please enter a valid number")


def learned_song(songs_list):
    learned_songs = [value[3] for value in songs_list]
    if UNLEARNED not in learned_songs:
        print("No more songs to learn!")
        return
    print("enter the number of a song you want to mark as learned")
    valid_input = False
    while not valid_input:
        try:
            learned_songs = int(input(">>>"))
            learned_songs -= 1
            if learned_songs == "":
                print("Input can not be blank")
            elif learned_songs >= len(songs_list):
                print("Invalid song number")
            elif learned_songs < 0:
                print("Number must be > 0")
            elif learned_songs >= 0 <= len(songs_list):
                list_to_change = songs_list[learned_songs]
                if LEARNED not in list_to_change[3]:
                    list_to_change[3] = LEARNED
                    songs_list[learned_songs] = list_to_change
                    print("{} by {} learned".format(list_to_change[0], list_to_change[1]))
                    return
                else:
                    print("That song is already learned")
                    valid_input = True
            else:
                print("Invalid input; enter a valid number")
        except ValueError:
            print("Invalid input; enter a valid number")


def save_program(songs_list):
    with open(FILE_NAME, "w", newline="") as write_file:
        write_csv = csv.writer(write_file, delimiter=",")
        write_csv.writerows(songs_list)
    print("{} songs saved to {}\n Have a nice day :)".format(len(songs_list), FILE_NAME))


if __name__ == '__main__':
    main()
