import os


### opens data, makes it writeable and other stuff
def lister(data):
    try:
        name = data.strip('.txt')
        with open (data) as person:
            for each_line in person:
                if each_line.find(',') != -1:
                     timez = each_line.strip().split(',')
                     print(f'Here is the data for {name}')
                     player_data = {
                     'Name' : timez.pop(0),
                     'Date of Birth' : timez.pop(0),
                     'Times'     : str(sorted(set([sanitize(t) for t in timez]))[0:3])}
                     print(player_data)
                     return(player_data)

    except IOError as ioerr:
        print('File Error: ' + str(ioerr))
        return(None)

#takes a given string and if that string has colon or a hyphen
#the splitter parameter will be set to eiter ':' or '-' said string
#will then be split up via the split function and then recombined
#replacing the split paprameter with a period
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

#iterates over a iven list and runs sanitize function on each item
def iter_clean(lyst):
    nu_lyst = [ sanitize(item) for item in lyst ]
    return(nu_lyst)

#prints sorted and cleaned lists of data using the methods above

mikey = lister('mikey2.txt')
sarah = lister('sarah2.txt')
james = lister('james2.txt')
julie = lister('julie2.txt')



#Prints all 4 lists with no duplicates
#print('James Unique List:')
#uni_jam = sorted(set(iter_clean(james)))
#print(uni_jam[0:3])
#print('Mikeys Unique List:')
#uni_mik = sorted(set(iter_clean(mikey)))
#print(uni_jam[0:3])
#print('Sarahs Unique List:')
#uni_sar = sorted(set(iter_clean(sarah)))
#print(uni_sar[0:3])
#print('Julies Unique List:')
#uni_jul = sorted(set(iter_clean(julie)))
#print(uni_jul[0:3])


#print(player_data['Name'] + "'s fastest times are: " +
#        str(sorted(set(iter_clean(james)))[0:3]))
