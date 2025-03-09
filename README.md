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

## Regras para identificar cada tipo de bandeira do cartão:

1. **American Express**:

   - Começa com os dígitos 34 ou 37.
   - Comprimento do número do cartão: 15 dígitos.

2. **Visa**:

   - Começa com o dígito 4.
   - Comprimento do número do cartão: 13 ou 16 dígitos.

3. **MasterCard**:

   - Começa com os dígitos 51 a 55.
   - Comprimento do número do cartão: 16 dígitos.

4. **Discover**:

   - Começa com os dígitos 6011, 622126-622925, 644-649, ou 65.
   - Comprimento do número do cartão: 16 dígitos.

5. **JCB**:

   - Começa com os dígitos 3528-3589.
   - Comprimento do número do cartão: 16 dígitos.

6. **Diners Club**:

   - Começa com os dígitos 300-305, 36 ou 38.
   - Comprimento do número do cartão: 14 dígitos.

7. **EnRoute**:

   - Começa com os dígitos 2014 ou 2149.
   - Comprimento do número do cartão: 15 dígitos.

8. **Voyager**:

   - Começa com o dígito 8699.
   - Comprimento do número do cartão: 15 dígitos.

9. **Hipercard**:

   - Começa com o dígito 38.
   - Comprimento do número do cartão: 13, 16 ou 19 dígitos.

10. **Alura**:

    - Começa com os dígitos 606282.
    - Comprimento do número do cartão: 16 dígitos.

    Sinta-se à vontade para contribuir com melhorias ou correções!
