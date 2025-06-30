import sqlite3

conn = sqlite3.connect('urna_eletronica.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS candidatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS votos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidato_id INTEGER,
    cpf TEXT UNIQUE,
    FOREIGN KEY (candidato_id) REFERENCES candidatos(id)
)
''')

conn.commit()



def cadastrar_candidatos():
    print("\n--- Cadastro de Candidatos ---")
    while True:
        nome = input("Nome do candidato (ou 'fim' para encerrar): ")
        if nome.lower() == 'fim':
            break
        cursor.execute("INSERT INTO candidatos (nome) VALUES (?)", (nome,))
        conn.commit()
        print(f"Candidato '{nome}' cadastrado com sucesso.")

def exibir_candidatos():
    print("\n--- Candidatos ---")
    cursor.execute("SELECT * FROM candidatos")
    candidatos = cursor.fetchall()
    for c in candidatos:
        print(f"{c[0]} - {c[1]}")

def votar():
    print("\n--- Votação ---")
    cpf = input("Digite seu CPF (apenas números): ")
    cursor.execute("SELECT * FROM votos WHERE cpf=?", (cpf,))
    if cursor.fetchone():
        print("⚠️ Você já votou!")
        return

    exibir_candidatos()
    try:
        escolha = int(input("Digite o número do candidato que deseja votar: "))
        cursor.execute("SELECT * FROM candidatos WHERE id=?", (escolha,))
        if cursor.fetchone():
            cursor.execute("INSERT INTO votos (candidato_id, cpf) VALUES (?, ?)", (escolha, cpf))
            conn.commit()
            print("✅ Voto registrado com sucesso.")
        else:
            print("❌ Candidato não encontrado.")
    except ValueError:
        print("❌ Entrada inválida.")

def apurar_votos():
    print("\n--- Apuração dos Votos ---")
    cursor.execute('SELECT COUNT(*) FROM votos')
    total_votos = cursor.fetchone()[0]

    cursor.execute('''
    SELECT candidatos.nome, COUNT(votos.id) AS total 
    FROM votos 
    JOIN candidatos ON votos.candidato_id = candidatos.id 
    GROUP BY candidato_id ORDER BY total DESC
    ''')
    resultado = cursor.fetchall()

    for nome, votos in resultado:
        porcentagem = (votos / total_votos) * 100
        print(f"{nome} - {votos} votos ({porcentagem:.1f}%)")

    if len(resultado) > 1 and resultado[0][1] == resultado[1][1]:
        print("\n⚠️ Empate técnico! Seria necessário um segundo turno.")
    else:
        print(f"\n🎉 Eleito(a): {resultado[0][0]}")

def main():
    while True:
        print("\n==== MENU ====")
        print("1 - Cadastrar candidatos")
        print("2 - Votar")
        print("3 - Apurar votos")
        print("4 - Sair")
        op = input("Escolha uma opção: ")
        if op == '1':
            cadastrar_candidatos()
        elif op == '2':
            votar()
        elif op == '3':
            apurar_votos()
        elif op == '4':
            break
        else:
            print("Opção inválida.")

main()
conn.close()
