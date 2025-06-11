from datetime import datetime
import os

ARQUIVO = "diario.txt"

def salvar_anotacao():
    texto = input("\nDigite sua anotação:\n> ").strip()
    if texto:
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(ARQUIVO, "a", encoding="utf-8") as f:
            f.write(f"[{data_hora}] {texto}\n")
        print("✅ Anotação salva com sucesso!")
    else:
        print("⚠️ A anotação está vazia!")

def mostrar_anotacoes():
    if not os.path.exists(ARQUIVO):
        print("📘 O diário ainda está vazio.")
        return

    print("\n📚 Anotações salvas:")
    print("-" * 40)
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        print(f.read())
    print("-" * 40)

def menu():
    while True:
        print("\n📘 Diário Eletrônico")
        print("1. Escrever nova anotação")
        print("2. Ver anotações")
        print("3. Sair")

        opcao = input("Escolha uma opção (1/2/3): ").strip()

        if opcao == "1":
            salvar_anotacao()
        elif opcao == "2":
            mostrar_anotacoes()
        elif opcao == "3":
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

# Executar o menu principal
if __name__ == "__main__":
    menu()