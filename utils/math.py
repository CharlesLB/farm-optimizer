def get_int_value(value):
    return int(value + 1)


def float_to_cash(value):
    return f"R$ {value:.2f}".replace(".", ",")
