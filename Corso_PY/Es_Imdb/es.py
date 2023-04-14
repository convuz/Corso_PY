import imdb
ia = imdb.Cinemagoer()

movies_id = ['8012', '12929', '6768', '25214882', '0499549']

for i in movies_id:
    movie = ia.get_movie(i)
    print(type(movie["year"]))