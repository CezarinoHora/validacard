def get_card_brand(card_number):
    # Converte o número do cartão para uma string eliminando espaços vazios
    card_number = str(card_number).replace(" ", "")
    
    # Verifica se é American Express: começa com 34 ou 37 e tem 15 dígitos
    if card_number.startswith(('34', '37')) and len(card_number) == 15:
        return "American Express"
    
    # Verifica se é Visa: começa com 4 e tem 13, 16 ou 19 dígitos
    elif card_number.startswith('4') and len(card_number) in [13, 16, 19]:
        return "Visa"
    
    # Verifica se é MasterCard: começa com 51-55 e tem 16 dígitos
    elif card_number.startswith(('51', '52', '53', '54', '55')) and len(card_number) == 16:
        return "MasterCard"
    
    # Verifica se é Discover: começa com 6011, 622126-622925, 644-649 ou 65 e tem 16 dígitos
    elif card_number.startswith('6011') or card_number.startswith(('622126', '622925')) or card_number.startswith(('644', '645', '646', '647', '648', '649')) or card_number.startswith('65') and len(card_number) == 16:
        return "Discover"
    
    # Verifica se é JCB: começa com 35 e tem 16 dígitos
    elif card_number.startswith('35') and len(card_number) == 16:
        return "JCB"
    
    # Verifica se é Diners Club: começa com 36 e tem 14 dígitos
    elif card_number.startswith('36') and len(card_number) == 14:
        return "Diners Club"
    
    # Verifica se é EnRoute: começa com 2014 ou 2149 e tem 15 dígitos
    elif card_number.startswith(('2014', '2149')) and len(card_number) == 15:
        return "EnRoute"
    
    # Verifica se é Voyager: começa com 8699 e tem 15 dígitos
    elif card_number.startswith('8699') and len(card_number) == 15:
        return "Voyager"
    
    # Verifica se é Hipercard: começa com 606282 e tem 16 dígitos
    elif card_number.startswith('606282') and len(card_number) == 16:
        return "Hipercard"
    
    # Verifica se é Alura: começa com 50 e tem 16 dígitos
    elif card_number.startswith('50') and len(card_number) == 16:
        return "Alura"
    
    # Se nenhuma das condições acima for atendida, retorna "Desconhecido"
    else:
        return "Desconhecido"

# Exemplo de uso
if __name__ == "__main__":
    card_number = input("Digite o número do seu cartão de crédito: ")
    print(f"A bandeira do cartão é: {get_card_brand(card_number)}")