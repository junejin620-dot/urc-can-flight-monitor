def get_direct_price():
    return 1380


def get_hidden_city_price(destination):
    mock_prices = {
        "SZX": 980,
        "ZUH": 1100,
        "NNG": 950,
        "HAK": 1200,
        "FOC": 1250,
        "XMN": 1000
    }

    return mock_prices.get(destination)