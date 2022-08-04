from __future__ import print_function, unicode_literals

import socket

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from pyfiglet import Figlet

from constants import CROSS_1_PORT, CROSS_2_PORT, LOCAL_IP


if __name__ == "__main__":
    cross_1_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cross_1_server.connect((LOCAL_IP, CROSS_1_PORT))
    cross_2_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cross_2_server.connect((LOCAL_IP, CROSS_2_PORT))


    f = Figlet(font="slant")
    print(f.renderText("Sistema de semaforos"))

    style = style_from_dict({
        Token.QuestionMark: "#E91E63 bold",
        Token.Selected: "#673AB7 bold",
        Token.Instruction: "",  # default
        Token.Answer: "#2196f3 bold",
        Token.Question: "",
    })


    print("Olá! Seja bem-vindo ao sistem de semáforos.\n\n")

    questions = [
        {
            "type": "list",
            "name": "command",
            "message": "Qual comando gostaria de executar?",
            "choices": ["Ligar modo noturno", "Ligar modo de emergência"],
        },
    ]

    answers = prompt(questions, style=style)

    if answers["command"] == "Ligar modo noturno":
        cross_1_server.send(bytes("1", "utf-8"))
    elif answers["command"] == "Ligar modo de emergência":
        cross_1_server.send(bytes("2", "utf-8"))
