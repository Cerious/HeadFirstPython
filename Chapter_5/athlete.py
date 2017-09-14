class Athlete(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top_three(self):
        return(sorted(set([sanitize(item) for item in self]))[0:3])

    def add_time(self, time):
        self.times.append(time)

    def add_times(self, times):
        for i in times:
            self.times.append(i)



def lister(data):
    try:
        name = data.strip('.txt')
        with open (data) as person:
            for each_line in person:
                if each_line.find(',') != -1:
                     timez = each_line.strip().split(',')
                     print(f'Here is the data for {name}')
                     player_data = Athlete(timez.pop(0),
                            timez.pop(0), timez)
                     #print(player_data)
                     return(player_data)

    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def iter_clean(lyst):
    nu_lyst = [ sanitize(item) for item in lyst ]
    return(nu_lyst)

james = lister('james2.txt')
print(james.name + "'s fastest times are: " +
        str(james.top_three()))
james.append('1.13')
james.extend(['1.21','1.33'])
print(lister('james2.txt').name)
