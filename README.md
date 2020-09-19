# Automatización inicial proyectos Python
### Introducción

Comencé este proyecto para profundizar conocimientos de Python y bash gracias a una publicación de @KalleHallden en su [proyecto Github!](https://github.com/KalleHallden/ProjectInitializationAutomation.git)

> Material de soporte
> - [x] Script in bash: muestra distintas formas de carga de [script en bash](https://www.youtube.com/watch?v=F-gskSl4pwQ). Adicionalmente a la instalación (pip install selenium) hay que utilizar chromedriver() para ejecutar funciones avanzadas.
> - [x] Selenium driver: para manejo avanzado de [scrapping](https://selenium-python.readthedocs.io/getting-started).

### TODO List
```bash
 1. [x] Clonar proyecto git clone "xxxxx"
 2. [x] Acceder al directorio: cd nombreDirectorio
 3. [x] Instalar dependencias: pip install -r requirements.txt
 4. [x] Crear archivo de entorno: touch .env
 5. [x] completar el archivo .env como se muestra mas abajo
```

chromeDriver() path
# Para utilizar en macbook 15
driver_path = "/Users/carlospereiro/Documents/SOFTWARE-DEVELOPMENT/DRIVERS/CHROME/chromedriver"
# Para utilizar en iMac
driver_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/DRIVERS/CHROME/chromedriver"


software installing path
# Para utilizar en iMac
project_path = "/Users/carlos/Documents/SOFTWARE-DEVELOPMENT/PYTHON/initDevDeployment/"
# Para utilizar en macbook 15
project_path = "/Users/carlospereiro/Documents/SOFTWARE-DEVELOPMENT/CARLOS/PYTHON/initDevDeployment/"
-------------------------

Todos los shell scripts comienzan con #!/bin/bash y determina que el interprete para este script es 'bash' y dependiendo como configuremos esta linea puede ser otro interprete.

Para hacer "ejecutable el shell script primero hay que avisarle al Sist Operativo: chmod +x ./nombre.sh

Para ejecutar los shell scripts: ./nombre.sh

