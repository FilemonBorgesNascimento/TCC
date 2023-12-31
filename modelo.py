# -*- coding: utf-8 -*-
"""CanceMama.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TO33oKv9KInuF05S1eNyKYNiXAZUAkvB
"""

from sklearn import tree
from sklearn.datasets import load_breast_cancer
import pickle
import pandas as pd

#dados = load_breast_cancer()
dados = pd.read_csv("data.csv")
print(dados)

y= dados['diagnosis']
#print(y)
x=dados[['radius_mean','texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean','concavity_mean','concave points_mean','symmetry_worst','fractal_dimension_worst']]
print(x)

#realizando o split da base para teste
from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x_treino, y_treino)
preditos = clf.predict(x_teste)
print("Preditos:",preditos[:20])
print("Real    :",y_teste[:20].values)

from sklearn.metrics import accuracy_score
print("Acuracia:", accuracy_score(y_teste,preditos))

pickle.dump(clf, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
#print (model.predict([ [5,2,5,2.5] ]))