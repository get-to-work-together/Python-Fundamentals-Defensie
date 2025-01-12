
s = input('Geef tekst: ').lower()

print(f'De tekst bevat {len(s)} karakters')
print(f'De tekst bevat {len(s.replace(" ", ""))} karakters (zonder spaties)')

totaal_aantal_klinkers = 0

for klinker in 'aeiouy':
    n = s.count(klinker)
    totaal_aantal_klinkers += n
    print(f'De "{klinker}" komt {n} keer voor')

print(f'De tekst bevat dus {totaal_aantal_klinkers} klinkers')













# s = input('Give some text: ').lower()
#
# total_number_of_vowels = 0
# for vowel in 'aeiouy':
#     n = s.count(vowel)
#     total_number_of_vowels += n
#     print(f'The vowel "{vowel}" was found {n} times.')
#
# print(f'The complete text contains {len(s)} characters.')
#
# print(f'The text contains {total_number_of_vowels} vowels.')






























# number_of_a = s.count('a')
# number_of_e = s.count('e')
# number_of_i = s.count('i')
# number_of_o = s.count('o')
# number_of_u = s.count('u')
# number_of_y = s.count('y')
#
# number_of_vowels = number_of_a + \
#                    number_of_e + \
#                    number_of_i + \
#                    number_of_o + \
#                    number_of_u + \
#                    number_of_y
#
# print("Total number of characters: %d" % len(s))
#
# print("Found the vowel 'a' %d times" % number_of_a)
# print("Found the vowel 'e' %d times" % number_of_e)
# print("Found the vowel 'i' %d times" % number_of_i)
# print("Found the vowel 'o' %d times" % number_of_o)
# print("Found the vowel 'u' %d times" % number_of_u)
# print("Found the vowel 'y' %d times" % number_of_y)
#
# print("Total number of vowels: %d" % number_of_vowels)
#
#









# s = input('Give some text: ').lower()
#
# number_of_vowels = 0
# for vowel in 'aeiouy':
#     n = s.count(vowel)
#     number_of_vowels += n
#     print(f"Vowel '{vowel}' occurs {n} times.")
#
# print(f"Total length: {len(s)}")
# print(f"Total number of vowels: {number_of_vowels}")
