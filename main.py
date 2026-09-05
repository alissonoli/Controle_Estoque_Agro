produtos = []

def pedir_nome(mensagem):
   while True:
      nome = input(mensagem).strip()

      if nome == "":
         print("Erro: o nome do produto não pode estar vazio.")
         continue

      return nome

def pedir_quantidade(mensagem):
   while True:
      try:
         quant = int(input(mensagem))

         if quant < 0:
            print("Erro: A quantidade deve ser maior que zero.")
            continue

         return quant

      except ValueError:
         print("Erro: Digite apenas números.")

def pedir_preco(mensagem):
   while True:
      try:
         preco = float(input(mensagem))

         if preco < 0:
            print("Erro: O preço deve ser maior que zero.")
            continue

         return preco

      except ValueError:
         print("Erro: Digite apenas números.")

def cadastrar_produto():
   print("=== CADASTRO ===")
   
   nome = pedir_nome("Digite o nome do produto: ")
   try: 
    quant = pedir_quantidade("Digite a quantidade: ")
    preco = pedir_preco("Digite o preço: ")
    val = input("Digite a validade do produto (dd/mm/aaaa): ")
   except ValueError:
      print("Erro: Digite apenas números.")
   
   produtos.append({
   "nome": nome, 
   "quantidade": quant,
   "preco": preco,
   "validade": val
   })
         
   print(f"Produto {nome}, com {quant} unidades, com valor R$ {preco} e validade {val} cadastrado com sucesso!")

def listar_produtos():
   print("=== PRODUTOS DO ESTOQUE ===")
   
   if len(produtos) == 0:
     print("Estoque vazio.")
   
   else:
    for produto in produtos:
     print(f"""
         Produto: {produto['nome']}
         Quantidade: {produto['quantidade']}
         Preço: R$ {produto['preco']:.2f}
         Validade: {produto['validade']}
         """)   

def adicionar_produto():
   print("=== ADICIONAR PRODUTO AO ESTOQUE ===")
      
   nome = pedir_nome("Digite o nome do produto: ")
   quant = pedir_quantidade("Digite a quantidade a ser adicionada: ")
   encontrado = False
      
   for produto in produtos:
      if produto["nome"].lower() == nome.lower():
        produto["quantidade"] += quant
        print(f"Adicionado {quant} unidades ao produto {nome}.") 
      
        encontrado = True
        break
      
   if not encontrado:
        print(f"Produto {nome} não encontrado no estoque.")

def remover_produto():
   print("=== REMOVER PRODUTO ===")
   
   nome = pedir_nome("Digite o nome do produto que deseja excluir: ")
   quant = pedir_quantidade("Digite a quantidade a ser removida: ")
   
   encontrado = False
   
   for produto in produtos:
      if produto["nome"].lower() == nome.lower():
   
       encontrado = True
   
       if produto["quantidade"] >= quant:
   
        produto["quantidade"] -= quant
   
        print(f"Removido {quant} unidades do produto {nome}.")
   
      else:
        print(f"Quantidade insuficiente do produto {nome}.")
      break
   
   if not encontrado:
            print(f"Produto {nome} não encontrado no estoque.")

def registrar_venda():
   print("=== REGISTRAR VENDA ===")
   
   nome = pedir_nome("Digite o nome do produto vendido: ")
   quant = pedir_quantidade("Digite a quantidade vendida: ")

   for produto in produtos:

      if produto["nome"].lower() == nome.lower(): 

        encontrado = True

        if produto["quantidade"] >= quant:

         produto["quantidade"] -= quant

         print(f"Produto {nome} vendido com sucesso! Quantidade vendida: {quant}.")
         print(f"Quantidade restante no estoque: {produto['quantidade']}.")

        else:
            print(f"Quantidade insuficiente do produto {nome}.")

        break


   if not encontrado:
    print(f"Produto {nome} não encontrado no estoque.")

def buscar_produtos():
   print("=== BUSCAR PRODUTO ===")

   nome = pedir_nome("Digite o nome do produto: ")

   encontrado = False

   for produto in produtos:
      if produto["nome"].lower() == nome.lower():
         encontrado = True
         print(f"""
         Produto: {produto["nome"]}
         Quantidade: {produto["quantidade"]}
         Preço: R$ {produto["preco"]:.2f}
         Validade: {produto["validade"]}
         """)
         break

   if not encontrado:
      print(f"O produto {nome} não existe no estoque.")

while True:
   
   print("\n===== CONTROLE DE ESTOQUE =====")
   print("Agropecuária São Judas Tadeu")

   print("1 - Cadastrar produto")
   print("2 - Listar produtos")
   print("3 - Adicionar produto ao estoque")
   print("4 - Remover produto do estoque")
   print("5 - Registrar venda")
   print("6 - Buscar produto no estoque")
   print("7 - Sair do sistema")

   opcao = input("Escolha uma opção: ")

   if opcao == "7":
      print("Saindo do sistema...")
      break

   elif opcao == "1":
      cadastrar_produto()

   elif opcao == "2":
      listar_produtos()

   elif opcao == "3":
      adicionar_produto()

   elif opcao == "4":
      remover_produto()

   elif opcao == "5":
      registrar_venda()

   elif opcao == "6":
      buscar_produtos()

   else:
      print("Opção inválida. Digite de 1 a 7, por favor.")

