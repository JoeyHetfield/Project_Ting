import sys
import os


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None

    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None

    with open(path_file) as file:
        lines = file.readlines()

        lines = [line.rstrip() for line in lines]

    return lines
