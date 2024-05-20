import requests
from bs4 import BeautifulSoup

def get_cigar_data():
    url = "https://www.finestcubancigars.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    cigars = []

    try:
        products = soup.find_all('div', class_='product-item-info')

        for product in products:
            try:
                name_element = product.find('a', class_='product-item-link')
                if name_element:
                    name = name_element.text.strip()
                else:
                    name = "Nome não encontrado"

                price_element = product.find('span', class_='price')
                if price_element:
                    price = price_element.text.strip()
                else:
                    price = "Preço não encontrado"

                cigars.append({'name': name, 'price': price})
            except AttributeError as e:
                print(f"Erro ao extrair dados do produto: {e}")
                continue

    except Exception as e:
        print(f"Erro geral ao processar a página: {e}")

    return cigars

def display_cigar_data(cigars):
    if not cigars:
        print("Nenhum dado de charuto encontrado.")
        return

    for cigar in cigars:
        print(f"Nome: {cigar['name']}, Preço: {cigar['price']}")

def main():
    while True:
        cigar_data = get_cigar_data()
        display_cigar_data(cigar_data)
        
        user_input = input("Tecle 'c' para tentar novamente ou qualquer outra tecla para sair: ").strip().lower()
        if user_input != 'c':
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    main()
