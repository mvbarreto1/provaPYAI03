produtos = {}

for i in range(5):
    nome = input(f"Insira o nome do produto {i+1}: ")
    while True:
        try:
            preco = float(input(f"Insira o preço do produto {nome}: R$ "))
            break
        except ValueError:
            print("Por favor, insira um valor válido para o preço.")
    produtos[nome] = preco

valor_total = sum(produtos.values())

print("\nProdutos cadastrados:")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")
print(f"\nValor total da compra: R$ {valor_total:.2f}")