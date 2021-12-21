from cryptography.fernet import Fernet
import pyttsx3
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)

print(Fore.BLACK + Back.BLUE + " ENCRYPT AND DECRYPT ")
print("Copyright (c) 2022 Ashfaaq Rifath")

engine = pyttsx3.init()
engine.say("Encrypt or Decrypt file")
engine.runAndWait()
option = input("Encrypt or Decrypt file (e/d): ")

if option.lower() == "e":
    key = Fernet.generate_key()
    with open('encryptkey.key', 'wb') as encryptkey:
        encryptkey.write(key)

    fernet = Fernet(key)

    engine = pyttsx3.init()
    engine.say("Current path or absolute path")
    engine.runAndWait()
    file_path = input("Current path or absolute path (c/a): ")

    if file_path.lower() == "c":
        engine = pyttsx3.init()
        engine.say("Enter file name")
        engine.runAndWait()
        user_file_encp = input("Enter file name: ")

        try:
            with open(user_file_encp, 'rb') as file:
                original_file = file.read()
        except FileNotFoundError:
            speak8 = " FILE NOT FOUND "
            print(Fore.BLACK + Back.RED + speak8)
            engine = pyttsx3.init()
            engine.say(speak8)
            engine.runAndWait()

        encrypt = fernet.encrypt(original_file)

        with open(user_file_encp, 'wb') as encp_file:
            encp_file.write(encrypt)
            speak1 = " Your file is encrypted "
            speak2 = " Move file, key from this directory after encryption "
            print(Fore.BLACK + Back.GREEN + speak1)
            print(Fore.BLACK + Back.GREEN + speak2)

            engine = pyttsx3.init()
            engine.say(speak1)
            engine.runAndWait()

            engine = pyttsx3.init()
            engine.say(speak2)
            engine.runAndWait()

    elif file_path.lower() == "a":
        engine = pyttsx3.init()
        engine.say("Enter file path")
        engine.runAndWait()
        abs_path = input("Enter file path: ")

        try:
            with open(abs_path, 'rb') as file:
                original_file = file.read()
        except FileNotFoundError:
            speak9 = " FILE NOT FOUND "
            print(Fore.BLACK + Back.RED + speak9)
            engine = pyttsx3.init()
            engine.say(speak9)
            engine.runAndWait()

        encrypt = fernet.encrypt(original_file)

        with open(abs_path, 'wb') as encp_file:
            encp_file.write(encrypt)
            encp_file.write(encrypt)
            speak3 = " Your file is encrypted "
            speak4 = " Move key from this directory after encryption "
            print(Fore.BLACK + Back.GREEN + " Your file is encrypted ")
            print(Fore.BLACK + Back.GREEN + " Move key from this directory after encryption ")

            engine = pyttsx3.init()
            engine.say(speak3)
            engine.runAndWait()

            engine = pyttsx3.init()
            engine.say(speak4)
            engine.runAndWait()
    else:
        speak5 = " INVALID OPTION "
        print(Fore.BLACK + Back.RED + speak5)
        engine = pyttsx3.init()
        engine.say(speak5)
        engine.runAndWait()

elif option.lower() == "d":
    speak6 = " FILE AND KEY MUST BE UPLOADED IN THIS DIRECTORY BEFORE DECRYPTION "
    print(Fore.BLACK + Back.YELLOW + speak6)
    engine = pyttsx3.init()
    engine.say(speak6)
    engine.runAndWait()

    engine = pyttsx3.init()
    engine.say("Enter file name")
    engine.runAndWait()
    user_file_decp = input("Enter file name: ")

    with open('encryptkey.key', 'rb') as encp_key:
        read_enc_key = encp_key.read()

    fernet = Fernet(read_enc_key)

    try:
        with open(user_file_decp, 'rb') as read_encp_file:
            encrypted_file  = read_encp_file.read()
    except FileNotFoundError:
        speak7 = " FILE AND KEY NOT FOUND "
        print(Fore.BLACK + Back.RED + speak7)
        engine = pyttsx3.init()
        engine.say(speak7)
        engine.runAndWait()

    decrypt = fernet.decrypt(encrypted_file)

    with open(user_file_decp, 'wb') as decp_file:
        decp_file.write(decrypt)
        print(Fore.BLACK + Back.GREEN + " Your file is decrypted ")
        print(Fore.BLACK + Back.GREEN + " Move file, key from this directory after decryption ")
        speak10 = " Your file is decrypted "
        speak11 = " Move file, key from this directory after decryption "
        print(Fore.BLACK + Back.GREEN + speak10)
        print(Fore.BLACK + Back.GREEN + speak11)

        engine = pyttsx3.init()
        engine.say(speak10)
        engine.runAndWait()
        
        engine = pyttsx3.init()
        engine.say(speak11)
        engine.runAndWait()

else:
    speak12 = " INVALID OPTION "
    print(Fore.BLACK + Back.RED + speak12)
    engine = pyttsx3.init()
    engine.say(speak12)
    engine.runAndWait()