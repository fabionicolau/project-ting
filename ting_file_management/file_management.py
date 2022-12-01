import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            text = file.readlines()
            formated_text = [line.strip() for line in text]
            return formated_text
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")


print(txt_importer("statics/arquivo_teste.txt"))
