from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data
df  = pd.read_csv('homedata.csv')

# Các cột quan trọng để xây dựng mô hình
df = df[["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF", "FullBath", "BedroomAbvGr", "TotRmsAbvGrd", "SalePrice"]]

# 1. Data Preprocessing
X = df.iloc[:,0:7].values
Y = df.iloc[:,7].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=1)

# 2. Chọn model LinearRegression
model = LinearRegression()
model.fit(X_train,Y_train)
Y_predict = model.predict(X_test)

# 3. Vẽ biểu đồ so sánh giữa Y_test và Y_predict
np.random.seed(1)
X_test_ids = np.arange(0, len(X_test))
plt.figure()
plt.scatter(X_test_ids, Y_test, label='Y_test')
plt.scatter(X_test_ids, Y_predict, label='Y_predict')
plt.title('So sánh giữa Y_test và Y_predict')
plt.xlabel('Id của X_test')
plt.ylabel('SalePrice')
plt.legend()
plt.show()
