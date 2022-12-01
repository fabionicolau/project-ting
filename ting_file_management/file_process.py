from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    data = txt_importer(path_file)

    for processed_datas in instance.queue:
        if processed_datas["nome_do_arquivo"] == path_file:
            return None

    processed_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(data),
        "linhas_do_arquivo": data,
    }

    instance.enqueue(processed_data)
    sys.stdout.write(str(processed_data))


def remove(instance):
    if not instance.queue:
        return sys.stdout.write("Não há elementos\n")

    path_file = instance.peek()["nome_do_arquivo"]

    instance.dequeue()
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        metadata = instance.search(position)
        sys.stdout.write(str(metadata))
    except IndexError:
        sys.stderr.write("Posição inválida\n")
