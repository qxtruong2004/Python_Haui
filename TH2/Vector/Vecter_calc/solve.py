''': Cộng hai véc tơ (cộng các 
tọa độ tương ứng), trừ hai véc tơ, tính khoảng cách OX, lấy đối xứng qua gốc 
tọa độ X’ = (-x1, -x2, -x3'''
import math
from Vector.Vector_input import Vector_info
def cong_vector(vector1, vector2):
    a1 = vector1[0] + vector2[0]
    a2 = vector1[1] + vector2[1]
    a3 = vector1[2] + vector2[2]
    return [a1, a2, a3] # trả về list

def tru_vector(vector1, vector2):
    a1 = vector1[0] - vector2[0]
    a2 = vector1[1] - vector2[1]
    a3 = vector1[2] - vector2[2]
    return [a1, a2, a3]

def khoangcach(vector):
    x = math.sqrt((vector[0]**2) + (vector[1]**2) + (vector[2]**2))
    print('Khoảng cách OX là: ', x)

def doixung(vector):
    new_vector = list(map(lambda x : x*-1, vector))
    print("Tọa độ điểm đối xứng: ", new_vector)
