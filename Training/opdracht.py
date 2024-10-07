import string
from operator import itemgetter

s = """Altijd snel alle voetbalwedstrijden die vandaag worden gespeeld in een handig voetbal TV-gids weekoverzicht. Op iservoetbalvanavond.nl kunt u met uw mobiele telefoon, tablet of pc in één oogopslag de juiste uitzendtijden vinden. Mis geen enkele topper uit de Eredivisie en blijf op de hoogte van al het voetbal in Europa met zowel de Champions League als de Europa League. Neem ook het weekoverzicht alvast over in uw agenda."""

s = s.lower().translate(str.maketrans('áäâàéëêèíïìîóöôòúüûù',
                                      'aaaaeeeeiiiioooouuuu',
                                      '.,!?'))

words = s.split()

unique_words = set(words)

d = {}
for word in sorted(unique_words):
    d[word] = words.count(word)

for word, n in sorted(d.items(), key = itemgetter(1), reverse = True):
    print(f'{word:25}: {n:3} {"*" * n}')
