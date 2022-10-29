from cryptography.fernet import Fernet

import ast

class Encrypt():
    def encryption_of_data(file_to_encrypt:str):
        """_summary_
        This will create the encrypted file WARNING THE ORIGINAL FILE WILL STILL BE THERE
        Make sure the key is kept SECRET

        Args:
            file_to_encrypt (str): Path to file to encrypt.
        """
        with open(file_to_encrypt,  "rb") as data_file:
            
            data_file = data_file.read()
        key_id = Fernet.generate_key()
        print(type(key_id))
        key = Fernet(key_id)
        token = key.encrypt(data_file)
        print(token)
        with open("data.txt", "w") as j:
            j.write(str(token))
            
        with open("key_do_not_upload_this_file.txt", "w") as j:
            j.write(str(key_id))





    
