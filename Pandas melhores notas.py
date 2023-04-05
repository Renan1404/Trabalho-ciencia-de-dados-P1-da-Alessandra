import pandas as pd

df = pd.DataFrame({
    'Aluno': ['Luana', 'Bruno', 'Carlos', 'Daniel', 'Evelyn'],
    'idade': [25, 28, 18, 25, 33],
    'Nota': [8.5, 7.2, 5.6, 6.5, 9.0]
})

print(df)

melhores_notas = df.nlargest(3, 'Nota')
maiores_idades = df.nlargest(3, 'idade')

filtrado = pd.merge(melhores_notas, maiores_idades, on=['Aluno', 'idade', 'Nota'])

print(filtrado)