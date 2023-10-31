# Aula 09 - Manipulando textos

## Fatiamento
- frase[9:13]
O último valor não conta na contagem do fatiamento, ele sempre fica até o caractere anterior
- frase[9:21:2]  --> vai de dois em dois
- frase[:5]  --> vai do início até o 5
- frase[5:]  --> inicia do 15 e vai até o fim
- frase[9::3]  --> inicia no 9 e vai até o fical mas vai pulando 3

- len(frase) --> faz a contagem
- frase.count("o")  --> quantas vezes aparece a letra "O"
- frase.fing('deo')  --> verifica onde está localizado

### Transformação
- frase.replace('python', 'android') --> troca as frases

- frase.upper() --> deixa o texto maiuscula
- frase.lower() --> letras minúsculas
- frase.capitalize() --> Deixa apenas a primeira letra maiúscula
- frase.strip() --> remove espaços inúteis no inicio ou fim.

### Divisão
* Estudar como fazer split
-frase.split() --> faz uma lista para cadad palavra

### Prática
#### Desafios
- 

Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
