# 1. Create a class to represent Video Game or Movie Collection
# 2. Create a constructor method __init__() 
# 3. Create a list for the video games and movies each
# 4. Create a instance variable for the user's favorite movie and video game respectively
# 5. Create the following functions fot your class
# - A function to display all the movies
# - A function to display all the video games
# - A function to add a movie/video game
# - A function to remove a movie/video game
# - A function to select a favorite video game and or movie
# 6. Create a seperate tester.py file to test your code

class Collection:

    def __init__(self, movieList, gameList):
        self.movieList = []
        self.gameList = []
        self.favGame = ""
        self.favMovie = ""

        self.movieList = movieList
        self.gameList = gameList

    def AddGame(self, game):
        if game in self.gameList:
            print("Game is already in collection")
        else:
            self.gameList.append(game)


    def AddMovie(self, movie):
        if movie in self.movieList:
            print("Movie is already in colection")
        else:
            self.movieList.append(movie)

    def RemoveGame(self, game):
        if game not in self.gameList:
            self.gameList.remove(game)
        else:
            print("Game Not Found")

    def RemoveMovie(self, movie):
        if movie not in self.movieList:
            self.movieList.remove(movie)
        else:
            print("Movie Not Found")
    
    def DisplayGames(self):
        for game in self.gameList:
            print(game)

    def DisplayMovies(self):
        for movie in self.movieList:
            print(movie)

    def DisplayFavGame(self):
        print(f'Fav Game: {self.favGame}')

    def DisplayFavMovie(self):
        print(f'Fav Movie: {self.favMovie}')

    def DisplayCollection(self):
        self.DisplayGames()
        self.DisplayFavGame()
        self.DisplayMovies()
        self.DisplayFavMovie()

    def SetFavMovie(self, movie):
        if movie not in self.movieList:
            self.AddMovie(movie)
        self.favMovie = movie

    def SetFavGame(self, game):
        if game not in self.gameList:
            self.AddGame(game)
        self.favGame = game
        