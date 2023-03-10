import pandas as pd

df = pd.read_json("dados.json")

df1 = df.loc[df['valor'] != 0]

media = df1["valor"].mean()

minimo = df1["valor"].min()

maximo = df1["valor"].max()

arr = df1["valor"] > media
maiores_que_media = arr.values.sum()

print(f"o menor valor de faturamento foi: {minimo}")
print(f"o maior valor de faturamento foi: {maximo}")
print(f"""o numero de dias do mes em que o valor do faturamento foi maior que a media mensal foi: {maiores_que_media}""")