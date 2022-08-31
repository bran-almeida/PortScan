import socket

def get_ports_range():
    """
        Realiza um get da porta inicial e final do scan e faz tratamento de erros das  entradas.
    """
    while True:
        try:
            print("-"*50)
            start_port = int(input("Informe a porta inicial:\n"))
            if start_port >= 0 and start_port <= 65000:
                end_port = int(input("Informe a porta final:\n"))
                if end_port >= 0 and end_port <= 65000:
                    if end_port < start_port:
                        print("Erro: A porta final informada é menor que a porta inicial!")
                        continue
                    else:
                        return (start_port, end_port)
            else:
                print("Valor inválido, informe um valor entre 0 e 65000.")
        except ValueError as error:
            print("Valor inválido, informe um valor entre 0 e 65000.")

def connection():
    """
        Instancia o objeto client e seta timeout de 0.5 seg
    """
    #Cria o objeto cliente com os seguintes parâmetros AF_INET: Familia IPV4 | SOCK_STREAM: Protocolo TCP 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Seta o tempo limite da tentativa de conexão
    client.settimeout(0.5)
    return client

if __name__ == "__main__": 
    while True:
        print("-"*50)
        host = str(input("Informe o IP ou URL do alvo:\n"))
        print("-"*50)
        menu = str(input("[1] Escanear porta específica\n[2] Escanear range de portas\n>>>"))
        if menu == "1":
            try:
                port = int(input("Informe a porta para escaneamento:\n"))
                if port >= 0 and port <= 65000:
                    client = connection()
                     #O metodo connect_ex, apenas informa o sucesso ou não da conexão.
                    status_code = client.connect_ex((host, port))
                    if status_code == 0:
                        print(f"[+] {port} open.")
                        break
                    print(f"[+] {port} closed.")
                    break
            except ValueError as error:
                print("Valor inválido, informe um valor entre 0 e 65000.")

        elif menu == "2":
            ports = get_ports_range()
            for p in range(ports[0], ports[1]+1):
                client = connection()
                status_code = client.connect_ex((host, p))
                if status_code == 0:
                    print(f"[+] {p} open.")
                else:
                    print(f"[+] {p} closed.")
            break
        else:
            print("Por favor informe uma opção valida 1 ou 2")
