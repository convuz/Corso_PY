import imdb
ia = imdb.Cinemagoer()

#titolo = Avatar: The Way of Water
#ID = 1630029

movie = ia.get_movie("1630029")
dict1 = {}
charactercode = ""
character = ""
role = ""
actors = movie["cast"]
for i in range(len(actors)):
    charactercode = movie["cast"][i]
    character = charactercode["name"]
    role = charactercode.currentRole.data["name"]
    dict1.update({character: role})

print(dict1)
print(type(movie["year"]))

movies_id = ['8012', '12929', '6768', '25214882', '0499549']
    

