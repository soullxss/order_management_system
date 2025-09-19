import pandas as pd
import matplotlib.pyplot as plt

def visualize_orders(dataframe):
    orders_per_date = dataframe.groupby('date').size()
    orders_per_date.plot(kind='bar')
    plt.title('Динамика количества заказов по датам')
    plt.xlabel('Дата')
    plt.ylabel('Количество заказов')
    plt.show()
