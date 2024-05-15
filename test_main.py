from main import count_prices


def test_count_prices_structure():
    data = []
    answer = count_prices(data)
    assert answer == {
        'Класс обслуживания': ['1', '2', '3'],
        'Цена билета (муж.)': [0, 0, 0],
        'Цена билета (жен.)': [0, 0, 0]
    }


def test_count_prices_no_sex():
    data = [list(str(i) for i in range(10)) for _ in range(10)]
    for i in range(len(data)):
        data[i][4] = None

    answer = count_prices(data)
    assert answer['Цена билета (муж.)'] == [0, 0, 0]
    assert answer['Цена билета (жен.)'] == [0, 0, 0]


def test_count_prices_common():
    data = [list(str(i) for i in range(10)) for _ in range(10)]
    for i in range(len(data)):
        data[i][4] = 'male' if i % 2 == 0 else 'female'

    data[1][2] = '1'
    data[2][2] = '2'
    data[3][2] = '3'
    data[4][2] = '1'

    answer = count_prices(data)
    assert answer['Цена билета (муж.)'] == [9.0, 36.0, 0]
    assert answer['Цена билета (жен.)'] == [9.0, 27.0, 9.0]
