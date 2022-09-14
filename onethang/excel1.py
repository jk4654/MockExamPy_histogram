# -*- coding: utf-8 -*-
#연도별 1~9등급 인원수
from openpyxl import load_workbook
import matplotlib.pyplot as plt
# import numpy as np

parameters = [["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2015학년도.xlsx", 243, 321, 2015], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2016학년도.xlsx", 236, 310, 2016], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2017학년도.xlsx", 94, 171, 2017], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2018학년도.xlsx", 92, 173, 2018], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2019학년도.xlsx", 81, 159, 2019], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2020학년도.xlsx", 91, 173, 2020], ["C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2021학년도.xlsx", 93, 172, 2021]]
print(parameters[0][0])

f, axes = plt.subplots(1, len(parameters))




def level(path, i, f1, y):
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
    sum_M_fq = sum(M_fq)
    print(sum_M_fq)
    #여자 도수 리스트
    get_cells_W = load_ws['E{}'.format(i) : 'E{}'.format(f1)]
    for row in get_cells_W:
        for cell in row:
            W_fq.append(cell.value)
    sum_W_fq = sum(W_fq)
    print(sum_W_fq)
    people = [x+y for x,y in zip(M_fq,W_fq)]
    print(people)
    #등급 리스트 level
    levels = [9,8,7,6,5,4,3,2,1]
    
    #각 등급의 인원 수 리스트 level_fq
    level_fq = [0,0,0,0,0,0,0,0,0]
    
    
    for i in people:
        if sum(level_fq) < sum(people)*0.04:
            level_fq[0] = level_fq[0] + i
        elif sum(level_fq) < sum(people)*0.11:
            level_fq[1] = level_fq[1] + i
        elif sum(level_fq) < sum(people)*0.23:
            level_fq[2] = level_fq[2] + i
        elif sum(level_fq) < sum(people)*0.40:
            level_fq[3] = level_fq[3] + i
        elif sum(level_fq) < sum(people)*0.60:
            level_fq[4] = level_fq[4] + i
        elif sum(level_fq) < sum(people)*0.77:
            level_fq[5] = level_fq[5] + i
        elif sum(level_fq) < sum(people)*0.89:
            level_fq[6] = level_fq[6] + i
        elif sum(level_fq) < sum(people)*0.96:
            level_fq[7] = level_fq[7] + i
        else:
            level_fq[8] = level_fq[8] + i
    print(level_fq)


    axes[pltIndex].bar(levels, level_fq)
    axes[pltIndex].set_title(y)

    

pltIndex = 0
for p in parameters:
    level(p[0], p[1], p[2], p[3])
    pltIndex = pltIndex + 1

plt.show()



# function("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/수능도수분포_2021.xlsx", 89, 169)

# function("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2021학년도.xlsx", 173, 253)

# level("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2015학년도.xlsx", 243, 321, 2015)
# level("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2017학년도.xlsx", 94, 171, 2017)

# level("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2018학년도.xlsx", 92, 173, 2018)
# level("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2019학년도.xlsx", 81, 159, 2019)
# level("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2020학년도.xlsx", 91, 173, 2020)
# level("C:/Users/박진규/OneDrive/바탕 화면/compiler/도수분포/대학수학능력시험 9월 모의평가 표준점수-도수분포_2021학년도.xlsx", 93, 172, 2021)