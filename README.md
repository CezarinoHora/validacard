# validacard
Criando um Validador de Bandeiras de Cartão de Crédito com o GitHub Copilot

Projeto faz parte do Desafio de projeto do Bootcamp Microsoft AI for Tech - GitHub Copilot
da DIO

Este projeto contém uma função chamada `get_card_brand`, que verifica a bandeira de um cartão de crédito com base no número fornecido. A função identifica várias bandeiras de cartões, incluindo:

- American Express
- Visa
- MasterCard
- Discover
- JCB
- Diners Club
- EnRoute
- Voyager
- Hipercard
- Alura

Se a bandeira do cartão não for reconhecida, a função retornará "Desconhecido".

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `Validacard.py`.
3. Execute o arquivo `Validacard.py` em um terminal ou prompt de comando.
4. Quando solicitado, insira o número do seu cartão de crédito.
5. O programa exibirá a bandeira do cartão correspondente.

## Instruções de instalação

Não há dependências externas necessárias para este projeto. Basta ter o Python instalado.

## Exemplo de uso

```python
if __name__ == "__main__":
    card_number = input("Digite o número do seu cartão de crédito: ")
    print(f"A bandeira do cartão é: {get_card_brand(card_number)}")
```

Sinta-se à vontade para contribuir com melhorias ou correções!
