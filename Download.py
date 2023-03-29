# This Python file uses the following encoding: utf-8
import os
import subprocess
import mysql.connector
import requests

headers = {
    # 填入伪造的IP地址
    'X-Forwarded-For': '*.*.*.*'
}

FilePath = "E:/Project/Python/爬虫/科学文库/book/"
surl = input("请输入书籍页链接：")
value = surl.split('=')[1]
# print(value)
url = "https://book.sciencereading.cn/shop/book/Booksimple/offlineDownload.do?id=" + value +"&readMark=1"
# print(url)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="科学文库"
)

mycursor = mydb.cursor()

SQL = "SELECT 图书名称 FROM information WHERE value = " + "\'" + value + "\'"
# print(SQL)
mycursor.execute(SQL)

myresult = mycursor.fetchall()[0][0]
myresult = myresult.replace('|', '_')
myresult = myresult.replace(' ', '')
print(f"正在下载《{myresult}》")

res = requests.get(url, headers=headers)

if res.status_code == 200:
    with open(f"book/{myresult}.pdf", "wb") as f:
        f.write(res.content)
    print("图书下载完成")
    command = f"python decrypt.py -i {FilePath}{myresult}.pdf -o {FilePath}{myresult}_dec.pdf"
    # output = os.popen(command, 'r').readlines()
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    output = process.stdout.read()
    error = process.stderr.read()
    output = output.decode(encoding="gbk")
    error = error.decode(encoding="gbk")
    print(output)
    os.remove(f"{FilePath}{myresult}.pdf")
    print("加密PDF文件已删除")
    os.rename(f"{FilePath}{myresult}_dec.pdf", f"{FilePath}{myresult}.pdf")
    print("PDF文件已重命名")
else:
    print(f"图书下载失败: {res.status_code}")
