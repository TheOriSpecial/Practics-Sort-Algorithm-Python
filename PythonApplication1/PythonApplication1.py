
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
def output(arr, arrraw): #Вывод в консоль и в 2 файла (выходной текст и его анализ)
    print('Исходный текст: ','\n')
    for x in arrraw:
        print(x,' ', end="")
    print('\n')
    print('Вариант 8: кириллица, по алфавиту, по возрастанию, игнорировать числа, сортировка расчёской')
    print('Количество слов: ',len(arr))
    print('Время выполнения: ',ttime[0], 'секунд')

    with open('F:/Practics/Analysis/Analysis1.txt','w')as fa: # Бояре не закрывают файлы, они используют with
        fa.writelines('Введённый текст:'+'\n')
        for word in arrraw: #Вывод текста циклом
            fa.write(word + ' ')
        fa.writelines('\n' + '\n') 
        fa.writelines('Вариант 8: кириллица, по алфавиту, по возрастанию, игнорировать числа, сортировка расчёской' + '\n')
        fa.writelines('Количество слов: ' + str(len(arr)) + '\n')
        fa.writelines('Время выполнения: ' + str(ttime[0]) + ' секунд' + '\n' + 'Статистика (количество слов на каждую букву алфавита)' + '\n')
        Signs = ['абвгдеёжзийклмнопрстуфкцчшщъыьэюя']
        count = 0
        for s in range(len(Signs[0])): #Проверка начала слова двойным циклом. Изначально неправильно прочитал задание и сделал подсчёт вообще всех букв в тексте (Там было 3 цикла)
            for p in range(len(arr)):
                    if arr[p][0] == Signs[0][s]:
                        count+=1
            fa.writelines(str(Signs[0][s])+": "+str(count) + '\n')
            print(Signs[0][s], ": ", count)
            count = 0

    with open('F:/Practics/Output/Result1.txt','w') as fo: # Бояре не закрывают файлы, они используют with
        for j in range(len(arr)-1):
            fo.writelines(arr[j])
            if arr[j][0].lower() != arr[j+1][0].lower():
                fo.writelines('\n')
            else:
                fo.writelines(' ')

with open('F:/Practics/Input/Original1.txt','r+') as f: # Бояре не закрывают файлы, они используют with
    arrraw = [row.strip() for row in f.read().split()] # Сырой лист(массив)
    arr = [row.strip('.,!?—:;()«»-IV1234567890') for row in arrraw] # без знаков препинания и тп.
    while ('' in arr): # Удаление пустых ячеек. Из-за удаления знаков препинания некоторые ячейки стали пустыми. Чтобы верно определить количество слов и работать с листом(массивом) нужно их удалить
            arr.remove('')
ttime = sort(arr)
output(arr, arrraw)

