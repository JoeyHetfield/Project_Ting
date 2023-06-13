import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None

    if not path_file.exists(path_file):
        print(f"Arquivo {path_file} não encontrado")
        return None
