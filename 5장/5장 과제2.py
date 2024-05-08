# 20244021, 컴퓨터공학과, 김성준
print("20244021, 컴퓨터공학과, 김성준")


def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    for line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'],
         s['board'], s['age']) = line.split(";")
        if id2find == int(s['id']):
            surfers_f.close()
            return (s)
    surfers_f.close()
    return ({})


lookup_id = 1
while lookup_id != -1:
    lookup_id = int(input("Enter the id of the surfer: (Exit code = -1)"))
    surfer = find_details(lookup_id)
    if surfer:
        print("ID:         " + surfer['id'])
        print("Name:       " + surfer['name'])
        print("Country:    " + surfer['country'])
        print("Average:    " + surfer['average'])
        print("Board type: " + surfer['board'])
        print("Age:        " + surfer['age'])
print("Bye!")
