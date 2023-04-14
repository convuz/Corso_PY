from retrieve_cast import retrieve_cast
from imdb import Cinemagoer

ia = Cinemagoer()

movies_id = ['8012', '12929', '6768', '25214882', '0499549']

'''
# Codice di esempio di utilizzo della funzione retrieve_cast
movies_cast = {}

for movie_id in movies_id:
	print(movie_id)
	movies_cast[movie_id] = retrieve_cast(movie_id, ia)

print(movies_cast)
'''


'''
# Utilizzando la funzione già pronta retrieve_cast, creare una funzione che:
1. per ogni film della lista movies_id, fornisca il numero totale di attori
2. aggiungere un parametro che permetta di scegliere un film specifico usando il suo id. La funzione restituisce il numero totale di attori solo per il film scelto
	- se il film scelto non è presente nella lista, la funzione restituisce un messaggio e si interrompe
3. aggiungere un parametro booleano per restituire un dizionario con i soli nomi degli attori in uppercase
4.[BONUS] aggiungere un parametro numerico per restituire solo i film usciti dopo l'anno indicato dal parametro
'''


def countattori(movies_id, one_film=None, uppercase=False, year_release:str=None):
    dict1 = {}
    if uppercase == False:
        if one_film is None:
            for movie_id in movies_id:
#                if int(movie_id["year"]) > int(year_release):
                    dict1.update({movie_id:len(retrieve_cast(movie_id, ia))})
                else:
                    print("il film: ",movie_id,"è uscito prima del ",year_release)
            return dict1
        else:
            if one_film in movies_id:
#                if int(movie_id["year"]) > int(year_release):
                    dict1.update({one_film:len(retrieve_cast(one_film, ia))})
                    return dict1
                else:
                    print("il film: ",movie_id,"è uscito prima del ",year_release)
            else:
                print("L'Id scelto non è nella lista")
    else:
        if one_film is None:
            for movie_id in movies_id:
#                if int(movie_id["year"]) > int(year_release):
                    dict2 = retrieve_cast(movie_id, ia)
                    for i in dict2.keys():
                        dict1.update({i.upper():dict2[i]})
                    return dict1
                else:
                    print("il film: ",movie_id,"è uscito prima del ",year_release)
        else:
            if one_film in movies_id:
#                if int(movie_id["year"]) > int(year_release):
                    dict2 = retrieve_cast(one_film, ia)
                    for i in dict2.keys():
                        dict1.update({i.upper():dict2[i]})
                    return dict1
                else:
                    print("il film: ",movie_id,"è uscito prima del ",year_release)                  
            else:
                print("L'Id scelto non è nella lista")



print(movies_id)
one_film = None
#one_film = '0499549'
uppercase = False #true per solo uppercase, false per utilizzo normale della funzione
year_release = "2000"
dict1 = countattori(movies_id, one_film, uppercase, year_release)
print(dict1)
