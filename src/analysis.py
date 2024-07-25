import pandas as pd

def run_analysis():
    data = pd.read_csv('data/Auto Sales data.csv')
    total_sales = data['Sales'].sum()
    average_sales = data['Sales'].mean()
    return {'total_sales': total_sales, 'average_sales': average_sales}
 
