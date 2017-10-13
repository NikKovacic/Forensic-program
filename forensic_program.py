characteristics = {
    'hair': {
        'black': 'CCAGCAATCGC',
        'brown': 'GCCAGTGCCG',
        'blonde': 'TTAGCTATCGC'
    },
    'face': {
        'square': 'GCCACGG',
        'round': 'ACCACAA',
        'oval': 'AGGCCTCA'
    },
    'eyes': {
        'blue': 'TTGTGGTGGC',
        'green': 'GGGAGGTGGC',
        'brown': 'AAGTAGTGAC'
    },
    'gender': {
        'female': 'TGAAGGACCTTC',
        'male': 'TGCAGGAACTTC'
    },
    'race': {
        'white': 'AAAACCTCA',
        'black': 'CGACTACAG',
        'asian': 'CGCGGGCCG'
    }
}

suspects = {
    'Eva': {
        'gender': 'female',
        'race': 'white',
        'hair': 'blonde',
        'eyes': 'blue',
        'face': 'oval'
    },
    'Larisa': {
        'gender': 'female',
        'race': 'white',
        'hair': 'brown',
        'eyes': 'brown',
        'face': 'oval'
    },
    'Matej': {
        'gender': 'male',
        'race': 'white',
        'hair': 'black',
        'eyes': 'blue',
        'face': 'oval'
    },
    'Miha': {
        'gender': 'male',
        'race': 'white',
        'hair': 'brown',
        'eyes': 'green',
        'face': 'square'
    }
}

dna_file = open('dna.txt', 'r')
dna = dna_file.read()
dna_file.close()

suspect = {}

# iteritems() function will iterate trough the characteristics data
for key, value in characteristics.iteritems():
    for characteristics, sequence in value.iteritems():
        if dna.find(sequence) != -1:
            suspect[key] = characteristics
            break

name = ''

for n, value in suspects.iteritems():
    current_name = ''

    for k, v in value.iteritems():
        if suspect[k] == v:
            current_name = n
        else:
            current_name = ''
            break

    if current_name:
        name = current_name
        break

print "The person who ate the ice cream is %s." % name
