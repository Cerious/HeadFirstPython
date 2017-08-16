import pickle


man = []
other = []



try:

    with open('sketch1.txt') as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(':', 1)
                line_spoken.replace(" ", "")
                if role == 'Man':
                    man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)
                print(role, end='')
                print(' said: ', end='')
                print(line_spoken, end='')
            except ValueError:
                pass

    data.close()

except IOError:
    print('The data file is missing!')


try:

    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man, man_file)
    with open('other_man.txt', 'wb') as other_man:
        pickle.dump(other, other_man)






except IOError:
    print("The data file is missing...")

finally:
    man_file.close()
    other_man.close()
