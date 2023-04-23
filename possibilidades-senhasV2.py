import itertools
from tqdm import tqdm
import os

# Definir o nome do arquivo de entrada e de saída
arquivo_entrada = "variacoes.txt"
arquivo_saida = "senhas.txt"

# Definir os caracteres especiais e dígitos numéricos a serem usados nas senhas
caracteres_especiais = ["!", "@", "#", "$", "%", "&"]
digitos_numericos = [str(i) for i in range(10)]

# Calcular o tamanho estimado do arquivo de saída
tamanho_entrada = os.path.getsize(arquivo_entrada)
tamanho_saida = 0
for n in range(1, 6):
    tamanho_saida += (len(caracteres_especiais) + len(digitos_numericos))**n * tamanho_entrada
tamanho_saida_mb = tamanho_saida / 1000000
print(f"Tamanho estimado do arquivo de saída: {tamanho_saida_mb:.2f} MB")

# Criar um conjunto para armazenar todas as palavras geradas
palavras_geradas = set()

# Iterar sobre cada linha do arquivo de entrada
with open(arquivo_entrada, "r") as f:
    for linha in tqdm(f, total=tamanho_entrada, desc="Gerando senhas"):
        linha = linha.strip()
        palavras_geradas.add(linha)

        # Gerar todas as possíveis combinações de caracteres especiais e adicioná-las à linha atual
        for n in range(1, 5):
            for combinacao in itertools.product(caracteres_especiais + digitos_numericos, repeat=n):
                linha_com_combinacao = linha + "".join(combinacao)
                palavras_geradas.add(linha_com_combinacao)

        # Gerar todas as possíveis combinações de 2 dígitos numéricos e um caractere especial e adicioná-las à linha atual
        for digito1 in range(10):
            for digito2 in range(10):
                for caracter_especial2 in caracteres_especiais:
                    linha_com_combinacao2 = linha + str(digito1) + str(digito2) + caracter_especial2
                    palavras_geradas.add(linha_com_combinacao2)

# Escrever cada palavra gerada no arquivo de saída
with open(arquivo_saida, "w") as f:
    for palavra in tqdm(palavras_geradas, desc="Escrevendo arquivo de saída"):
        f.write(palavra + "\n")
