# IA Local com Mistral (Ollama)

Este projeto é um chatbot simples rodando **localmente** no terminal com o modelo **Mistral**, utilizando a API do [Ollama](https://ollama.com/). Ideal para testar IA de forma offline e com privacidade.

---

# IA Local com Mistral rodando via Ollama

Este projeto é uma interface de terminal para interagir com o modelo de linguagem Mistral localmente utilizando o Ollama.

## 📁 Clonando o repositório

```bash
git clone https://github.com/cavaliieri/local-ai.git
cd local-ai
```

## 🛠️ Instalação

1. Certifique-se de que o [Ollama](https://ollama.com/download) esteja instalado e em execução em sua máquina.
2. Execute o comando para baixar o modelo Mistral:
```bash
ollama run mistral
```
3. Instale as dependências Python:
```bash
pip install ollama
```

## ▶️ Como usar

Execute o script principal no terminal:
```bash
python app.py
```
O terminal pedirá seu nome e você poderá interagir com a IA local.

Digite `sair` para encerrar o chat.

## 💡 Exemplo de uso

```bash
====== Bem vindo a IA  =========

Digite sua pergunta:
> Qual a capital da França?
IA: A capital da França é Paris.
```

## 🧠 Modelo Utilizado

- **Mistral 7B** rodando localmente via Ollama.

## 🧱 Estrutura do Projeto

```
local-ai/
│
├── app.py               # Script principal com o chat no terminal
├── README.md            # Este arquivo
└── requirements.txt     # Dependências do projeto (opcional)
```

## 🧰 Tecnologias Utilizadas

- Python 3.x
- Ollama
- Mistral 7B
- Terminal (modo texto)

## 📬 Contato

Entre em contato comigo:

- GitHub: [@cavaliieri](https://github.com/cavaliieri)
- Email: lbcavalieri@gmail.com
