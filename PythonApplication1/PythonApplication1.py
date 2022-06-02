
import time # Библиотека для замера времени (очевидно)

def sort(arr): #Сортировка листа (текста) по возрастанию "расчёской"
    totaltime = 0
    for j in range (1000): #1000 повторений для точного определения времени. 1000 работает довольно долго, уменьшите по необходимости
        start_time = time.time()
        end = len(arr)
        swaps = True
        while end > 1 or swaps:
            end = max(1, int(end / 1.247))
            swaps = False
            for i in range(len(arr) - end):
                j = i + end
                if arr[i].lower() > arr[j].lower(): # Использую lower чтобы не учитывать регистр, когда сортирую по возрастанию
                    arr[i], arr[j] = arr[j], arr[i] # А вот меняю местами не lower, чтобы сохранить регистр при выводе
                    swaps = True
        ttime = time.time() - start_time
        totaltime += ttime #Время за 1000 раз
    return[(totaltime/1000)] #Поэтому и делю на 1000


with open('F:/Practics/Input/Original1.txt','r+') as f: # Бояре не закрывают файлы, они используют with
    arrraw = [row.strip() for row in f.read().split()] # Сырой лист(массив)
    arr = [row.strip('.,!?—:;()«»-IV1234567890') for row in arrraw] # без знаков препинания и тп.
    while ('' in arr): # Удаление пустых ячеек. Из-за удаления знаков препинания некоторые ячейки стали пустыми. Чтобы верно определить количество слов и работать с листом(массивом) нужно их удалить
            arr.remove('')
ttime = sort(arr)