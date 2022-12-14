import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys
import datetime



keys="1234567890ABCD"
n=random.randint(1,6)
num=random.randint(0,n-1)
listpasswds=[]
print (num)
f=open("xxx","w+")
for j in range(n):
    passwd=""
    for k in range(4):
        passwd=passwd+keys[random.randint(0,13)]
    listpasswds.append(passwd)
    f.write(passwd+"\n")
f.close()
message="Добро пожаловать в СНТ мирэашник!\n\n Введите код ниже для прохода через калитку\n\n" + listpasswds[num]+"\n\nНикому не сообщайте этот код!\nВы получили это сообщение, так как было произведено 3 неудачных попытки входа и был запрошен mail код для вашего участка.\n\nТех. вопросы: +71111111111"
msg = MIMEMultipart()
password = "Intelekt2023"
msg['From'] = "mireas2023@gmail.com"
f0=open(sys.argv[1][:-1]+"logCout","r")
f1=open(sys.argv[1][:-1]+"log","a")
f=open(sys.argv[1][:-1]+"mail")
msg['To'] = f.read()
f1.write(str(datetime.datetime.now())[0:16]+"/"+"запрошен новый mail код\n")
f.close()
f1.close()
buffer=str(int(f0.read())+1) 
f0.close()
f0=open(sys.argv[1][:-1]+"logCout","w+")
f0.write(buffer)
f0.close()
msg['Subject'] = "["+listpasswds[num]+"]"+" код для прохода на территорию СНТ"
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'],msg.as_string())
server.quit()

