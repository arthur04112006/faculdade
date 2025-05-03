#calculo de imc

#entrada de dados
nome = input("Qual seu nome? ")
peso = float(input("Qual seu peso em kilos? (Ex: 68.4): "))
altura =  float(input("Qual sua altura em metros? (Ex: 1.75): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"{nome}, Seu imc é: {imc:.2f} e você está abaixo do peso")
elif 18.5 <= imc < 24.9:
    print(f"{nome}, Seu imc é: {imc:.2f} e você está com peso normal")
elif 25 <= imc < 29.9:
    print(f"{nome}, Seu imc é: {imc:.2f} e você está com sobrepeso") 
else:
    print(f"{nome}, Seu imc é: {imc:.2f} e você está obeso(a)!")




