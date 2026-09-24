[33mcommit 87d85f0d0a26079ed950132babc5af5be9f5f454[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mrama-registro[m[33m)[m
Author: Equipo Votacion <equipo@sena.edu.co>
Date:   Sat Sep 19 12:08:06 2026 -0500

    feat: implementar registrar_voto con validacion de doble voto

[1mdiff --git a/sistema_votacion.py b/sistema_votacion.py[m
[1mindex e06ea94..61fa93c 100644[m
[1m--- a/sistema_votacion.py[m
[1m+++ b/sistema_votacion.py[m
[36m@@ -1,13 +1,3 @@[m
[31m-"""[m
[31m-Sistema de Votación Simple[m
[31m-Actividad: ramas y versionado con Git (SENA - ADSO)[m
[31m-[m
[31m-Cada función se implementa en una rama distinta:[m
[31m-  - rama-registro   -> registrar_voto()[m
[31m-  - rama-resultados -> ver_resultados()[m
[31m-  - rama-reinicio   -> reiniciar_votacion()[m
[31m-"""[m
[31m-[m
 # Candidatos disponibles para votar[m
 CANDIDATOS = ["Candidato A", "Candidato B", "Candidato C"][m
 [m
