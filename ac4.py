#ex1
def e_primo(num):
    if num <= 1:
        print("o numero é primo")
        return 

    primo = True
    for div in range(2, int(num**0.5) + 1):
        if num % div == 0:
            primo = False
    if primo:
        print("o numero é primo")
    else:
        print("o numero nao é primo")

numero = 8
e_primo(numero)

#ex2
def calcular_parcelamento(divida):
    tabela_juros = {
        1: 0,
        3: 10,
        6: 15,
        9: 20,
        12: 25
    }
    
    print("Quantidade de Parcelas  % de Juros Valor dos Juros Valor Total Valor da Parcela")
    for parcelas, juros in tabela_juros.items():
        valor_juros = (juros / 100) * divida
        valor_total = divida + valor_juros
        valor_parcela = valor_total / parcelas
        print(f"{parcelas}                       {juros}%             R$ {valor_juros:.2f}         R$ {valor_total:.2f}     R$ {valor_parcela:.2f}")

# Entrada do valor da dívida
divida = float(input("Digite o valor da dívida: R$ "))
calcular_parcelamento(divida)

#ex3
intervalos = {
    "0-25": 0,
    "26-50": 0,
    "51-75": 0,
    "76-100": 0
}

while True:
    numero = int(input("Digite um número positivo (ou um número negativo para encerrar): "))
    
    if numero < 0:
        break
    
    if 0 <= numero <= 25:
        intervalos["0-25"] += 1
    elif 26 <= numero <= 50:
        intervalos["26-50"] += 1
    elif 51 <= numero <= 75:
        intervalos["51-75"] += 1
    elif 76 <= numero <= 100:
        intervalos["76-100"] += 1

for intervalo, quantidade in intervalos.items():
    print(f"Números no intervalo {intervalo}: {quantidade}")
