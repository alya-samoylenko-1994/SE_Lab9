import csv
import streamlit as st
import matplotlib.pyplot as plt


ticket_prices = {1: 0, 2: 0, 3: 0}

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        pclass = int(row[2])
        fare = float(row[9])
        ticket_prices[pclass] += fare

for pclass, total_price in ticket_prices.items():
    print(f"Суммарная стоимость билетов для класса {pclass}: {total_price}")
