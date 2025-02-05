**Plataforma de E-Learning**

__Descripción del Proyecto__

Esta plataforma permite a los usuarios registrarse, crear y matricularse en cursos, 
realizar seguimientos de su progreso e interactuar con instructores y compañeros. 
Ofrece una interfaz intuitiva y funcionalidades backend para gestionar contenido de cursos, 
usuarios y evaluaciones.

__Mejoras Practicas en Core MVC__

**Principio SOLID: Responsabilidad Única (SRP)**
Separación de responsabilidades en el manejo de usuarios y autenticación.

**Principio SOLID: Sustitución de Liskov (LSP)**
Diseño flexible para manejar diferentes tipos de contenido (video, texto, cuestionarios) sin romper la funcionalidad existente.

**Patrón de Diseño: Strategy**
Clases para manejar diferentes estrategias de contenido dentro del sistema.

**Patrón de Diseño: Decorator**
Decoradores para restringir acceso según roles.

__Características__
**Autenticación de Usuario:** Registro, inicio de sesión y gestión de contraseñas.

**Creación y Gestión de Cursos:** Los administradores pueden crear, editar y eliminar cursos.

**Matriculación en Cursos**: Los usuarios pueden matricularse y hacer seguimiento de su progreso.

**Cuestionarios y Evaluaciones:** Los creadores de cursos pueden agregar cuestionarios.

**Panel de Usuario:** Muestra cursos matriculados, progreso y logros.

__Stack Tecnológico__
Frontend: HTML, CSS

Backend: Flask 

Base de Datos: SQLite / PostgreSQL / SQLAlchemy

__Se utilizo en el SASS__
Flexbox: Se utiliza con display: flex; 

Permite crear diseños flexibles. Las propiedades clave son flex-direction, justify-content, align-items, entre otras.

CSS Grid: Se utiliza con display: grid; 

Define un sistema de filas y columnas. Las propiedades clave son grid-template-columns, grid-template-rows, grid-gap, etc.
