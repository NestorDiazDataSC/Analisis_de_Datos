import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Cargar los datos
print("Cargando datos...")
df = pd.read_csv("loan_data.csv")

# Limpiar y preparar datos (igual que en tu notebook)
print("Preparando datos...")
df = df.drop(columns=['Text'])
df.columns = ["Ingreso", "Score_Credito", "Monto_Deuda", "Deuda/Ingreso", "Empleo", "Credito"]
df.Credito = df.Credito.replace(['Rejected'], 0)
df.Credito = df.Credito.replace(['Approved'], 1)
df.Empleo = df.Empleo.replace(['unemployed'], 0)
df.Empleo = df.Empleo.replace(['employed'], 1)

# Separar variables
X = df[['Score_Credito', 'Ingreso', 'Monto_Deuda', 'Deuda/Ingreso', 'Empleo']]
y = df['Credito']

# Escalar los datos
print("Escalando datos...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar el modelo
print("Entrenando modelo...")
modelo = LogisticRegression(class_weight='balanced')
modelo.fit(X_scaled, y)

# Guardar el modelo y el escalador
print("Guardando modelo...")
joblib.dump(modelo, 'modelo_credito.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("✅ ¡Modelo guardado exitosamente!")
print("📁 Archivos creados: modelo_credito.pkl y scaler.pkl")