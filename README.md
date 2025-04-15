# Hackathon 0: Dominando Git y GitHub 🚀

## Consideraciones Generales 📋

Bienvenidos a la primera hackathon del semestre **2025-1** del curso CS2031, Desarrollo Basado en Plataformas. En esta edición, nos centraremos exclusivamente en Git y GitHub, herramientas fundamentales para cualquier desarrollador. En lugar de enfocarnos en la escritura de código, nos dedicaremos a perfeccionar nuestras habilidades en el manejo de repositorios, la colaboración en equipos y la integración continua.

Para esta hackathon, cada equipo estará compuesto por cuatro (4) miembros. Será crucial que trabajen en conjunto para cumplir con todos los checkpoints establecidos. Es importante que mantengan una comunicación constante y que asignen tareas de manera equitativa. Al ser una actividad grupal, la organización y la cooperación serán clave para el éxito.

## Instrucciones Generales 📝

1. **Formación de Equipos**: Los equipos deben estar conformados por 4 alumnos de la misma sección de laboratorio. Cada equipo debe asegurarse de que todos sus miembros participen activamente en cada checkpoint.

2. **Gestión de Repositorios**: Solo se permitirá un repositorio por equipo, el cual deberá cumplir con los requisitos especificados en cada checkpoint. La calidad del trabajo en cada checkpoint será evaluada con base en el cumplimiento de los requisitos, la correcta utilización de Git y GitHub, y la capacidad de resolver conflictos y problemas de manera efectiva.

3. **Entrega y Evaluación**: Al finalizar la hackathon, se revisará el repositorio de cada equipo. Asegúrense de cumplir con todos los requisitos antes de la hora límite. Se evaluará tanto el trabajo grupal como la participación individual a través del historial de commits y los pull requests realizados.

## Checkpoints 📌

### **Checkpoint 1: Configuración Inicial** ⚙️

- **Objetivo**: Configurar adecuadamente el entorno de trabajo local y la cuenta en GitHub.
  - **Tareas**:
    1. Cada miembro del equipo debe configurar Git en su máquina local: configurar usuario, email y nombre.
    2. Crear o asegurarse de tener una cuenta en GitHub.
    3. Generar claves SSH en sus máquinas locales y agregarlas a sus cuentas de GitHub.
  - **Evaluación**: Mostrar la configuración de Git local y la adición exitosa de la clave SSH en su cuenta de GitHub.

### **Checkpoint 2: Creación y Configuración del Repositorio** 📦

- **Objetivo**: Crear y configurar un repositorio en GitHub que refleje buenas prácticas de desarrollo colaborativo.
  - **Tareas**:
    1. Crear un repositorio público o privado en GitHub. Este repositorio será compartido por todos los miembros del equipo.
    2. Crear un archivo `README.md` en el directorio `docs/` (vacío por ahora).
    3. Configurar las reglas de la rama principal (`main` o `master`) para que no se pueda hacer `push` directo a esta rama. Los cambios en la rama principal solo deben realizarse mediante pull requests aprobados.
    4. Crear un archivo `.gitignore` en el repositorio y añadir los directorios y archivos que no deben ser versionados, por ejemplo, `__pycache__/`, `*.pyc`, `.env`, `venv/`, `.venv/`, etc.
  - **Evaluación**: Proveer un enlace al repositorio y capturas de pantalla de la configuración de las reglas de la rama principal.

### **Checkpoint 3: Gestión de Issues y Pull Requests** 🔄

- **Objetivo**: Implementar un flujo de trabajo que simule un entorno colaborativo real.
  - **Tareas**:
    1. Crear un issue en GitHub para cada miembro del equipo. El título del issue debe reflejar la tarea que realizará cada miembro, por ejemplo, "Añadir nombre al README.md".
    2. Cada miembro del equipo debe crear una rama nueva a partir del issue asignado (la rama debe llevar el nombre del issue).
    3. Cada miembro deberá modificar el archivo `docs/README.md` añadiendo su nombre y un breve párrafo de presentación.
    4. Realizar un pull request de cada rama hacia la rama principal (`main` o `master`) y completar el proceso de revisión y aprobación.
    5. Resolver cualquier conflicto que pueda surgir durante el proceso de merge.
  - **Evaluación**: Mostrar los issues creados, las ramas correspondientes, y el historial de pull requests. Se verificará que haya un pull request por cada miembro del equipo.

### **Checkpoint 4: Resolución de Conflictos en Pull Requests** 🔧

- **Objetivo**: Trabajar con issues, pull requests, y resolver conflictos en el merge mientras se desarrolla un mini proyecto en Python.

  - **Descripción del Proyecto**:
    - El equipo desarrollará una **calculadora en línea de comandos** que permita realizar operaciones básicas (suma, resta, multiplicación y división).
    - La calculadora debe permitir a los usuarios **escribir operaciones completas** (por ejemplo, `2 + 2`), y al presionar **Enter**, la operación se debe calcular y mostrar el resultado.
    - Si el usuario presiona la tecla **'c'**, la operación escrita debe ser borrada.

  - **Tareas (Issues)**:
    1. **Issue 1:** Implementar la función de **suma** en la calculadora.
    2. **Issue 2:** Implementar la función de **resta** en la calculadora.
    3. **Issue 3:** Implementar la función de **multiplicación** en la calculadora.
    4. **Issue 4:** Implementar la función de **división** en la calculadora.

  - **Requisitos**:
    - Cada tarea debe ser creada como un **issue** en GitHub con una descripción detallada, nombres de los responsables y un estimado de tiempo.
    - Cada tarea debe ser resuelta en una **rama separada** y enviada como un pull request.
    - Se debe provocar **conflictos de merge** en al menos un pull request, los cuales deberán ser resueltos por el equipo.

  - **Evaluación**:
    - Se revisarán los issues creados, las ramas correspondientes, los pull requests, y la resolución efectiva de los conflictos.
    - La calculadora debe cumplir con los requisitos de funcionalidad especificados.

### **Checkpoint 5: Testing Automatizado con GitHub Actions** ✅

- **Objetivo**: Implementar pruebas automatizadas utilizando GitHub Actions.
  - **Tareas**:
    1. Se proporcionará un archivo `.py` que contiene pruebas automatizadas para el mini proyecto de Python.
    2. Configurar un **GitHub Action** que ejecute estas pruebas automáticamente cada vez que se realice un push o un pull request al repositorio.
    3. El workflow debe ser configurado para ejecutar las pruebas en al menos dos versiones diferentes de Python (por ejemplo, 3.11 y 3.12). Para ejecutar las pruebas de Python, usa el siguiente comando:

          ```sh
          python -m unittest tests.test
          ```

    4. Documentar el proceso de configuración y cualquier problema encontrado durante la implementación.
  - **Evaluación**: Verificación del workflow configurado y que todas las pruebas pasen correctamente antes de completar el merge.

## Consideraciones Finales

- **Documentación**: Asegúrense de documentar cada paso realizado en el repositorio, utilizando los mensajes de commit y el archivo `docs/README.md`.
- **Fecha Límite**: La hackathon deberá completarse antes del 15 de abril a las 18 horas, momento en el cual los repositorios serán revisados.

¡Buena suerte a todos! ⚡ Que esta hackathon sea una oportunidad para fortalecer su dominio de Git y GitHub.
