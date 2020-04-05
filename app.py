from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/<texto>')
def index(texto):
    return str.upper(texto)

@app.route('/yorn')
def yesorno():
    resp = randint(0,2)

    if resp == 1:
        return "Sim"
    elif resp == 2:
        return "Talvez"
    else:
        return "Não"

@app.route('/poi/<numero>')
def poi(numero):
    num = int(numero)
    if num%2==0:
        return "Par"
    else:
        return "Ímpar"

@app.route('/descreve/<numero>')
def descreve_numero(numero):

    casas = len(numero)
    num = int(numero)

    nums = {
        1: "UM",
        2: "DOIS",
        3: "TRÊS",
        4: "QUATRO",
        5: "CINCO",
        6: "SEIS",
        7: "SETE",
        8: "OITO",
        9: "NOVE",
        0: "ZERO"
    }

    onzea19 = {
        
        11: "ONZE",
        12: "DOZE",
        13: "TREZE",
        14: "QUATORZE",
        15: "QUINZE",
        16: "DEZESSEIS",
        17: "DEZESSETE",
        18: "DEZOITO",
        19: "DEZENOVE"
    }

    dezenas = {
        1: "DEZ",
        2: "VINTE",
        3: "TRINTA",
        4: "QUARENTA",
        5: "CINQUENTA",
        6: "SESSENTA",
        7: "SETENTA",
        8: "OITENTA",
        9: "NOVENTA"
    }

    centenas = {
        1: "CEM",
        2: "DUZENTOS",
        3: "TREZENTOS",
        4: "QUATROCENTOS",
        5: "QUINHENTOS",
        6: "SEISCENTOS",
        7: "SETECENTOS",
        8: "OITOCENTOS",
        9: "NOVECENTOS"
    }

    message = ""

    if casas == 1:
        return "{}".format(nums[num])

    elif casas == 2:
        if numero[1] == "0":
            return "{}".format(dezenas[int(numero[0])])
        if numero[0] == "1":
            return "{}".format(onzea19[num])

        return "{} E {}".format(dezenas[int(numero[0])], nums[int(numero[1])])
    
    elif casas == 3:
        if numero[1] == "0":
            if numero[2] == "0":
                return centenas[int(numero[0])]
            else:
                return "{} E {}".format(centenas[int(numero[0])], nums[int(numero[2])])
            
        elif numero[1] == "1":
            if numero[2] == "0":
                return "{} E {}".format(centenas[int(numero[0])],dezenas[int(numero[1])])
        if numero[0] == "1":
            return "{} E {}".format(centenas[int(numero[0])],onzea19[int("{}".format(numero[1])+numero[2])])

        elif numero[1] != "0":
            if numero[2] == "0":
                return "{} E {}".format(centenas[int(numero[0])],dezenas[int(numero[1])])
            return "{} E {} E {}".format(centenas[int(numero[0])], dezenas[int(numero[1])], nums[int(numero[2])])
            
    else:
        return "NÚMERO INVÁLIDO"

if __name__ == '__main__':
    app.run(debug=True)