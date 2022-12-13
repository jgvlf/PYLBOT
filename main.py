# Perguntas sobre "pessoas"
# É alta | É gorda | Tem cabelos longos | Tem voz grossa?

# Definindo as pessoas conforme as características.

homem1 = [1, 0, 0, 1]
homem2 = [0, 1, 0, 1]
homem3 = [1, 1, 1, 1]
mulher1 = [1, 0, 1, 0]
mulher2 = [0, 1, 0, 0]
mulher3 = [0, 1, 1, 0]

# Adicionando as pessoas em um único array, para unificar os dados

dados = [homem1, homem2, homem3, mulher1, mulher2, mulher3]

# Definindo o genêro das pessoas

classes = [1, 1, 1, 0, 0, 0]

# pip install sklearn

#Importando o modulo "LinearSVC" da biblioteca "sklearn".

from sklearn.svm import LinearSVC

# Instanciando a Classe e colocando as entradas "input" e os rótulos "output".

model = LinearSVC()
model.fit(dados, classes)

# Criando uma pessoa com as características e informando o seu genêro com base nos dados recebidos pela IA.

pessoa = [0, 0, 0, 1]

print(model.predict([pessoa]))