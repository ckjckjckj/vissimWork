#!/user/env python
# _*_ coding:utf-8 _*_
import xml.dom.minidom
path = r'C:\Users\Mr.Chen\Desktop\\new\\1121.sig'
dom = xml.dom.minidom.parse(path)
root =dom.documentElement
sgList = dom.documentElement.getElementsByTagName('progs')[0].getElementsByTagName('sgs')[0].getElementsByTagName('sg')
dom.documentElement.getElementsByTagName('progs')[0].getElementsByTagName('prog')[0].setAttribute("offset",'20')
for sg in sgList:
    sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[0].setAttribute("begin",'20')
    sg.getElementsByTagName('cmds')[0].getElementsByTagName('cmd')[1].setAttribute("begin",'30')

f = open(r'C:\Users\Mr.Chen\Desktop\\new\\111.sig','w')
dom.writexml(f)
print(1)