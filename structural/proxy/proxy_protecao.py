from abc import ABC, abstractmethod

class Video(ABC):
    @abstractmethod
    def play(self):
        pass

class RealVideo(Video):
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        print(f"Tocando vídeo: {self.filename}")

class VideoProxy(Video):
    def __init__(self, filename, user_role):
        self.filename = filename
        self.user_role = user_role
        self.real_video = RealVideo(filename)

    def play(self):
        if self.user_role == "premium":
            self.real_video.play()
        else:
            print("Acesso negado! Apenas usuários premium podem assistir a este vídeo.")

if __name__ == "__main__":
    usuario_comum = VideoProxy("video_aula.mp4", "comum")
    usuario_premium = VideoProxy("video_aula.mp4", "premium")

    print("Usuário comum tenta acessar:")
    usuario_comum.play()

    print("\nUsuário premium tenta acessar:")
    usuario_premium.play()
