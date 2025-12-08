# Servicio de Inventario - Modo Independiente

Este servicio ahora funciona de manera **completamente independiente**, sin necesidad de Eureka Server ni Config Server.

## Cambios Realizados

### 1. Dependencias Eliminadas (`pom.xml`)
- ❌ `spring-cloud-starter-config` (Config Server)
- ❌ `spring-cloud-starter-netflix-eureka-client` (Eureka Client)
- ❌ Sección `dependencyManagement` de Spring Cloud

### 2. Configuración Local (`application.properties`)
La configuración ahora está completamente en `src/main/resources/application.properties`:

```properties
# Configuración de la aplicación
spring.application.name=inventario
server.port=8083

# Base de datos PostgreSQL
spring.datasource.url=jdbc:postgresql://localhost:5432/inventariodb
spring.datasource.username=postgres
spring.datasource.password=postgres

# JPA/Hibernate
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

# OpenAPI/Swagger
springdoc.api-docs.path=/api-docs
springdoc.swagger-ui.path=/swagger-ui.html
```

## Requisitos Previos

1. **PostgreSQL**: Debe estar instalado y ejecutándose
2. **Base de datos**: Crear la base de datos `inventariodb`
   ```sql
   CREATE DATABASE inventariodb;
   ```

## Ejecutar el Servicio

### Opción 1: Con Maven
```bash
.\mvnw.cmd spring-boot:run
```

### Opción 2: Con Java
```bash
.\mvnw.cmd clean package
java -jar target\inventario-0.0.1-SNAPSHOT.jar
```

## Acceso a los Endpoints

- **API REST**: http://localhost:8081/api/inventario
- **Swagger UI**: http://localhost:8081/swagger-ui.html
- **OpenAPI Docs**: http://localhost:8081/api-docs
