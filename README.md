# Sistema de Votación Simple

Proyecto grupal (3 integrantes) para practicar ramas y versionado con Git.

## Estructura de ramas

| Rama              | Integrante | Función a implementar                         | Tag ejemplo         |
|-------------------|------------|------------------------------------------------|---------------------|
| `rama-registro`   | 1          | `registrar_voto()` + validación de doble voto  | `v0.1-registro`      |
| `rama-resultados` | 2          | `ver_resultados()` + porcentajes               | `v0.1-resultados`    |
| `rama-reinicio`   | 3          | `reiniciar_votacion()` + historial en archivo  | `v0.1-reinicio`      |

## Flujo de trabajo (cada integrante, en su propia rama)

```bash
git checkout main
git pull origin main
git checkout -b rama-<tu-parte>

# ... editas sistema_votacion.py, implementas tu función ...

git add sistema_votacion.py
git commit -m "feat: implementar <tu funcion>"

# ... más cambios / pruebas ...
git add .
git commit -m "test: validar <tu funcion>"

# al terminar, marca tu rama con tu tag personal
git tag v0.1-<tu-parte>

# sube tu rama y el tag
git push origin rama-<tu-parte>
git push origin v0.1-<tu-parte>
```

## Entrega

Captura de pantalla de:

```bash
git log --oneline --decorate
```

mostrando tus commits y tu tag personal.
