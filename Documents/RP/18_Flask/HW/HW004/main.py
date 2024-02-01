'''
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
- Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
- Массив должен быть заполнен случайными целыми числами от 1 до 100.
- При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
- В каждом решении нужно вывести время выполнения вычислений.
'''
import time
from arrayFuncs import get_array
from threads_sum import threads_array_sum
from process_sum import multiprocessing_sum
from asyncio_sum import asyncio_main

if __name__ == '__main__':
    array = get_array(1000000)
    
    start_time = time.time()
    asum = asyncio_main(array)
    print(f'Сумма: {asum}\nВремя асинхронного выполнения: {time.time() - start_time:.4f} seconds\n')


    start_time = time.time()
    processes_qty = 2
    psum = multiprocessing_sum(array, processes_qty)
    print(f'Сумма: {psum}\nВремя многопроцессорного выполнения: {time.time() - start_time:.4f} seconds\n')


    start_time = time.time()
    threads_qty = 2
    tsum = threads_array_sum(array, threads_qty)
    print(f'Сумма: {tsum}\nВремя многопоточного выполнения: {time.time() - start_time:.4f} seconds\n')