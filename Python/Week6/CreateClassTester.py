import CreateClass

movies = ["Spider Man 3", "Free Guy", "Black Panther", "Creed 3"]
games = ["College Football 26", "Roblox", "Fortnite", "NBA 2K25"]

myCollection = CreateClass.Collection(movies, games)

myCollection.SetFavGame("College Football 26")
myCollection.SetFavMovie("Black Panther")
myCollection.DisplayCollection()