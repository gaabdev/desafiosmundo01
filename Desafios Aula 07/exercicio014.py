# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

grauscelsius = float(input("Informe a temperatura em °C: "))

fahrenheit = (grauscelsius * 9/5)+32

print("A temperatura de {}°C corresponde a {}F!".format(grauscelsius, fahrenheit))