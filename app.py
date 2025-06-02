import sqlite3

conexao = sqlite3.connect("financas.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    categoria TEXT NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL,
    descricao TEXT               
)
""")

conexao.commit()

def menu():
    while True:
        print("===== MENU =====")
        print("[1] Despesas")
        print("[2] Receitas")
        print("[3] Vizualizar Registros")
        print("[4] Sair")
        opcao = int(input("Informe a operação escolhida: "))
        
        if opcao == 1:
            despesas()
        elif opcao == 2:
            receitas()
        elif opcao == 3:
            visualizar()
        elif opcao == 4:
            print("Você saiu do sistema. Até a próxima!")
            break
        else:
            print("Você escolheu uma opção inválida. Tente novamente.")
            continue

def despesas():
    
    print("[1] Adicionar Despesa")
    print("[2] Editar Despesa")
    print("[3] Excluir Despesa")        
    opcao = int(input("Informe a operação escolhida: "))

    if opcao == 1:
        tipo = "despesa"
        categoria = input("Informe a categoria da despesa: ")
        valor = float(input("Informe o valor da despesa: "))
        data = input("Informe a data da despesa (DD-MM-AAAA): ")
        descricao = input("Informe a descrição da despesa (OPCIONAL): ")
        
        cursor.execute("INSERT INTO transacoes (tipo, categoria, valor, data, descricao) VALUES (?, ?, ?, ?, ?)", (tipo, categoria, valor, data, descricao))
        conexao.commit()
    elif opcao == 2:
        id_despesa = int(input("Informe o ID da despesa: "))
        cursor.execute("SELECT * FROM transacoes WHERE id = ?", (id_despesa,))
        despesa = cursor.fetchone()

        if despesa:
            print("\n Despesa Atual:\n")
            print(f"| [{despesa[0]}] - {despesa[1]} | {despesa[2]} | R${float(despesa[3]):.2f} em {despesa[4]} | Descrição: {despesa[5]}")

            nova_categoria = input("Informe a nova categoria: ")
            novo_valor = float(input("Informe o novo valor: "))
            nova_data = input("Informe a nova data: ")
            nova_descricao = input("Informe a nova descrição: ")
            cursor.execute("""
                UPDATE transacoes
                SET categoria = ?, valor = ?, data = ?, descricao = ?
                WHERE id = ? AND tipo = 'despesa'
            """,(nova_categoria, novo_valor, nova_data, nova_descricao, id_despesa))
            conexao.commit()
            print("\n Despesa atualizada!")
        else:
            print("Despesa não encontrada")
    elif opcao == 3:
        id_despesa = int(input("Informe o ID da despesa: "))
        cursor.execute("DELETE FROM transacoes WHERE id = ? AND tipo = 'despesa'", (id_despesa,))
        print("\n Despesa deletada.\n")


def receitas():

    print("[1] Adicionar Receitas")
    print("[2] Editar Receitas")
    print("[3] Excluir Receitas")
    opcao = int(input("Informe a operação escolhida: "))

    if opcao == 1:
        
        tipo = "receita"
        categoria = input("Informe a categoria da Receita: ")
        valor = float(input("Informe o valor da Receita: "))
        data = input("Informe a data da operação: ")
        descricao = input("Informe a descrição da operação (OPCIONAL): ")
        conexao.execute("INSERT INTO transacoes (tipo, categoria, valor, data, descricao) VALUES (?, ?, ?, ?, ?)", (tipo, categoria, valor, data, descricao))
    elif opcao == 2:
        id_receita = int(input("Informe o ID da receita: "))
        cursor.execute("SELECT * FROM transacoes WHERE id = ?", (id_receita,))
        receita = cursor.fetchone()

        if receita:
            print("\nReceita Atual:\n")
            print(f"| [{receita[0]}] - {receita[1]} | {receita[2]} | R${float(receita[3]):.2f} em {receita[4]} | Descrição: {receita[5]}")

            nova_categoria = input("Informe a nova categoria da receita")
            novo_valor = float(input("Informe o novo valor: "))
            nova_data = input("Informe a nova data: ")
            nova_descricao = input("Informe a nova descrição: ")
            cursor.execute("""
                UPDATE transacoes
                SET categoria = ?, valor = ?, data = ?, descricao = ?
                WHERE id = ? AND tipo = 'receita'
                """, (nova_categoria, novo_valor, nova_data, nova_descricao, id_receita))
            conexao.commit()
            print("\nReceita alterada.\n")
        else:
            print("\nID não encontrado.\n")
    elif opcao == 3:
        id_receita = int(input("Informe o ID da receita: "))
        cursor.execute("DELETE FROM transacoes WHERE id = ? AND tipo = 'receita'", (id_receita,))
        print("\nReceita deletada.\n")

def visualizar():
    print("[1] Por Data")
    print("[2] Por Categoria")
    print("[3] Por Tipo")
    print("[4] Voltar")

    opcao = int(input("Informe a operação escolhida: "))

    if opcao == 1:
        data = input("Informe a data (DD-MM-AAAA): ")
        cursor.execute("SELECT * FROM transacoes WHERE data = ?", (data,))
    elif opcao == 2:
        categoria = input("Informe a categoria: ")
        cursor.execute("SELECT * FROM transacoes WHERE categoria = ?", (categoria,))
    elif opcao == 3:
        tipo = input("Informe o tipo: ")
        cursor.execute("SELECT *FROM transacoes WHERE tipo = ?", (tipo,))
    elif opcao == 4:
        menu()
    else:
        print("Opção inválida. Tente novamente")
        return

    resultados = cursor.fetchall()
    
    if not resultados:
        print("Não foi encontrado registros.")
    else:
        for resultado in resultados:
            print(f"| [{resultado[0]}] - {resultado[1]} | {resultado[2]} | R${float(resultado[3]):.2f} em {resultado[4]} | Descrição: {resultado[5]}")

menu()
conexao.close()