#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
f = open('seoul.csv','r',encoding='cp949') #읽기모드(read)로 읽어오되 'cp949'라는 형식(Windows 한글 인코딩 방식)으로 읽어오기
data = csv.reader(f,delimiter=',') #','을 기준으로 분리해서 저장, delimiter:구분자, 기본값, 생략가능
print(data)
f.close()


# In[ ]:


#다른 운영체제에서 작성된 csv 파일을 윈도 운영체제에서 다룰 때는 encoding='utf8'


# In[2]:


import csv
f = open('seoul.csv',encoding='cp949') 
data = csv.reader(f)

for row in data:
    print(row)
f.close()
#각 행이 []와 ''로 둘러싸여 있음. 리스트, 문자열, 누락


# In[3]:


f = open('seoul.csv') 
data = csv.reader(f)
header = next(data)
print(header)
f.close()


# In[ ]:


f = open('seoul.csv') 
data = csv.reader(f)
header = next(data)
for row in data:
    print(row)
f.close()


# In[ ]:


#서울이 가장 더웠던 날은 언제였을까?
f = open('seoul.csv') 
data = csv.reader(f)
header = next(data)
for row in data:
    if row[-1] == '':
        row[-1] = -999 #-999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1]) #최고기온을 실수로 변환
    print(row)
f.close()


# In[10]:


f = open('seoul.csv') 
data = csv.reader(f)
header = next(data)
max_temp = -999 #최고 기온 값을 저장할 변수
max_date ='' #최고 기온이 가장 높았던 날짜를 저장할 변수

for row in data:
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])
    if max_temp < row[-1]:
        max_date = row[0]
        max_temp = row[-1]
f.close()

print(max_date,max_temp)
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로,',max_temp,'도 였습니다.')

