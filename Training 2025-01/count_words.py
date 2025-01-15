import string

s = """Ten noorden van het dorp Soesterberg lag tot het begin van de twintigste eeuw een heideveld; dit heideveld lag op een nagenoeg vlakke waaier van zand en grind die uitgespoeld was tijdens het Saalien, de voorlaatste ijstijd. Deze vlakte wordt door geomorfologen wel aangeduid als de sandr van Soesterberg. In 1910 vroegen enkele ondernemers, Lugard en Verwey, toestemming om een deel van die heide te mogen gebruiken als start- en landingsplaats voor hun bedrijf voor vliegtuigen. Na bijna twee jaar ging hun onderneming failliet. De vliegheide bleef in gebruik, onder andere door enkele officieren van de Landmacht die door Lugard en Verwey waren opgeleid als vliegenier. In 1913 werd de Luchtvaartafdeeling van de Koninklijke Landmacht opgericht. Het vliegveld werd vliegbasis Soesterberg. De basis trok veel belangstelling en het dorp groeide snel. In de Eerste Wereldoorlog werden in het 'Kamp van Zeist' enkele tienduizenden Belgen opgevangen die vanwege de oorlog uit hun land waren gevlucht.

Na de Tweede Wereldoorlog werd de vliegbasis Soesterberg aangewezen als NAVO-basis, vanaf 1954 werden er Amerikaanse militairen gestationeerd, waarbij het Amerikaanse deel bekend stond als 'Camp New Amsterdam'. Voor hen werd een eigen woonwijk, Apollo genaamd, gebouwd. In de jaren tachtig waren er regelmatig vredesacties nabij de vliegbasis tegen de kernbewapening, zo werd de basis in 1984 door circa 5000 demonstranten symbolisch omsingeld. Na het einde van de Koude Oorlog, in 1994, vertrokken de Amerikanen. In een gedeelte van het Kamp van Zeist werd het Militaire Luchtvaart Museum gehuisvest, en in een ander gedeelte werd eind vorige eeuw tijdelijk een Schots gerechtshof gevestigd voor de berechting van verdachten in verband met de Lockerbie-zaak. In 2003 werd dat laatste gedeelte verbouwd tot een gevangenis waar onder meer illegalen die Nederland niet willen of kunnen verlaten en bolletjesslikkers worden gedetineerd."""

s = s.lower().translate(str.maketrans('', '', string.punctuation))

words = s.split()

print(f'{len(words)} woorden')
print(words)

unique_words = set(words)

print(f'{len(unique_words)} unieke woorden')
print(unique_words)

d = {}
for word in unique_words:
    n = words.count(word)
    d[word] = n

print(d)

for word, n in sorted(d.items(), key = lambda item: item[1]):
    print(f'{word:20}: {n:3} {"*" * n}')