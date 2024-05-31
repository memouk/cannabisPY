import requests
import pandas as pd
import matplotlib.pyplot as plt


url = "http://localhost:8080/api/plantas"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data["items"])
    #print(df)
    #print(data)
    print(df.iloc[0:10])
    print(df.info())
           
    print(df['etapa_id'].value_counts())

    plt.bar([1,2,3,4,5],df['etapa_id'].value_counts())
    plt.xlabel('Cantidad de plantas por etapa')
    plt.ylabel('Etapa')
    plt.show()
else:
    print("Error:", response.status_code)