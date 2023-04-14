import imdb
ia = imdb.Cinemagoer()

movies = ia.search_movie('avatar')
#print(movies)
for i in movies:
    print(i)
    #print(type(i))
mymovie = input("Scrivi il nome esatto del film che vuoi vedere: ")
print(mymovie)
mymovieID = ""
for i in movies:
    currentmovie = i
    if mymovie == currentmovie:
        mymovieID = i.movieID
print(mymovieID)
print(currentmovie)
