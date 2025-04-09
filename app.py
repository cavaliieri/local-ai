from ollama import Client
from colorama import Fore,  init
import time
import os
import sys


init(autoreset=True)

client = Client(host='http://localhost:11434')


def digitando(texto, delay=0.03):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_nome():
    limpar_terminal()
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "BEM-VINDO AO ASSISTENTE IA LOCAL")
    print(Fore.CYAN + "=" * 50)
    return input(Fore.GREEN + "\nDigite seu nome: ")

# Início
name_user = obter_nome()
message_history = []

while True:
    limpar_terminal()
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + f" Chat IA Local - Mistral | Usuário: {name_user}")
    print(Fore.CYAN + "=" * 60)

    prompt_user = input(Fore.BLUE + f"\n{name_user}: ")

    if prompt_user.lower() in ["sair", "exit", "quit"]:
        print(Fore.RED + "\nEncerrando o chat. Até mais!\n")
        break

    message_history.append({"role": "user", "content": prompt_user})

    print(Fore.GREEN + "\nIA está digitando...\n")
    response = client.chat(model="mistral", messages=message_history)

    reply = response["message"]["content"]
    digitando(Fore.MAGENTA + "IA: " + reply)
    message_history.append({"role": "assistant", "content": reply})

    input(Fore.CYAN + "\nPressione ENTER para continuar...")