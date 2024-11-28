import pandas as pd
import numpy as np
from sqlalchemy import create_engine

host = 'localhost'
user = 'root'
passaword = 'root'
database = 'bd_PM'

engine = create_engine(f'mysql+pymysql://{user}:{passaword}@{host}/{database}')

#Tabelas
df_pm = pd.read_sql('basedp', engine)
#print(df_pm)
df_policia = pd.read_sql('basedp_roubo_celular', engine)
#print(df_policia)

#Juntando as tabela por marge
base_pm = pd.merge(df_pm, df_policia, on='cod_ocorrencia')
#print(base_pm.head())

#Variavel
df_roubo = base_pm[['cod_ocorrencia', 'ano_x', 'aisp', 'roubo_celular']]
#print(df_roubo)

# comparação

#base_pm.columns = [col.strip().replace('\ufeff', '') for col in base_pm.columns]
df_roubo = df_roubo[(df_roubo['ano_x'] >= 2022) & (df_roubo['ano_x'] <= 2023)]
#print(df_roubo)

#toal
df_roubo = df_roubo.groupby('aisp').sum ('roubo_celular').reset_index()    
#print(df_roubo.head())

#Analise

print('Analisando..')

#media
array_roubo_celuar = np.array(df_roubo["roubo_celular"])
media_roubo = np.mean(array_roubo_celuar)
mediana_roubo = np.median(array_roubo_celuar)
print(mediana_roubo)

#quartil
q1 = np.quantile(array_roubo_celuar, 0.25)
q2 = np.quantile(array_roubo_celuar, 0.50)
q3 = np.quantile(array_roubo_celuar, 0.75)

#print(df_total_q3)