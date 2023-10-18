# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;

valor = float(input("Digite o valor em reais: "))
desconto = float(input("Digite a '%' de desconto: "))

desconto = (valor * desconto) / 100
resultado = valor-desconto
print(f"""
        Valor de Desconto: R${desconto}
        Valor Final: R${resultado} 
""")