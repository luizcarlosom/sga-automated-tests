# **Guia para Execução do Projeto**

Este projeto requer **Python 3.10 ou superior** e o **pip** instalados.  
Siga os passos abaixo para configurar e executar o projeto.

## **Passos para Configuração**

### **1º - Criar um ambiente virtual**
```
    Windows: python -m venv venv
    Linux: python3 -m venv venv
```

### **2º Entre no ambiente virtual**
```
    Windows: venv\Script\activate
    Linux ou Mac: source venv/bin/activate
```

### **3º Instale as dependencias do arquivo requirements.txt**
**Obs: Antes de executar se certifique que você já está no ambiente virtual**
```
    pip install -r requirements.txt
```

### **4º Crie um arquivo .env**
```
    Preencha com as informações do .env.example
```
## **5º Para executar os casos de testes individualmente**
```
    Windows: python CT00x.py
    Linux ou Mac: python3 CT00x.py
```

# *Atenção*

*Sempre que o teste for ser executado novamente é necessário alterar as informações na .env para que ele crie um novo usuário.*