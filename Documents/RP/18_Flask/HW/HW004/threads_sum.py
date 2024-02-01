import threading
    

def sum_array(array):
    return sum(array)
    

def threads_array_sum(array, threads_qty):
    threads = []
    results = []
    chunk_size = len(array) // threads_qty

    for i in range(threads_qty):
        start = i * chunk_size
        if i < (threads_qty-1):
            end = start + chunk_size
        else:
            end = len(array)
        thread = threading.Thread(target=lambda: results.append(sum_array(array[start:end])))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return sum(results)
        