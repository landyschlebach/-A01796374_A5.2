# Actividad 5.2: Análisis Estático - Pylint & Flake8
```
A01796374_A4.2/
 ├── results/                 <- Resultados de las ejecuciones de cada programa con los recursos de apoyo proporcionados
 │   ├── SalesResultsTC1.txt
 │   ├── SalesResultsTC2.txt
 │   ├── SalesResultsTC3.txt
 │   ├── README.md       <- Print screens of results per each test case
 ├── computeSales.py
 └── README.md
 ```
**Nota:**\
Inicialmente el programa desarrollado obtuvo un score de 9.88/10 en pylint debido al nombre del archivo.
Para obtener un score de 10.00/10, manteniendo el nombre indicado en la rúbrica se implementó la siguiente regla:
```
# pylint: disable=invalid-name
```

## Pylint: Resultado
```
PS C:\Users\landyschlebach> pylint computeSales.py
-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.90/10, +0.10)
```

## Flake8: Resultado
```
PS C:\Users\landyschlebach> flake8 --statistics computeSales.py
```
Debido a que Flake8 no mantiene un "score" como Pylint, el comando anterior no devuelve ningún resultado. Esto comprueba que el código está libre de errores y está alineado con el estándar de codificación PEP-8
