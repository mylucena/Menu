while True:
  print("Menu")
  print("1. Criar Turma")
  print("2. Adicionar Professor")
  print("3. Adicionar Estudante")
  print("4. Adicionar Nota")
  print("5. Consultar Nota")
  print("6. Salvar Nota")
  print("7. Sair")

  opcao_escolhida = int(input("\nEscolha a opção: "))


  if opcao_escolhida == 1:
      print("Criei uma turma!\n")
  elif opcao_escolhida == 2:
      print("Adicione um professor!\n")
  elif opcao_escolhida == 3:
      print("Adicione um estudante!\n")
  elif opcao_escolhida == 4:
      print("Adicione uma nota!\n")
  elif opcao_escolhida == 5:
      print("Consultar uma nota!\n")
  elif opcao_escolhida == 6:
      print("Salve uma nota!\n")
  elif opcao_escolhida == 7:
      print("Saindo...")
      break
  else:
      print("Opção inválida!\n")