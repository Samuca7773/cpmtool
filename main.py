from time import sleep
import os
import requests
from rich.console import Console
from CarParkingMultiTool import LoginCarParking

url = 'https://Samuca007.pythonanywhere.com'

console = Console()
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pause():
    console.input(' [bold white]..pressione enter para continuar..')
    
    
def create_account():
    clear()
    console.print("  [bold cyan]![/bold cyan] [bold white]Opção escolhida[/bold white] > [bold cyan]Criar Conta[/bold cyan]")
    account_username = console.input(' [[bold cyan]?[/bold cyan]] [bold white]Digite um username[/bold white] >> ')
    account_password = console.input(' [[bold cyan]?[/bold cyan]] [bold white]Crie um senha[/bold white] >> ')
    account_password_confirm = console.input(' [[bold cyan]?[/bold cyan]] [bold white]Confirme sua senha[/bold white] >> ')
    
    if account_password != account_password_confirm:
        console.print(" [[bold cyan]![/bold cyan]] [bold white]As senhas não coincidem![/bold white]")
        sleep(2)
        start()
    if not account_password or not account_password_confirm or not account_username:
        console.print(" [[bold cyan]![/bold cyan]] [bold white]Nada pode ficar em branco![/bold white]")
        pause()
        start()
        
    data = {
        "account_username": account_username,
        "account_password": account_password
    }
    response = requests.post(f"{url}/account_register", json=data)
    if response.status_code == 201:
        console.print(" [[bold cyan]![/bold cyan]] [bold white]Conta criada com sucesso![/bold white]")
        sleep(2)
        console.print(" [[bold cyan]![/bold cyan]][bold white] Faça login para continuar! [/bold white]")
        pause()
        start()
    elif response.status_code == 409:
        console.print(' [[bold cyan]![/bold cyan]] [bold white]Esse username já está registrado em outra conta! [/bold white] ')
        pause()
        start()
    elif response.status_code == 500:
        console.print(f" [[bold cyan]![/bold cyan]] [bold white] Erro ao se conectar com o db: {response.json().get('message')}[/bold white]")
        pause()
        start()
        
def login():
    clear()
    console.print("  [bold cyan]![/bold cyan] [bold white]Opção escolhida[/bold white] > [bold cyan]Login[/bold cyan]")
    
    global account_username
    account_username = console.input(' [[bold cyan]?[/bold cyan]] [bold white] Digite seu username[/bold white] >> ')
    account_password = console.input(' [[bold cyan]?[/bold cyan]] [bold white] Digite sua senha >> ')
    
    if not account_username or not account_password:
        console.print(" [[bold cyan]![/bold cyan]] [bold white]Nada pode ficar em branco![/bold white]")
        pause()
        start()
    
    data = {
        "account_username": account_username,
        "account_password": account_password
    }
    
    response = requests.post(f"{url}/account_login", json=data)
    
    if response.status_code == 404:
        console.print(" [[bold cyan]![/bold cyan]] [bold white] Usuário não encontrado![/bold white]")
        pause()
        start()
    elif response.status_code == 401:
        console.print(" [[bold cyan]![/bold cyan]] [bold white] Senha incorreta![/bold white]")
        pause()
        start()
    elif response.status_code == 200:
        console.print(" [[bold cyan]![/bold cyan]] [bold white]Acesso liberado![/bold white]")
        sleep(2)
        menu()
        
    elif response.status_code == 500:
        console.print(f" [[bold cyan]![/bold cyan]] [bold white]Erro ao se conectar com o db: {response.json().get('message')}[/bold white]")
        pause()
        start()
    else:
        console.print(" [[bold cyan]![/bold cyan]] [bold white]Erro ao tentar fazer login![/bold white]")
        pause()
        start()
def start():
    clear()
    console.print('  [bold cyan]?[/bold cyan] [bold white]Digite a opção desejada:[/bold white] ')
    console.print(' [[bold cyan]01[/bold cyan]] [bold white]Criar Conta[/bold white]')
    console.print(' [[bold cyan]02[/bold cyan]] [bold white]Login[/bold white]')
    
    service = console.input(' [bold white] >> [/bold white]')
    
    if not service:
        console.print(' [[bold cyan]![/bold cyan]][bold white] Você não pode deixar em branco![/bold white]')
        sleep(2)
        start()
    if service == '1':
        create_account()
    elif service == '2':
        login()
    else:
        console.print(' [[bold cyan]![/bold cyan]] [bold white]Opção inválida, tente novamente![/bold white]')
        sleep(2)
        start()

def menu():
    clear()
    try:
        response = requests.get(f"{url}/account_info/{account_username}")
        if response.status_code == 200:
            data = response.json()
            console.print(" [bold white]Informações do usuário:[/bold white]")
            account_username_info = data.get('account_username')
            account_balance = data.get('balance')
            console.print(f' [[bold cyan]![/bold cyan]] [bold white]Username[/bold white] > [bold cyan]{account_username_info}[/bold cyan]')
            console.print(f" [[bold cyan]![/bold cyan]] [bold white]Dinheiro[/bold white] > [bold cyan]{account_balance}[/bold cyan]")
            console.print(" [[bold cyan]![/bold cyan]] [bold white]Desenvolvido por[/bold white] > [bold cyan]t.me/Samuca_007[/bold cyan]")
            console.print("\n [bold white]Menu Principal: ")
           
            # Servicos de Car Parking
            
            # 1 - Injetar Coins
            console.print(" [[bold cyan]01[/bold cyan]] [bold white]Injetar Coins               [/bold white] [ 400 ]")
            # 2 - Injetar Dinheiro
            console.print(" [[bold cyan]02[/bold cyan]] [bold white]Injetar Dinheiro            [/bold white] [ 400 ]")
            # 3 - Liberar Carros 
            console.print(" [[bold cyan]03[/bold cyan]] [bold white]Liberar Todos Carros        [/bold white] [[bold cyan] 1K  [/bold cyan]]")
             # 4 - Liberar Roupas
            console.print(" [[bold cyan]04[/bold cyan]] [bold white]Liberar Todas As Roupas     [/bold white] [ 300 ]")
             # 5 - Liberar animações 
            console.print(" [[bold cyan]05[/bold cyan]] [bold white]Liberar Todas As Animações  [/bold white] [ 300 ]")
            # 6 - Excluir Conta
            console.print(" [[bold cyan]06[/bold cyan]] [bold white]Excluir conta [/bold white]               [ 200 ]")
            # 7 - Liberar Rodas
            console.print(" [[bold cyan]07[/bold cyan]] [bold white]Desbloquear Rodas[/bold white]            [ 300 ]")
            # 8 - Nome grande
            console.print(" [[bold cyan]08[/bold cyan]] [bold white]Nome grande  [/bold white]                [ 300 ]")
            # 9 - ID Personalizado
            console.print(" [[bold cyan]09[/bold cyan]] [bold white]ID Personalizado[/bold white]             [ 500 ]")
            console.print("\n")
            service = console.input(' [[bold cyan]?[/bold cyan]] [bold white]Digite a opção desejada[/bold white] >> ')
            
            # Verificar Servicos
            # Hack Coin
            if service == '1':
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                try:
                    client = LoginCarParking(email=account_email, password=account_password)
                    console.print(f" [[bold cyan]![/bold cyan]] [bold white]Quantidade de coins do usuário: [/bold white]{client.data_account.coin}")
                    login = True
                   
                except Exception as err:
                    console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {err}[/bold white]")
                    login = False
                    sleep(2)
                    menu()
                
                coins = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite a quantidade de coins que deseja >> [/bold white] >> ")
                if not coins:
                    console.print(" [[bold cyan]?[/bold cyan]] [bold white]Digite um número válido![/bold white]")
                    sleep(2)
                    menu()
                    
                coins_int = int(coins)
                if coins_int > 500000:
                    console.print(" [[bold cyan]?[/bold cyan]][bold white] Você não pode injetar coins acima de 500.000![/bold white]")
                    sleep(2)
                    menu()
                
                if login == True:
                    data = {
                        'account_username': account_username,
                        'item': 'coin'
                    }
                    response = requests.post(f"{url}/buy_item", json=data)
                    if response.status_code == 200:
                        client.hack_coin(coins_int)
                        console.print(f" [[bold cyan]![/bold cyan]][bold white] Coins alterados![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel alterar os coins![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
            # Hack Money
            elif service == '2':
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                try:
                    client = LoginCarParking(email=account_email, password=account_password)
                    console.print(f" [[bold cyan]![/bold cyan]] [bold white]Quantidade de dinheiro do usuário: [/bold white]{client.data_account.money}")
                    login = True
                   
                except Exception as err:
                    console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {err}[/bold white]")
                    login = False
                    sleep(2)
                    menu()

                money = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite a quantidade de dinheiro[/bold white] >> ")
                if not money:
                    console.print(" [[bold cyan]?[/bold cyan]] [bold white]Digite um número válido![/bold white]")
                    sleep(2)
                    menu()
                    
                money_int = int(money)
                if money_int > 50000000:
                    console.print(" [[bold cyan]?[/bold cyan]][bold white] Você não pode injetar dinheiro acima de 50.000.000![/bold white]")
                    sleep(2)
                    menu()

                
                if login == True:
                    data = {
                        'account_username': account_username,
                        'item': 'money'
                    }
                    response = requests.post(f"{url}/buy_item", json=data)
                    if response.status_code == 200:
                        client.hack_money(money_int)
                        console.print(f" [[bold cyan]![/bold cyan]][bold white] Dinheiro alterado![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel alterar o dinheiro![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
            # Liberar carros
            elif service == '3':
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                try:
                    client = LoginCarParking(email=account_email, password=account_password)
                    login = True
                except Exception as err:
                    console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {err}[/bold white]")
                    login = False
                    sleep(2)
                    menu()

                if login == True:
                    data = {
                        'account_username': account_username,
                        'item': 'car'
                    }
                    response = requests.post(f"{url}/buy_item", json=data)
                    if response.status_code == 200:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Liberando carros, aguarde..[/bold white]")
                        client.unlock_all_car()
                        console.print(f" [[bold cyan]![/bold cyan]][bold white] Carros liberados![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel liberar os carros![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
            # Liberar roupas
            elif service == '4':
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                try:
                    client = LoginCarParking(email=account_email, password=account_password)
                    login = True
                except Exception as err:
                    console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {err}[/bold white]")
                    login = False
                    sleep(2)
                    menu()

                if login == True:
                    data = {
                        'account_username': account_username,
                        'item': 'look'
                    }
                    response = requests.post(f"{url}/buy_item", json=data)
                    if response.status_code == 200:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Liberando roupas, aguarde..[/bold white]")
                        client.unlock_all_cosmetic()
                        console.print(f" [[bold cyan]![/bold cyan]][bold white] Roupas liberadas![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel liberar as roupas![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
            # Liberar animações
            elif service == '5':
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                try:
                    client = LoginCarParking(email=account_email, password=account_password)
                    login = True
                except Exception as err:
                    console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {err}[/bold white]")
                    login = False
                    sleep(2)
                    menu()

                if login == True:
                    data = {
                        'account_username': account_username,
                        'item': 'animation'
                    }
                    response = requests.post(f"{url}/buy_item", json=data)
                    if response.status_code == 200:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Liberando animações, aguarde..[/bold white]")
                        client.unlock_animations()
                        console.print(f" [[bold cyan]![/bold cyan]][bold white] Animações liberadas![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel liberar as animações![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
            
            # Deletar conta
            elif service == "6":
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                
                try:
                    client = LoginCarParking(email=account_email, password=account_password)
                    login = True
                except Exception as err:
                    console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {err}[/bold white]")
                    login = False
                    sleep(2)
                    menu()
                
                if login == True:
                    data = {
                        'account_username': account_username,
                        'item': 'delete'
                    }
                    response = requests.post(f"{url}/buy_item", json=data)
                    if response.status_code == 200:
                        confirm = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite 'confirmar' para excluir a conta[/bold white] >> ")
                        if confirm == 'confirmar':
                            try:
                                client.delete_account()
                                console.print(" [[bold cyan]![/bold cyan]][bold white] Conta deletada![/bold white]")
                                sleep(2)
                                menu()
                            except Exception as err:
                                console.print(f" [[bold cyan]![/bold cyan]][bold white] Não foi possivel excluir a conta: {err}")
                                sleep(2)
                                menu()
                        else:
                            console.print(" [[bold cyan]![/bold cyan]][bold white] Você não confirmou a exclusão de conta![/bold white]")
                            sleep(2)
                            menu()
                        
                    elif response.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel liberar as animações![/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
                    elif response.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
            
            # Liberar Rodas
            elif service == "7":
                base_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key\u003dAIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                data = {
                    "email": account_email,
                    "password": account_password,
                    "returnSecureToken": True
                }
                headers = {
                    "Content-Type": "application/json",
                    "Accept-Language": "pt-BR, en-US"
                }
                response = requests.post(base_url, headers=headers, json=data)
                login = False
                if response.status_code == 400:
                    console.print(" [[bold cyan]?[/bold cyan]][bold white] Erro: Email ou senha inválidos[/bold white]")
                    sleep(2)
                    menu()
                else:
                    login = True
                    data_buy = {
                        'account_username': account_username,
                        'item': 'wheels'
                    }
                    response_buy = requests.post(f"{url}/buy_item", json=data_buy)
                    if response_buy.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel liberar as rodas![/bold white]")
                        sleep(2)
                        menu()
                    elif response_buy.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
                    elif response_buy.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    elif response_buy.status_code == 200:
                        
                        data = response.json()
                        idToken = data.get("idToken")
                        save_url = "https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5"
                        headers_save = {
                            "Host": "us-central1-cp-multiplayer.cloudfunctions.net",
                            "Authorization": f"Bearer {idToken}",
                            "Content-Type": "application/json",
                            "User-Agent": "okhttp/3.12.13"
                        }
                        data_save = {
                            "data": "{\"wheels\":[118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210]}"
                        }
                        response = requests.post(save_url, headers=headers_save, json=data_save)
                        if response.status_code == 200:
                            console.print(" [[bold cyan]![/bold cyan]] [bold white]Rodas liberadas![/bold white]")
                            sleep(2)
                            menu()
                        else:
                            console.print(" [[bold cyan]![/bold cyan]] [bold white]Não foi possivel liberar as rodas![/bold white]")
                            sleep(2)
                            menu()
                           
            # Nome grande
            elif service == '8':
                base_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key\u003dAIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                new_name = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite o novo nome[/bold white] >> ")
                data = {
                    "email": account_email,
                    "password": account_password,
                    'returnSecureToken': True
                }
                headers = {
                    "Content-Type": "application/json",
                    "Accept-Language": "pt-BR, en-US"
                }
                response = requests.post(base_url, json=data, headers=headers)
                login = False
                if response.status_code == 400:
                    console.print(" [[bold cyan]?[/bold cyan]][bold white] Erro: Email ou senha inválidos[/bold white]")
                    sleep(2)
                    menu()
                    
                else:
                    login = True
                    data_buy = {
                        'account_username': account_username,
                        'item': 'name_raimbow'
                    }
                    response_buy = requests.post(f"{url}/buy_item", json=data_buy)
                    if response_buy.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel alterar o nome![/bold white]")
                        sleep(2)
                        menu()
                    elif response_buy.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
                    elif response_buy.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    
                    elif response_buy.status_code == 200:
                        data = response.json()
                        idToken = data.get("idToken")
                        save_url = "https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5"
                        headers_save = {
                            "Host": "us-central1-cp-multiplayer.cloudfunctions.net",
                            "Authorization": f"Bearer {idToken}",
                            "Content-Type": "application/json",
                            "User-Agent": "okhttp/3.12.13"
                        }
                        data = {
                            "data": "{\"Name\":\"" + new_name + "\"}"
                        }
                        response = requests.post(save_url, headers=headers_save, json=data)
                        if response.status_code == 200:
                        
                            console.print(" [[bold cyan]![/bold cyan]] [bold white]Nome alterado![/bold white]")
                            sleep(2)
                            menu()
                        else:
                            console.print(" [[bold cyan]![/bold cyan]] [bold white]Não foi possivel alterar o nome![/bold white]")
                            sleep(2)
                            menu()
            
            # ID Personalizado
            elif service == "9":

                base_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key\u003dAIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
                account_email = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite seu email[/bold white] >> ")
                account_password = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite sua senha[/bold white] >> ")
                new_id = console.input(" [[bold cyan]?[/bold cyan]][bold white] Digite o novo ID[/bold white] >> ")
                data = {
                    "email": account_email,
                    "password": account_password,
                    'returnSecureToken': True
                }
                headers = {
                    "Content-Type": "application/json",
                    "Accept-Language": "pt-BR, en-US"
                }
                response = requests.post(base_url, json=data, headers=headers)
                login = False
                if response.status_code == 400:
                    console.print(" [[bold cyan]?[/bold cyan]][bold white] Erro: Email ou senha inválidos[/bold white]")
                    sleep(2)
                    menu()
                    
                else:
                    login = True
                    data_buy = {
                        'account_username': account_username,
                        'item': 'localid'
                    }
                    response_buy = requests.post(f"{url}/buy_item", json=data_buy)
                    if response_buy.status_code == 404:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Não foi possivel alterar o ID![/bold white]")
                        sleep(2)
                        menu()
                    elif response_buy.status_code == 500:
                        console.print(f" [[bold cyan]?[/bold cyan]][bold white]Erro: {response.json().get('message')}[/bold white]")
                        sleep(2)
                        menu()
                    elif response_buy.status_code == 403:
                        console.print(" [[bold cyan]![/bold cyan]][bold white] Saldo insuficiente![/bold white]")
                        sleep(2)
                        menu()
                    
                    elif response_buy.status_code == 200:
                        data = response.json()
                        idToken = data.get("idToken")
                        save_url = "https://us-central1-cp-multiplayer.cloudfunctions.net/SavePlayerRecordsPartially5"
                        headers_save = {
                            "Host": "us-central1-cp-multiplayer.cloudfunctions.net",
                            "Authorization": f"Bearer {idToken}",
                            "Content-Type": "application/json",
                            "User-Agent": "okhttp/3.12.13"
                        }
                        data = {
                            "data": "{\"localID\":\"" + new_id + "\"}"
                        }
                        response = requests.post(save_url, headers=headers_save, json=data)
                        if response.status_code == 200:
                        
                            console.print(" [[bold cyan]![/bold cyan]] [bold white]ID alterado![/bold white]")
                            sleep(2)
                            menu()
                        else:
                            console.print(" [[bold cyan]![/bold cyan]] [bold white]Não foi possivel alterar o ID![/bold white]")
                            sleep(2)
                            menu()
                            
        
        
        elif response.status_code == 500:
            console.print(f" [[bold cyan]![/bold cyan]][bold white]Erro ao se conectar com o db: {response.json().get('message')}[/bold white]")
            pause()
            start()
        elif response.status_code == 404:
            console.print(f" [[bold cyan]![/bold cyan]][bold white]Não foi possivel acessar suas informações![/bold white]")
            pause()
            start()
    except Exception as err:
        console.print(f" [[bold cyan]![/bold cyan]] Erro: {err}")
if __name__ == "__main__":
    start()
