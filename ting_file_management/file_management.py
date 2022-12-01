import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file, "r") as file:
            text = file.read()
            formated_text = text.split("\n")
            return formated_text
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
