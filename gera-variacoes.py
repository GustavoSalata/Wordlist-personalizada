#!/usr/bin/python3 
import itertools

def generate_variations(word):
    """Gera todas as possíveis variações de uma palavra"""
    variations = set()
    for variation in itertools.product(*zip(word.upper(), word.lower())):
        variations.add(''.join(variation))
    return variations

def generate_replacements(word):
    """Gera todas as possíveis substituições de caracteres similares em uma palavra"""
    variations = set()
    for char in word:
        if char.lower() == 'a':
            variation = word.replace(char, '@')
            variations.update(generate_variations(variation))
        elif char.lower() == 'e':
            variation = word.replace(char, '3')
            variations.update(generate_variations(variation))
        elif char.lower() == 'i':
            variation = word.replace(char, '!')
            variations.update(generate_variations(variation))
        elif char.lower() == 'o':
            variation = word.replace(char, '0')
            variations.update(generate_variations(variation))
        elif char.lower() == 's':
            variation = word.replace(char, '$')
            variations.update(generate_variations(variation))
        elif char.lower() == 't':
            variation = word.replace(char, '7')
            variations.update(generate_variations(variation))
    return variations

def generate_variations_list(words, output_file):
    """Gera todas as possíveis variações de uma lista de palavras e as escreve em um arquivo de texto"""
    variations = set()
    for word in words:
        variations.update(generate_variations(word))
        variations.update(generate_replacements(word))
    with open(output_file, 'w') as f:
        for variation in variations:
            f.write(variation + '\n')

if __name__ == '__main__':
    words = ['support']
    output_file = 'variacoes.txt'
    generate_variations_list(words, output_file)
