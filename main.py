from ClassMelodyNote import MelodyNotebook
from ClassSong import Song
from ClassNote import Note
from random import choice

notebook = MelodyNotebook()

for i in range(2):
    new_song = Song()
    for j in range(50):
        new_song << Note(choice(["c", "d", "e", "f", "g", "a", "h"]), choice(["Major", "Minor"]))
    with notebook:
        notebook << new_song
    new_song = Song()

new_song = Song()
for j in range(50):
    new_song << Note(choice(["c", "d", "e", "f", "g", "a", "h"]), choice(["Major", "Minor"]))
with notebook:
    notebook = notebook[1] + new_song

with notebook:
    notebook[0].play()
    print("Сравнение нот " + notebook[0][0].note_sign + " " + notebook[0][1].note_sign)
    print(notebook[0][0] < notebook[0][1])
    print(notebook[0][0] <= notebook[0][1])
    print(notebook[0][0] > notebook[0][1])
    print(notebook[0][0] >= notebook[0][1])
    print(notebook[0][0] == notebook[0][1])
    print("Сравнение песен")
    print(notebook[0] < notebook[1])
    print(notebook[0] <= notebook[1])
    print(notebook[0] > notebook[1])
    print(notebook[0] >= notebook[1])
    print(notebook[0] == notebook[1])
    print("Итерация по песне")
    for i in notebook[0].into_pages(10):
        print(i.notes)
    notebook[0].change_mood("Major",10,20)
    notebook[0].play()
