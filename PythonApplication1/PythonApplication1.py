
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
def output(arr, arrraw): #����� � ������� � � 2 ����� (�������� ����� � ��� ������)
    print('�������� �����: ','\n')
    for x in arrraw:
        print(x,' ', end="")
    print('\n')
    print('������� 8: ���������, �� ��������, �� �����������, ������������ �����, ���������� ���������')
    print('���������� ����: ',len(arr))
    print('����� ����������: ',ttime[0], '������')

    with open('F:/Practics/Analysis/Analysis1.txt','w')as fa: # ����� �� ��������� �����, ��� ���������� with
        fa.writelines('�������� �����:'+'\n')
        for word in arrraw: #����� ������ ������
            fa.write(word + ' ')
        fa.writelines('\n' + '\n') 
        fa.writelines('������� 8: ���������, �� ��������, �� �����������, ������������ �����, ���������� ���������' + '\n')
        fa.writelines('���������� ����: ' + str(len(arr)) + '\n')
        fa.writelines('����� ����������: ' + str(ttime[0]) + ' ������' + '\n' + '���������� (���������� ���� �� ������ ����� ��������)' + '\n')
        Signs = ['��������������������������������']
        count = 0
        for s in range(len(Signs[0])): #�������� ������ ����� ������� ������. ���������� ����������� �������� ������� � ������ ������� ������ ���� ���� � ������ (��� ���� 3 �����)
            for p in range(len(arr)):
                    if arr[p][0] == Signs[0][s]:
                        count+=1
            fa.writelines(str(Signs[0][s])+": "+str(count) + '\n')
            print(Signs[0][s], ": ", count)
            count = 0

    with open('F:/Practics/Output/Result1.txt','w') as fo: # ����� �� ��������� �����, ��� ���������� with
        for j in range(len(arr)-1):
            fo.writelines(arr[j])
            if arr[j][0].lower() != arr[j+1][0].lower():
                fo.writelines('\n')
            else:
                fo.writelines(' ')

with open('F:/Practics/Input/Original1.txt','r+') as f: # ����� �� ��������� �����, ��� ���������� with
    arrraw = [row.strip() for row in f.read().split()] # ����� ����(������)
    arr = [row.strip('.,!?�:;()��-IV1234567890') for row in arrraw] # ��� ������ ���������� � ��.
    while ('' in arr): # �������� ������ �����. ��-�� �������� ������ ���������� ��������� ������ ����� �������. ����� ����� ���������� ���������� ���� � �������� � ������(��������) ����� �� �������
            arr.remove('')
ttime = sort(arr)
output(arr, arrraw)

