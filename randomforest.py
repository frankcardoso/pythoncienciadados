# -*- coding: utf-8 -*-
"""Analise Vinhos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c9Geoxx5B1bFe_AYLfC4opBdUmPJLB3d

#Análise de dados de qualidade de vinhos

Random Forest Classifier.

É um meta estimador que ajusta vários classificadores de árvore de decisão em várias subamostras do conjunto de dados e usa a média para melhorar a precisão preditiva e o sobreajuste de controle.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

"""Base de dados (Kaggle): https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009/download"""

dados = pd.read_csv('wine_dataset.csv')

dados.head()

dados.dtypes

dados.shape

"""###Campos utilizados:

1 - fixed_acidity,

2 - volatile_acidity,

3 - citric_acid,

4 - residual_sugar,

5 - chlorides,

6 - free_sulfur_dioxide,

7 - total_sulfur_dioxide,

8 - density,

9 - pH,

10 - sulphates,

11 - alcohol
"""

variaveis = ['fixed_acidity','volatile_acidity','citric_acid','residual_sugar','chlorides','free_sulfur_dioxide','total_sulfur_dioxide','density','pH','sulphates','alcohol']

x = dados[variaveis]
y = dados['quality']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

modelo = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)

modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print('Acurácia:', accuracy_score(y_test, y_pred) * 100)