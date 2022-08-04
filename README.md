Aluno: Lucas Dutra Ferreira do Nascimento
Matrícula: 17/0050939

> Instale os requisitos do projeto na raíz antes da execução utilizando `pip3 install -r requirements.txt`

# Execução do projeto

Serão necessários 3 terminais para execução do projeto.

1. (Opcional) Pode ser necessário alterar o PYTHONPATH do ambiente, caso seja necessário basta executar export `PYTHONPATH="${PYTHONPATH}:/home/lucasnascimento/FSE-Trabalho1/"`
2. Dentro da pasta `/src` é necessário de dois terminais para inicializar ambos servidores
```
python3 distributed_system/cross_1.py
```
e

```
python3 distributed_system/cross_2.py
```
3. Em um novo terminal execute o servidor principal (interação com o sistema)
```
python3 client.py
```

4. Siga os comandos mostrados na linha de Comando

5. Caso seja necessário executar um novo comando, o programa `client.py` deve ser executado novamente

# Pontos implementados

* Conexão através TCP/IP com um client principal e outros dois distribuídos responsáveis pelas operações menores

* Comando de modo noturno

* Comando de modo de emergência

* Configuração do tempo máximo e mínimo de cada cor em cada sinal (principal ou secundário)