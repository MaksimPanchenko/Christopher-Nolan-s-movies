print("Christopher Nolan's movies")

class Movie:

    def __init__(self, name):
        self.name = name       #название фильма
        self.rating = 1.0      #рейтинг фильма
        self.length = 0.00     #длина фильма

    def display_info(self):
            print(f'Title: {self.name} Rating: {self.rating}  Length:  {self.length}')



following = Movie("Following")
following.rating = 7.5
following.length = 1.10
following.display_info()


memento = Movie("Memento")
memento.rating = 8.4
memento.length = 1.53
memento.display_info()


insomnia = Movie("Insomnia")
insomnia.rating = 7.2
insomnia.length = 1.58
insomnia.display_info()


batman_begins = Movie("Batman begins")
batman_begins.rating = 8.2
batman_begins.length = 2.20
batman_begins.display_info()


the_prestige = Movie("The Prestige")
the_prestige.rating = 8.5
the_prestige.length = 2.10
the_prestige.display_info()


the_dark_knight = Movie("The Dark Knight")
the_dark_knight.rating = 9.0
the_dark_knight.length = 2.32
the_dark_knight.display_info()


inception = Movie("Inception")
inception.rating = 8.8
inception.length = 2.28
inception.display_info()


the_dark_knight_rises = Movie("The Dark Knight Rises")
the_dark_knight_rises.rating = 8.4
the_dark_knight_rises.length = 2.45
the_dark_knight_rises.display_info()


interstellar = Movie("Interstellar")
interstellar.rating = 8.6
interstellar.length = 2.49
interstellar.display_info()


dunkirk = Movie("Dunkirk")
dunkirk.rating = 7.8
dunkirk.length = 1.46
dunkirk.display_info()


tenet = Movie("Tenet")
tenet.rating = 7.5
tenet.length = 2.30
tenet.display_info()




