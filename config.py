import os

EMAIL_TO = os.getenv("EMAIL_TO", "2838658340@qq.com")
QQ_SMTP_AUTH = os.getenv("QQ_SMTP_AUTH", "test")

FROM_EMAIL = "2838658340@qq.com"

ORIGIN = "URC"
DESTINATION = "CAN"

TARGET_DATE = "2026-09-05"

THRESHOLD = 300

HIDDEN_CITY_DESTS = [
    "SZX",
    "ZUH",
    "NNG",
    "HAK",
    "FOC",
    "XMN"
]