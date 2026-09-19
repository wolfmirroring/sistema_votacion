from sistema_votacion import votos, ver_resultados

# Simulamos votos directamente sobre el diccionario para probar el cálculo
votos["Candidato A"] = 3
votos["Candidato B"] = 1
votos["Candidato C"] = 0

ver_resultados()
# Esperado: Candidato A 75.0%, Candidato B 25.0%, Candidato C 0.0%, total 4
