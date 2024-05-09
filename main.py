import csv
import streamlit as st
import matplotlib.pyplot as plt


st.image('титаник.jpg')
st.header('Данные пассажиров Титаника')
st.text('Для просмотра данных конкретного пола выберите соответствующее')
st.text('значение в выпадающем списке')
sex = st.selectbox('Пол пассажира', ['Любой', 'муж.', 'жен.'])


def count_prices():
    ticket_prices_m = {'1': 0, '2': 0, '3': 0}
    ticket_prices_f = {'1': 0, '2': 0, '3': 0}

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            pclass = row[2]
            fare = float(row[9])
            sex = row[4]
            if sex == 'male':
                ticket_prices_m[pclass] += fare
            else:
                ticket_prices_f[pclass] += fare

    return {
            'Класс обслуживания': list(ticket_prices_m.keys()),
            'Цена билета (муж.)': list(ticket_prices_m.values()),
            'Цена билета (жен.)': list(ticket_prices_f.values())
        }


def main():
    data = count_prices()
    st.table(data)

    # for pclass, total_price in data.items():
    #     print(f"Суммарная стоимость билетов для класса {pclass}: {total_price}")
    fig = plt.figure(figsize=(10, 5))
    p_class = data['Класс обслуживания']
    male_price = data['Цена билета (муж.)']
    female_price = data['Цена билета (жен.)']

    if sex == 'Любой':
        plt.bar(p_class, male_price, width=0.3, label='Male', align='center')
        plt.bar(p_class, female_price, width=0.3, label='Female', color='pink', align='edge')
    elif sex == 'муж.':
        plt.bar(p_class, male_price, width=0.3, label='Male', align='center')
    else:
        plt.bar(p_class, female_price, width=0.3, label='Female', color='pink', align='edge')
    # Customizing the appearance of the plot
    plt.title('Цены билетов по классам обслуживания')
    plt.xlabel('Класс обслуживания')
    plt.ylabel('Цена билета')

    # Displaying the plot
    st.pyplot(fig)

main()
