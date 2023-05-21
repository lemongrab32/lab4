from parser import parse


def calc(currency, value, desired):
    try:
        value = float(value)
    except ValueError:
        return 'ValueError: "' + value + '"' + ' - не является числом'
    except TypeError:
        return 'TypeError: недопустимое значение'
    if value < 0:
        return 'ValueError: (' + str(value) + ') меньше нуля'
    if currency == "RUB":
        if desired == currency:
            return value
        else:
            new = parse(desired)
            result = float(value) / new
            return "The answer is " + '{:.4f}'.format(result)
    else:
        if desired == "RUB":
            result = float(value) * parse(currency)
            return "The answer is " + '{:.4f}'.format(result)
        if desired == currency:
            return value
        else:
            val1 = parse(desired)
            val2 = parse(currency)
            result = (float(val2) / float(val1)) * float(value)
            return "The answer is " + '{:.4f}'.format(result)