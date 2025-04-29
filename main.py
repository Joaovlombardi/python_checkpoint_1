alunos = {
    "nome" : [],
    "idade" : [],
    "notas" : [],
    "status" : [],
    "media" : []
}

while True:
    print("MENU DE OPÇÕES")
    print("1 - Cadastrar novo aluno")
    print('2 - Listar alunos cadastrados')
    print('3 - Ver estatísticas')
    print('4 - Sair do programa')

    menu = input('Digite uma opção: ')

    match menu:
        case "1":
            nome = input("Digite o nome do aluno: ")
            idade = float(input("Digite o idade do aluno: "))
            nota1 = float(input("Digite sua nota 1: "))
            nota2 = float(input("Digite sua nota 2: "))
            nota3 = float(input("Digite sua nota 3: "))
            media = (nota1 + nota2 + nota3) / 3

            alunos["nome"].append(nome)
            alunos["idade"].append(idade)
            alunos["notas"].append([nota1, nota2, nota3])
            alunos["media"].append((media))

            if media >= 6:
                alunos["status"].append("Aprovado")
            else:
                alunos["status"].append("Reprovado")

        case "2":
            if len(alunos["nome"]) == 0:
                print("Nenhum aluno foi cadastrado.")
            else:
                for i in range(len(alunos["nome"])):
                    print("---------------------------")
                    print(f' Nome: {alunos["nome"][i]}\n Idade: {alunos["idade"][i]}\n Notas: {alunos["notas"][i]}\n Média: {alunos["media"][i]:.2f}\n Status: {alunos["status"][i]}\n')

        case "3":
            media = sum(alunos["idade"]) / len(alunos["idade"])
            aprovados = alunos["status"].count("Aprovado")
            maiorMedia = 0

            for i in range(len(alunos["media"])):

                if alunos["media"][i] > maiorMedia:
                    maiorMedia = alunos["media"][i]

            print(f"A maior média é: {maiorMedia}")
            print(f"A média de idade é: {media}")
            print(f"Alunos aprovados: {aprovados}")

        case "4":
            print("Saindo...")
            break
        case _:
            print("Digite uma opção válida")