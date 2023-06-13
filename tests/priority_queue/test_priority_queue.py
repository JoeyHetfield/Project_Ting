from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    teste_fila = PriorityQueue()
    teste_fila.enqueue("arquivo1.txt", 1)
    teste_fila.enqueue("arquivo2.txt", 6)
    teste_fila.enqueue("arquivo3.txt", 3)
    assert teste_fila._data[0]["nome_do_arquivo"] == "arquivo3.txt"
    assert teste_fila._data[1]["nome_do_arquivo"] == "arquivo2.txt"
    assert teste_fila._data[2]["nome_do_arquivo"] == "arquivo1.txt"
