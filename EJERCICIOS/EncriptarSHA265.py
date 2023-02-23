import hashlib
import tkinter as tk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb


class SHA256Encrypter:
    
    @staticmethod
    def sha256(input_str):
        hash_obj = hashlib.sha256(input_str.encode('utf-8'))
        return hash_obj.hexdigest()
    
    def run(self):
        root = tk.Tk()
        root.withdraw()
        input_str = tk.simpledialog.askstring("Encriptar con SHA-256", "Ingresa una cadena para encriptar")
        if input_str is not None:
            encrypted_str = SHA256Encrypter.sha256(input_str)
            mb.showinfo("Encriptar con SHA-256", "La cadena encriptada es: " + encrypted_str)

if __name__ == "__main__":
    encrypter = SHA256Encrypter()
    encrypter.run()
