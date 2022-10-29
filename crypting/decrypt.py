from cryptography.fernet import Fernet

import ast


class Decrypt():
    def decryption_of_data(file_to_decrypt: str, key_directory: str):
        """_summary_

        Args:
            file_to_decrypt (str): Path to the file to decrypt.
            key_directory (str): Path to the key.

        Returns:
            Decrypted data in the same format of the original file. Exactly as it would have been read originally.
        """

        with open(file_to_decrypt,  "r") as data_file:
            bstr = data_file.read()
        with open(key_directory, "r") as key_data:
            key_str = key_data.read()
        key = ast.literal_eval(key_str)
        data = ast.literal_eval(bstr)
        token = Fernet(key)
        decrypted_text = token.decrypt(data)
        return decrypted_text
