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

         if quant <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            continue

         return quant

      except ValueError:
         print("Erro: Digite apenas números.")

def pedir_preco(mensagem):
   while True:
      try:
         preco = float(input(mensagem))

         if preco <= 0:
            print("Erro: O preço deve ser maior que zero.")
            continue

         return preco

      except ValueError:
         print("Erro: Digite apenas números.")

def encontrar_produto(nome):
   for produto in produtos:
         if produto["nome"].lower() == nome.lower():
            return produto

   return None

def cadastrar_produto():
   print("=== CADASTRO ===")
   
   nome = pedir_nome("Digite o nome do produto: ")

   produto = encontrar_produto(nome)

   if produto:
      print(f"O produto {nome} já esta cadastrado.")
      return

   quant = pedir_quantidade("Digite a quantidade: ")
   preco = pedir_preco("Digite o preço: ")
   val = input("Digite a validade do produto (dd/mm/aaaa): ")

   produtos.append({
   "nome": nome, 
   "quantidade": quant,
   "preco": preco,
   "validade": val
   })
         
   print(f"Produto {nome}, com {quant} unidades, com valor R${preco} e validade {val} cadastrado com sucesso!")

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
   produto = encontrar_produto(nome)

   if produto:

      quant = pedir_quantidade("Digite a quantidade a ser adicionada: ")
      produto["quantidade"] += quant

      print(f"Adicionado {quant} unidades ao produto {nome}.") 
      print(f"Quantidade atual no estoque: {produto['quantidade']}")
   
   else:
        print(f"Produto {nome} não encontrado no estoque.")

def remover_produto():
   print("=== REMOVER PRODUTO ===")
   
   nome = pedir_nome("Digite o nome do produto que deseja excluir: ")
   produto = encontrar_produto(nome)

   if produto:

      quant = pedir_quantidade("Digite a quantidade a ser removida: ")
      if produto["quantidade"] >= quant:
         produto["quantidade"] -= quant
   
         print(f"Removido {quant} unidades do produto {nome}.")
         print(f"Quantidade atual no estoque: {produto['quantidade']}")

      else:
         print(f"Quantidade insuficiente do produto {nome}.")
      
   else:
      print(f"Produto {nome} não encontrado no estoque.")
      

def registrar_venda():
   print("=== REGISTRAR VENDA ===")
   
   nome = pedir_nome("Digite o nome do produto vendido: ")
   produto = encontrar_produto(nome)

   if produto:

      quant = pedir_quantidade("Digite a quantidade vendida: ")
      if produto["quantidade"] >= quant:
         produto["quantidade"] -= quant

         print(f"Produto {nome} vendido com sucesso! Quantidade vendida: {quant}.")
         print(f"Quantidade restante no estoque: {produto['quantidade']}.")

      else:
            print(f"Quantidade insuficiente do produto {nome}.")

   else:
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

def editar_produto():
   print("=== EDITAR PRODUTO ===")

   nome = pedir_nome("Digite o nome do produto que deseja alterar: ")

   produto = encontrar_produto(nome)

   if produto:

      print("O que deseja alterar?")
      print("1 - Nome")
      print("2 - Quantidade")
      print("3 - Preço")
      print("4 - Validade")
      print("5 - Cancelar")

      opcao = input("Escolha uma opção: ")

      if opcao == "1":
         novo_nome = pedir_nome("Digite o novo nome: ")

         produto["nome"] = novo_nome

         print(f"{nome} atualizado para {novo_nome}.")

      elif opcao == "2":
         nova_quant = pedir_quantidade("Digite a nova quantidade: ")

         produto["quantidade"] = nova_quant

         print(f"{nome} com a quantidade atualizada.")

      elif opcao == "3":
         novo_preco = pedir_preco("Digite o novo preço: ")

         produto["preco"] = novo_preco

         print(f"{nome} com o preço atualizado.")

      elif opcao == "4":
         nova_val = input("Digite a nova validade: ").strip()

         produto["validade"] = nova_val

         print(f"{nome} com a validade atualizada.")

      elif opcao == "5":
         print("Edição cancelada.")

      else:
         print("Opção inválida.")

   else:
      print(f"O produto {nome} não foi encontrado no estoque.")

def relatorio_estoque():
   print("=== RELATÓRIO DE ESTOQUE ===")

   if len(produtos) == 0:
      print("Estoque vazio.")
      return

   total_produtos = len(produtos)
   total_unid = 0
   valor_tot = 0

   for produto in produtos:
      total_unid += produto["quantidade"]
      valor_tot += produto["quantidade"] * produto["preco"]

   print(f"Produtos cadastrados: {total_produtos}.")
   print(f"Total de unidades: {total_unid}.")
   print(f"Valor total do estoque: R${valor_tot:.2f}.")

   print("\n= PRODUTOS COM ESTOQUE BAIXO ===")

   limite = 5

   for produto in produtos:
      if produto["quantidade"] <= limite:
         print(f"{produto['nome']} - {produto['quantidade']} unidades.")

         encontrou_baixo = True

   if not encontrado:
      print("Nenhum produto com estoque baixo.")


   
while True:
   
   print("\n===== CONTROLE DE ESTOQUE =====")
   print("Agropecuária São Judas Tadeu")

   print("1 - Cadastrar produto")
   print("2 - Listar produtos")
   print("3 - Adicionar produto")
   print("4 - Remover produto")
   print("5 - Registrar venda")
   print("6 - Buscar produto")
   print("7 - Editar produto")
   print("8 - Relatório do estoque")
   print("9 - Sair do sistema")

   opcao = input("Escolha uma opção: ")

   if opcao == "9":
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

   elif opcao == "7":
      editar_produto()

   elif opcao == "8":
      relatorio_estoque()

   else:
      print("Opção inválida. Digite de 1 a 9, por favor.")

