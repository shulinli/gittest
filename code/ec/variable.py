import os

dirname = os.path.dirname(os.path.dirname(__file__))

'''filePath'''
filePath = os.path.join(dirname,"files")

'''file type'''
fileType = "All Files (*);;Word Files (*.doc;*.docx);;Text Files (*.txt);;" \
           "PDF Files (*.pdf);;XML Files (*.xml);;HTML Files (*.htm;*.html,*.mhtml);;" \
           "RTF Files (*.rtf)"

'''size of every block'''
chunkSize = 1024*1024 #1MB

'''directory of file block'''
directory = os.path.join(dirname,"blocks")

'''sockets information'''
ip_port = ("localhost",8080)
