from math import sqrt
import csv

TestData = []
LearnData = []

class Data:
    def __init__(self,nomor,emosi,provokasi,hoax):
        self.nomor = nomor
        self.emosi = emosi
        self.provokasi =provokasi
        self.hoax = hoax

class ResultClass:
    def __init__(self, distance, data):
        self.distance = distance
        self.data = data

with open('TrainData.csv', 'r') as f:
    reader1 = csv.reader(f)
    for row in reader1:
        LearnData.append(Data(row[0], row[1], row[2],row[3]))
with open('TestData.csv', 'r') as g:
    reader2 = csv.reader(g)
    for row in reader2:
        TestData.append(Data(row[0], row[1], row[2],""))

def Test(Learn_Data, Test_Data):
    distance  = sqrt((int(Learn_Data.provokasi)-int(Test_Data.provokasi))**2 +(int(Learn_Data.emosi)-int(Test_Data.emosi))**2)
    Result = ResultClass(distance, Learn_Data)
    return Result

def GetClassification(K, Result):
    Count_Ya = 0
    Count_Tidak = 0
    for i in range(0,K-1):
        if (Result[i].data.hoax == "Ya"):
            Count_Ya +=1
        else:
            Count_Tidak +=1

    if (Count_Ya > Count_Tidak):
        return "Ya"
    else:
        return "Tidak"

if __name__ == '__main__':
    K = 11

    for i in range(len(TestData)):
        Result = []
        for j in range(len(LearnData)):
            Result.append(Test(LearnData[j],TestData[i]))
        Result.sort(key=lambda ResultClass: ResultClass.distance,reverse=False)
        print (GetClassification(K,Result))
