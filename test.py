import joblib

# 加载pickle文件
loaded_data = joblib.load('src/saved_model/trained_model_1683882309.pkl')

# 打印pickle文件的内容
print(loaded_data)