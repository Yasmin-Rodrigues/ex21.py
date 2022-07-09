#Programa que leia o nome completo de uma pessoa e mostre seu primeiro e último nome 
nome =str(input('Digite seu nome completo:')).strip()
print('Primeiro nome:', nome.split()[0])
print('Último nome:', nome.split()[-1])