import multiprocessing

result = multiprocessing.Value('i', 0)


def sum_array(array, res):
    with res.get_lock():
        res.value += sum(array)
 

def multiprocessing_sum(array, processes_qty):
    processes = []
    chunk_size = len(array) // processes_qty
    for i in range(0, len(array), chunk_size):
        tmp = array[i:i+chunk_size]
        process = multiprocessing.Process(target=sum_array, args=[tmp, result])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    return result.value
