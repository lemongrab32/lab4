from parser import parse


def calc(currency, value, desired):
    if (isinstance(value, int) == False) and (isinstance(value, float) == False):
        return "TypeError"
    if value < 0:
        return "ValueError"
    if currency == "RUB":
        if desired == currency:
            return value
        else:
            new = parse(desired)
            result = float(value) / new
            return float('{:.4f}'.format(result))
    else:
        if desired == "RUB":
            result = float(value) * parse(currency)
            return float('{:.4f}'.format(result))
        if desired == currency:
            return value
        else:
            val1 = parse(desired)
            val2 = parse(currency)
            result = (float(val2) / float(val1)) * float(value)
            return float('{:.4f}'.format(result))