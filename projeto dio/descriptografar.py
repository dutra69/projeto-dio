import os
from cryptography.fernet import Fernet


def carregar_chave():
    return open("chave.key", "rb").read()


def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    
    # O método correto é decrypt (sem o 's')
    dados_descriptografados = f.decrypt(dados)
    
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)


def encontrar_arquivos(diretorio):
    lista = []
    # Ajustada a indentação que estava desalinhada aqui
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            # Evita tentar descriptografar o próprio script, a chave ou a mensagem de texto
            if nome != "ransomware.py" and not nome.endswith(".key") and nome != "LEIA_ISSO.txt":
                lista.append(caminho)
    return lista


def main():
    pasta_teste = "teste_files"
    
    if not os.path.exists("chave.key"):
        print("Erro: O arquivo 'chave.key' não foi encontrado! Não é possível descriptografar.")
        return

    chave = carregar_chave()
    arquivos = encontrar_arquivos(pasta_teste)
    
    if not arquivos:
        print(f"Nenhum arquivo encontrado em '{pasta_teste}' para descriptografar.")
        return

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
        print(f"Arquivo restaurado: {arquivo}")

    # Remove o bilhete de resgate se ele existir
    if os.path.exists("LEIA_ISSO.txt"):
        os.remove("LEIA_ISSO.txt")
        
    print("\nTodos os arquivos foram restaurados com sucesso!")


if __name__ == "__main__":
    main()