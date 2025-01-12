import string

s = r"""\
Op 10 mei 1940 bleef het versperde vliegveld verschoond van een Duits bombardement. Maar de Luftwaffe nam het vliegveld spoedig na de Nederlandse overgave in gebruik. De Duitsers herstelden het vliegveld en breidden het uit. Het vliegveld huisvestte grote, onbeschadigde Nederlandse hangars en had een gunstige bodemgesteldheid. Hierdoor was Soesterberg uitermate geschikt voor het stationeren van zwaardere toestellen.
Toch beten kleine jachtvliegtuigen van het type Bf 109 het spits af. Rond juni 1940 streken namelijk een aantal Bf 109’s neer op de voormalige ‘Bakermat’. Zij waren van de Gruppenstab van de I./JG 54 en de III./JG 54. Maar begin juli 1940 vertrokken zij alweer.
Daarna waren er vooral bommenwerpers op Soesterberg. Het vliegveld werd eind juli de thuisbasis van het KG 4 en het I./KG 4. Beide eenheden hadden He 111’s. Zij bleven tot eind juni 1941 op het vliegveld. Van hieruit namen ze deel aan de slag om Engeland en de ‘Blitz’. Begin 1941 kregen zij nog versterking van de heropgerichte III./KG 4. De bommenwerpers van het KG 4 bombardeerden onder meer Britse steden. Ook legden zij mijnen in de Britse kustwateren en vielen de geallieerde koopvaardijvaart aan.
Na het vertrek van het KG 4 werd het allerminst stil op Soesterberg. Vanaf augustus was het vliegveld de thuisbasis van de Geschwaderstab van het KG 40 en de III./KG 40.
In december 1941 arriveerden bovendien ook nog de bommenwerpers van het Kampfgeschwader 2. Alle Gruppen van dit Geschwader waren tot september 1944 voor kortere of langere tijd op Soesterberg gestationeerd.
Dit geldt ook voor de Geswaderstab. De oorlogsgeschiedenis van deze eenheid is onlosmakelijk verbonden met die van het vliegveld. Tussen eind 1941 en 1944 voerden de Do 217’s van het KG 2 talloze bombardementen uit vanaf Soesterberg. Dit deden zij op scheepsdoelen en op steden en havens in Groot-Brittannië. Zij incasseerden hierbij zware verliezen."""


# clean up
# s = s.lower().replace('.', '').replace(',', '').replace('(', '').replace(')', '')

# or
# s = s.lower()
# for c in string.punctuation:
#     s = s.replace(c, '')

# or
# s = s.lower().translate(str.maketrans('', '', r'\'"‘’.,(){}[]/\|#&?!'))

# or
import string
s = s.lower().translate(str.maketrans('', '', string.punctuation + '‘’'))

# or
# import re
# s = re.sub(r'[^a-zA-Z0-9 ]', '', s).lower()


words = s.split()

unique_words = set(words)

d = {}
for word in unique_words:
    d[word] = words.count(word)

for word, n in sorted(d.items()):
    print(f'{word:30} {n:3}', n * '*')













# or
# d = {word: words.count(word) for word in set(words)}

# from operator import itemgetter
# for word, n in sorted(d.items(), key = itemgetter(1, 0), reverse = True):
#    print(f'{word:20}: {n:3}')

# for word, n in sorted(d.items(), key = lambda item: item[1], reverse=True):
#    print(f'{word:20}: {n:3} {"*" * n}')

# def get_values(item):
#     return item[1]
#
# for word, n in sorted(d.items(), key=get_values, reverse=True):
#     # print(word, n)
#     # print('%-25s: %3d' % (word, n))
#     print(f'{word:<25}: {n:3}')
#     # or
#     print('%-15s: %3d %s' % (word, n, '*' * n))
