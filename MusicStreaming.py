from abc import ABC, abstractmethod

class Audio(ABC):
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self._duracion = duracion  # duracion en segundos
    
    @abstractmethod
    def getDetalles(self):
        pass
    
# Cancion
class Cancion(Audio):
    def __init__(self, titulo, artista, duracion):
        super().__init__(titulo, artista, duracion)
    
    def getDetalles(self):
        minutos, segundos = divmod(self._duracion, 60)
        return f"Canción: {self.titulo} - Artista: {self.artista} - Duración: {minutos}:{segundos:02d}"

# Podcast
class Podcast(Audio):
    def __init__(self, titulo, artista, duracion, episodio):
        super().__init__(titulo, artista, duracion)
        self.episodio = episodio
    
    def getDetalles(self):
        minutos, segundos = divmod(self._duracion, 60)
        return f"Podcast: {self.titulo} - Episodio: {self.episodio} - Artista: {self.artista} - Duración: {minutos}:{segundos:02d}"


# REPRODUCTOR
class Reproductor:
    def __init__(self):
        self.estado = "pausado"  # estados: "reproduciendo", "pausado"
    
    def play(self):
        if self.estado == "reproduciendo":
            raise Exception("El audio ya está en reproducción")
        self.estado = "reproduciendo"
        print(f"\nReproduciendo...\n",audio.getDetalles())
        
    def pause(self):
        if self.estado != "reproduciendo":
            raise Exception("El audio no está en reproducción")
        self.estado = "pausado"
        print("\nPausado")
    

# Main de prueba
if __name__ == "__main__":
    cancion = Cancion("Amazing", "Aereosmith", 356)
    podcast = Podcast("The Podcast", "Podcast Prueba", 1500, "Episode 1")
    
    reproductor = Reproductor()
    
    # Reproducir canción
    audio = cancion
    reproductor.play()
    reproductor.pause()
    
    # Reproducir podcast
    audio = podcast
    reproductor.play()
    reproductor.pause()