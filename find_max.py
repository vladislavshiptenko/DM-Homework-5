from graph import data

def find_max(data):
    maxx = (0, '')
    for i in data:
        maxx = max(maxx, (len(data[i]), i))
    print(maxx)

find_max(data)
