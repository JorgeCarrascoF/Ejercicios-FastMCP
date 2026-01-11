# Guía de Instalación

Esta guía proporciona instrucciones para instalar y ejecutar los recursos disponibles en este proyecto. Asegúrate de seguir los pasos específicos para cada ejemplo.

---

La conexión a los servidores MCP se pueden realizar de dos formas:
- Con VSCode y la extensión de GitHub.
- Utilizando Docker y ejecutando el docker-compose.yml que se encuentra en la raíz del proyecto.

## Requisitos Previos

1. **Docker y Docker Compose**:
   - Asegúrate de tener Docker y Docker Compose instalados en tu sistema.
   - Puedes descargar Docker desde [https://www.docker.com/](https://www.docker.com/).

2. **Python**:
   - Instala Python 3.8 o superior desde [https://www.python.org/](https://www.python.org/).
   - Asegúrate de tener `pip` instalado.

3. **Java**:
   - Instala Java JDK 11 o superior desde [https://www.oracle.com/java/technologies/javase-downloads.html](https://www.oracle.com/java/technologies/javase-downloads.html).
   - Configura la variable de entorno `JAVA_HOME`.

---

## Ejemplo 1: Servidor y Cliente MCP

### Instalación

1. Navega a la carpeta `Ejemplo1 -- Servidor y cliente MCP/servidorMCP`.
2. Instala las dependencias de Python ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. Construye la imagen Docker:
   ```bash
   docker build -t servidor-mcp .
   ```
2. Ejecuta el contenedor:
   ```bash
   docker run -p 5000:5000 servidor-mcp
   ```
3. Para el cliente, ejecuta el archivo `client.py`:
   ```bash
   python client.py
   ```

---

## Ejemplo 2: OpenAPI

### Instalación

1. Navega a la carpeta `Ejemplo2 -- OpenAPI/inventario`.
2. Asegúrate de tener Maven instalado. Si no lo tienes, descárgalo desde [https://maven.apache.org/](https://maven.apache.org/).

### Ejecución

1. Construye el proyecto con Maven:
   ```bash
   ./mvnw clean install
   ```
2. Construye la imagen Docker:
   ```bash
   docker build -t inventario .
   ```
3. Ejecuta el contenedor:
   ```bash
   docker run -p 8080:8080 inventario
   ```

---

## Ejemplo 3: Gemini

### Instalación

1. Navega a la carpeta `Ejemplo3 -- Gemini`.
2. Instala las dependencias de Python ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. Ejecuta los scripts de ejemplo:
   ```bash
   python fast_mcp_ex_1.py
   python fast_mcp_ex_2.py
   python fast_mcp_ex_3.py
   python fast_mcp_ex_4.py
   ```
2. Opcionalmente, abre el archivo `code_analizer.ipynb` en Jupyter Notebook para analizar el código.

---

## Limpieza

1. Para detener y eliminar contenedores Docker:
   ```bash
   docker ps -a
   docker stop <container_id>
   docker rm <container_id>
   ```
2. Para eliminar imágenes Docker:
   ```bash
   docker images
   docker rmi <image_id>
   ```

---

Sigue estas instrucciones para instalar y ejecutar los recursos de este proyecto. Si encuentras algún problema, consulta los archivos `README.md` en cada carpeta para obtener más detalles.
