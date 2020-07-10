people = ["Abe", "Bill", "Charles", "Dolly", "Evelyn", "Frank", "Gunther"]

# comp for names that start with D
dcomp = [person for person in people if person[0] == 'D'] 
# or
# dcomp = [person for person in people if person.startswith('D')]

print(dcomp)
# comp for names that end in Y
ycomp = [person for person in people if person[len(person)-1] == 'y']
print(ycomp)
# comp for names that start with B through D
bdcomp = [person for person in people if person[0]=='B' or person[0]=='C' or person[0]=='D']
print(bdcomp)
# comp for names but in uppercase
upcomp = [person.upper() for person in people]
print(upcomp)