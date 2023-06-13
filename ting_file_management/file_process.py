from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            return None

    imported_file = txt_importer(path_file)

    created_obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(imported_file),
        "linhas_do_arquivo": imported_file,
    }

    instance.enqueue(created_obj)

    print(created_obj)


def remove(instance):
    if len(instance._data) <= 0:
        print("Não há elementos")
        return None

    removed = instance.dequeue()
    removed_file = removed["nome_do_arquivo"]

    print(f"Arquivo {removed_file} removido com sucesso")


def file_metadata(instance, position):
    if position >= len(instance._data):
        print("Posição inválida", file=sys.stderr)
        return None
