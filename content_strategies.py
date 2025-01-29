from abc import ABC, abstractmethod

# Clase abstracta base para estrategias de contenido
class ContentStrategy(ABC):
    @abstractmethod
    def render_content(self):
        pass


# Estrategia para contenido de texto
class TextContentStrategy(ContentStrategy):
    def render_content(self):
        return "Renderizando contenido de texto: aquí va el contenido textual del curso."


# Estrategia para contenido de video
class VideoContentStrategy(ContentStrategy):
    def render_content(self):
        return "Renderizando contenido de video: reproducción del video."


# Estrategia para contenido de archivos (PDF, Word, etc.)
class FileContentStrategy(ContentStrategy):
    def render_content(self):
        return "Renderizando contenido de archivo: descarga habilitada."


# Estrategia para contenido de cuestionarios
class QuizContentStrategy(ContentStrategy):
    def render_content(self):
        return "Renderizando cuestionario: pregunta y opciones de respuesta."
