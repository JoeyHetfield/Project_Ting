from file_management import txt_importer


def process(path_file, instance):
    if instance.search(path_file):
        return None

    imported_file = txt_importer(path_file)

    created_obj = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(imported_file),
        "linhas_do_arquivo": imported_file,
    }


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
