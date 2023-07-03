letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, 'it a vowel')
else:
    print(letter, 'it not a vowel')

vowels = 'aeiou'
letter = 'o'
print(letter in vowels)
if letter in vowels:
    print(letter, 'it a vowel')


letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set)

vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_list)

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple)

vowel_dict = {'a': 'apple', 
              'e': 'elephant',
              'i': 'impala',
              'o': 'ocelot',
              'u': 'unicorn'}
print(letter in vowel_dict)

vowel_string = "aeiou"
print(letter in vowel_string)