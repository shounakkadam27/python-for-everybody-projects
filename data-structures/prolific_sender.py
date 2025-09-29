name = input('Enter file:')
if len(name) < 1: name = 'mbox-short.txt'
handle = open(name)

many = dict()
for line in handle:
    line = line.strip()
    if line.startswith('From '):
        line = line.split()
        email = line[1]

        many[email] = many.get(email, 0) + 1

largest = None
bigword = None
for cle, valeur in many.items():
    if largest is None or valeur > largest:
        largest = valeur
        bigword = cle
print(bigword, largest)