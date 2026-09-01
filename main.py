produtos = []

while True:

   print("===== CONTROLE DE ESTOQUE =====")
   print("Agropecuária São Judas Tadeu")

   print("1 - Cadastrar produto")
   print("2 - Listar produtos")
   print("3 - Adicionar produto ao estoque")
   print("5 - Registrar venda")
   print("4 - Remover produto do estoque")
   print("6 - Buscar produto no estoque")
   print("7 - Sair do sistema")

   opcao = input("Escolha uma opção: ")

   if opcao == "7":
      print("Saindo do sistema...")
      break

   elif opcao == "1":

      print("=== CADASTRO ===")

      nome = input("Digite o nome do produto: ")
      quant = int(input("Digite a quantidade: "))
      preco = float(input("Digite o preço: "))
      val = input("Digite a validade do produto (dd/mm/aaaa): ")

      produtos.append({
        "nome": nome, 
        "quantidade": quant,
        "preco": preco,
        "validade": val
      })
      
      print(f"Produto {nome}, com {quant} unidades, com valor R$ {preco} e validade {val} cadastrado com sucesso!")

   elif opcao == "2":

      print("=== LISTA DE PRODUTOS ===")

      if len(produtos) == 0:
         print("Nenhum produto cadastrado.")

      else:
         for produto in produtos:
            print(f"""
            Produto: {produto['nome']}
            Quantidade: {produto['quantidade']}
            Preço: R$ {produto['preco']:.2f}
            Validade: {produto['validade']}
            """)
   elif opcao == "3":

      print("=== ADICIONAR PRODUTO AO ESTOQUE ===")

      nome = input("Digite o nome do produto: ")
      quant = int(input("Digite a quantidade a ser adicionada: "))

      encontrado = False

      for produto in produtos:
         if produto["nome"].lower() == nome.lower():
            produto["quantidade"] += quant
            print(f"Adicionado {quant} unidades ao produto {nome}.") 

            encontrado = True
            break

      if not encontrado:
         print(f"Produto {nome} não encontrado no estoque.")

   elif opcao == "4":

      print("=== REMOVER PRODUTO ===")

      