#coding:UTF-8
import win32com
from win32com.client import Dispatch,constants


w=win32com.client.Dispatch('Word.Application')
w.Visible=0
w.DisplayAlerts=0
doc = w.Documents.Open(r'C:/Users/djj/Desktop/test/adad.docx') 

#插入文字
# myRange=doc.Range(0,0)  		#在文档的第一行的第一个地方插入
# myRange.InsertBefore('Hello')


#打印文件
doc.PrintOut()


#关闭
doc.Close()
w.Documents.Close()
w.Quit()