from flight_api import (
    get_direct_price,
    get_hidden_city_price
)

from config import (
    HIDDEN_CITY_DESTS,
    THRESHOLD
)

direct_price = get_direct_price()

print(f"URC-CAN: {direct_price}")

for dest in HIDDEN_CITY_DESTS:

    hidden_price = get_hidden_city_price(dest)

    diff = direct_price - hidden_price

    print(
        f"URC-CAN-{dest} "
        f"{hidden_price} "
        f"差价:{diff}"
    )

    if diff >= THRESHOLD:

        print(
            f"发现低价弃程票: "
            f"{dest} "
            f"节省 {diff} 元"
        )