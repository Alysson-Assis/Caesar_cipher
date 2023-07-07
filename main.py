alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(code, inc_txt, number):
    end = ""
    if code == "decode":
        number *= -1
    for let in inc_txt:
        if let in alphabet:
            position = alphabet.index(let)
            new_pos = position + number
            end += alphabet[new_pos]
        else:
            end += let
    print(f"Aqui está o {code}d resultado: {end}")



while input("Você quer codificar alguma frase? Digite 's' para sim, e 'n' para não: ") == "s":
    code = input("Digite 'encode' para criptografar, digite 'decode' para descriptografar:\n")
    text = input("Escreva a mensagem:\n")
    number = int(input("Qual o numero de troca:\n"))
    number = number % 26

    caesar(code=code, inc_txt=text, number=number)

print("Tchau, Tchau!")


