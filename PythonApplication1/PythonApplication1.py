
import time # ���������� ��� ������ ������� (��������)

def sort(arr): #���������� ����� (������) �� ����������� "���������"
    totaltime = 0
    for j in range (1000): #1000 ���������� ��� ������� ����������� �������. 1000 �������� �������� �����, ��������� �� �������������
        start_time = time.time()
        end = len(arr)
        swaps = True
        while end > 1 or swaps:
            end = max(1, int(end / 1.247))
            swaps = False
            for i in range(len(arr) - end):
                j = i + end
                if arr[i].lower() > arr[j].lower(): # ��������� lower ����� �� ��������� �������, ����� �������� �� �����������
                    arr[i], arr[j] = arr[j], arr[i] # � ��� ����� ������� �� lower, ����� ��������� ������� ��� ������
                    swaps = True
        ttime = time.time() - start_time
        totaltime += ttime #����� �� 1000 ���
    return[(totaltime/1000)] #������� � ���� �� 1000


with open('F:/Practics/Input/Original1.txt','r+') as f: # ����� �� ��������� �����, ��� ���������� with
    arrraw = [row.strip() for row in f.read().split()] # ����� ����(������)
    arr = [row.strip('.,!?�:;()��-IV1234567890') for row in arrraw] # ��� ������ ���������� � ��.
    while ('' in arr): # �������� ������ �����. ��-�� �������� ������ ���������� ��������� ������ ����� �������. ����� ����� ���������� ���������� ���� � �������� � ������(��������) ����� �� �������
            arr.remove('')
ttime = sort(arr)