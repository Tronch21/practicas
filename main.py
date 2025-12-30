#Ventas totales por mes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos desde un archivo CSV
customers = pd.read_csv('archives/customers.csv')
products = pd.read_csv('archives/products.csv')
transactions = pd.read_csv('archives/transactions.csv')

transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date']) 
"""
print("Customers:")
print(customers.head(), "\n")

print("Products:")
print(products.head(), "\n")

print("Transactions:")
print(transactions.head())

ventas_mes = transactions["transaction_date"].dt.month
# Ventas totales por mes
print(transactions.groupby(ventas_mes)["total_amount"].sum())
"""
print("Ventas por cliente: ")



topClientes = transactions.groupby("customer_id")["total_amount"].sum().sort_values(ascending=False)
print(topClientes.head(10))
print()
