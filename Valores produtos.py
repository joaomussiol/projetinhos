valor_produto = float(input("Digite o valor do seu produto:"))
desconto_produto = float(input("Digite o valor de desconto do seu produto:"))
TAXAS = 0.1

valor_desconto = valor_produto * desconto_produto / 100
valor_produto_descontado = valor_produto - valor_desconto

taxas = valor_produto_descontado * TAXAS
preco_final = valor_produto_descontado + taxas

print(preco_final)

