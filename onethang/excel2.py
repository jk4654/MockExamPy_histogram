# -*- coding: utf-8 -*-
#연도별 표준점수 분포 그래프
from openpyxl import load_workbook
import matplotlib.pyplot as plt
# import numpy as np

parameters = [["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2015학년도.xlsx", 243, 321, 2015], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2016학년도.xlsx", 236, 310, 2016], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2017학년도.xlsx", 94, 171, 2017], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2018학년도.xlsx", 92, 173, 2018], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2019학년도.xlsx", 81, 159, 2019], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2020학년도.xlsx", 91, 173, 2020], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2021학년도.xlsx", 93, 172, 2021]]
print(parameters[0][0])

f, axes = plt.subplots(1, len(parameters))

def function1(path, i, f1, y):
    load_wb = load_workbook(path, data_only=True)

    load_ws = load_wb['Sheet1']

    # x = np.arange(81)

    M_fq = []
    W_fq = []

    #남자 도수 리스트 
    get_cells_M = load_ws['D{}'.format(i) : 'D{}'.format(f1)]
    for row in get_cells_M:
        for cell in row:
            M_fq.append(cell.value)

    #여자 도수 리스트
    get_cells_W = load_ws['E{}'.format(i) : 'E{}'.format(f1)]
    for row in get_cells_W:
        for cell in row:
            W_fq.append(cell.value)

    people_fq = [x+y for x,y in zip(M_fq,W_fq)]

    #표준점수의 계급 리스트 T_score
    T_score = []
    get_cells_Ts = load_ws['C{}'.format(i) : 'C{}'.format(f1)]
    for row in get_cells_Ts:
        for cell in row:
            T_score.append(cell.value)

    print(T_score)
    
    
    axes[pltIndex].bar(T_score, people_fq)
    axes[pltIndex].set_title(y)

    # plt.show()

# function("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/수능도수분포_2021.xlsx", 89, 169)

# function("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2021학년도.xlsx", 173, 253)
pltIndex = 0
for p in parameters:
    function1(p[0], p[1], p[2], p[3])
    pltIndex = pltIndex + 1

plt.show()