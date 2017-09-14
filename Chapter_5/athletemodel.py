import pickle
from athlete import Athlete

def lister(data):
    try:
        name = data.strip('.txt')
        with open (data) as person:
            for each_line in person:
                if each_line.find(',') != -1:
                     timez = each_line.strip().split(',')
                     #print(f'Here is the data for {name}')
                     player_data = Athlete(timez.pop(0),
                            timez.pop(0), timez)
                     #print(player_data)
                     return(player_data)

    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)


def put_to_store(lyst):
    all_athletes = {}
    for item in lyst:
        all_athletes[lister(item).name] = lister(item)

    try:
        with open('athletes,pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)

    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store):' + str(ioerr))
    return(all_athletes)
