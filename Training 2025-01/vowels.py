s = input('Geef tekst: ')

total_number_of_vowels = 0
for vowel in 'aeiou':
    n = s.count(vowel)
    total_number_of_vowels += n
    print(f'Klinker "{vowel}" komt {n} keer voor.')

print(f'Er zijn {total_number_of_vowels} klinkers in de tekst.')