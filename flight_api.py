from config import TARGET_DATE


def search_route(origin, destination, date):
    """
    后续这里接真实数据源
    """
    print(f"查询 {origin} -> {destination} {date}")

    mock_data = {
        ("URC", "CAN"): 1380,
        ("URC", "SZX"): 980,
        ("URC", "NNG"): 950,
        ("URC", "XMN"): 1000,
        ("URC", "ZUH"): 1100,
        ("URC", "HAK"): 1200,
        ("URC", "FOC"): 1250,
    }

    return mock_data.get((origin, destination))


def get_direct_price():
    return search_route(
        "URC",
        "CAN",
        TARGET_DATE
    )


def get_hidden_city_price(destination):
    return search_route(
        "URC",
        destination,
        TARGET_DATE
    )