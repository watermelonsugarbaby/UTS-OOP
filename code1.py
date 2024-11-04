class DisneyPrincess:
    def __init__(self, name, movie, power):
        self.__name = name  # variabel private
        self.__movie = movie  # variabel private
        self.__power = power  # variabel private

    def __private_info(self):
        return f"Nama: {self.__name}, Film: {self.__movie}, Kekuatan: {self.__power}"  # metode private

    # Getter untuk nama
    def get_name(self):
        return self.__name

    # Setter untuk nama
    def set_name(self, new_name):
        self.__name = new_name

    # Metode publik untuk mengakses info private
    def access_private_info(self):
        return self.__private_info()

    def introduce(self):
        print(f"Saya adalah {self.__name}, dari film {self.__movie}.")
        print("Kekuatan saya adalah:", self.__power)

class Ariel(DisneyPrincess):
    def __init__(self):
        super().__init__("Ariel", "The Little Mermaid", "Berenang dengan cepat")

    def demo(self):
        self.introduce()
        private_info = self.access_private_info()
        print("Informasi lengkap:", private_info)

class Belle(DisneyPrincess):
    def __init__(self):
        super().__init__("Belle", "Beauty and the Beast", "Cinta dan keberanian")

    def demo(self):
        self.introduce()
        private_info = self.access_private_info()
        print("Informasi lengkap:", private_info)

# Membuat objek dari kelas Ariel dan Belle
ariel = Ariel()
ariel.demo()

print()  # Tambahkan jarak antara output

belle = Belle()
belle.demo()
