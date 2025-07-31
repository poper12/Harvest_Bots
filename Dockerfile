FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 main.py

#This repo is developed by @aaru_2075, don't you fucking dare to remove credit. [Ask @aaru_2075 before reselling it]
#For Paid bot or support contact on @Manga_Campus_Chat
