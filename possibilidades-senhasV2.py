#!/usr/bin/python3 

import itertools
import os
from tqdm import tqdm

# Definir o nome do arquivo de entrada e de saída
arquivo_entrada = "variacoes.txt"
arquivo_saida = "senhas.txt"

# Definir os caracteres especiais e dígitos numéricos a serem usados nas senhas
caracteres_especiais = ["!", "@", "#", "$", "%"]
digitos_numericos = [str(i) for i in range(10)]

# Calcular o tamanho estimado do arquivo de saída
tamanho_entrada = os.path.getsize(arquivo_entrada)
tamanho_saida = 0
for n in range(1, 5):
    tamanho_saida += len(caracteres_especiais) * (10**n) * tamanho_entrada
    tamanho_saida += len(caracteres_especiais) * tamanho_entrada
tamanho_saida_mb = tamanho_saida / 1000000
print(f"Tamanho estimado do arquivo de saída: {tamanho_saida_mb:.2f} MB")

# Criar um conjunto para armazenar todas as palavras geradas
palavras_geradas = set()

# Iterar sobre cada linha do arquivo de entrada
with open(arquivo_entrada, "r") as f:
    for linha in tqdm(f, total=tamanho_entrada, desc="Gerando senhas"):
        linha = linha.strip()

        # Adicionar 1 caracter especial + 4 digitos numéricos
        for char_especial in caracteres_especiais:
            for digitos in itertools.product(digitos_numericos, repeat=4):
                senha = linha + char_especial + ''.join(digitos)
                palavras_geradas.add(senha)

        # Adicionar 2 digitos numéricos + 1 caracter especial
        for digitos in itertools.product(digitos_numericos, repeat=2):
            for char_especial in caracteres_especiais:
                senha = linha + ''.join(digitos) + char_especial
                palavras_geradas.add(senha)

        palavras_geradas.add(linha)

# Escrever cada palavra gerada no arquivo de saída
with open(arquivo_saida, "w") as f:
    for palavra in tqdm(palavras_geradas, desc="Escrevendo arquivo de saída"):
        f.write(palavra + "\n")

