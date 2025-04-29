# Sistema de Cadastro de Alunos - Explicação do Código

Este programa em Python permite cadastrar alunos, listar os cadastrados e visualizar estatísticas como média de idade, maior média de notas e total de aprovados.

## Estrutura de Dados

O sistema usa um dicionário para armazenar as informações dos alunos:

```python
alunos = {
    "nome" : [],
    "idade" : [],
    "notas" : [],
    "status" : [],
    "media" : []
}
```

Cada lista dentro do dicionário guarda as seguintes informações dos alunos:
- `nome`: Lista com os nomes dos alunos.
- `idade`: Lista com as idades dos alunos.
- `notas`: Lista com as 3 notas de cada aluno.
- `status`: Lista com o status de aprovação de cada aluno (Aprovado ou Reprovado).
- `media`: Lista com as médias das notas dos alunos.

## Menu Principal

O programa exibe um menu com 4 opções e executa ações com a estrutura `match-case`:

```
1 - Cadastrar novo aluno  
2 - Listar alunos cadastrados  
3 - Ver estatísticas  
4 - Sair do programa
```

## Opção 1 - Cadastrar Novo Aluno

Quando o usuário escolhe a opção 1, o programa realiza os seguintes passos:
1. Solicita o nome, idade e 3 notas do aluno.
2. Calcula a média das notas com a fórmula:
   ```python
   media = (nota1 + nota2 + nota3) / 3
   ```
3. Armazena os dados no dicionário `alunos`.
4. Verifica se a média é maior ou igual a 6:
   - Se sim, o status do aluno é "Aprovado".
   - Caso contrário, o status é "Reprovado".

## Opção 2 - Listar Alunos Cadastrados

Na opção 2, o programa verifica se há alunos cadastrados:
- Se não houver, exibe a mensagem "Nenhum aluno foi cadastrado".
- Caso contrário, lista todos os alunos cadastrados, exibindo as informações de cada um, como nome, idade, notas, média e status.

O código que realiza a listagem é:
```python
for i in range(len(alunos["nome"])):
    print(f'Nome: {alunos["nome"][i]}')
    print(f'Idade: {alunos["idade"][i]}')
    print(f'Notas: {alunos["notas"][i]}')
    print(f'Média: {alunos["media"][i]:.2f}')
    print(f'Status: {alunos["status"][i]}')
```

## Opção 3 - Estatísticas

A opção 3 fornece algumas estatísticas gerais dos alunos cadastrados:
1. **Média de idade**: Calcula a média das idades de todos os alunos com a fórmula:
   ```python
   media = sum(alunos["idade"]) / len(alunos["idade"])
   ```
2. **Maior média**: Determina a maior média de notas entre todos os alunos:
   ```python
   maiorMedia = 0
   for i in range(len(alunos["media"])):
       if alunos["media"][i] > maiorMedia:
           maiorMedia = alunos["media"][i]
   ```
3. **Total de aprovados**: Conta quantos alunos foram aprovados:
   ```python
   aprovados = alunos["status"].count("Aprovado")
   ```

## Opção 4 - Sair

A opção 4 encerra o programa com a instrução `break`, saindo do loop principal.

## Opção Inválida

Se o usuário digitar algo diferente de 1 a 4, o programa exibe a mensagem:
```python
print("Digite uma opção válida")
```

## Observações

- **Armazenamento**: O programa não salva os dados em um arquivo, todas as informações são mantidas apenas em memória durante a execução.
- **Validação de Entrada**: Não há tratamento de erro para entradas inválidas (por exemplo, se o usuário digitar um valor não numérico para notas ou idade).
- **Uso de `match-case`**: O código utiliza a estrutura `match-case` que foi introduzida no Python 3.10.

