import pandas as pd
import numpy as np
import math


#pre-processamento para utilizar apenas as colunas que possuem/"esperam" números:
def pre_processing():
    data = pd.read_excel('dataset.xlsx') #criei um csv utilizando o py e apaguei a linha de código
    number_columns = data.columns[data.dtypes != 'object']

    for column in number_columns:
        print(f'Na coluna [{column}]')
        get_outlier_with_z_score(data[column])


def get_outlier_with_z_score(data_set, cut=3):
    outliers = []
    invalid_data = 0
    mean = np.mean(data_set) #media da coluna
    detour = np.std(data_set) #desvio padrão da coluna
    print(f'a média é: {mean}')
    print(f'o desvio padrão é: {detour}')
    for data in data_set:
        if check_invalid_or_missing_data(data):
            z_score = np.abs((data - mean) / detour)
            if z_score >= cut:
                outliers.append(data)
        else:
            invalid_data += 1
    print(f'Estes são seus outliers = {outliers}')
    print(f'Esta é a quantidade de dados inválidos = {invalid_data}')


def check_invalid_or_missing_data(data): #nossa coluna espera apenas valores numéricos
    return not math.isnan(data)


#test_outliers = [180, 156, 9, 176, 163, 1827, 166, 171, 200, 220, 198, 159, 203, 209]
#get_outlier_with_z_score(test_outliers)
pre_processing()