# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:21:54 2021

@author: MTAEXAM
"""

score=[]
while True:#一直進入迴圈模式
    inscore=int(input("分數"))
    if (inscore==""):
        break#直到碰到break才會跳出迴圈
    else:
        score.append(inscore)
        score2=sorted(score,reverse=True)
#        score.sort()
#        scort.reverse()#由大到小排列
    print(score2)


