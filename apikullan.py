from tkinter import *
from tkinter.scrolledtext import ScrolledText
import requests
from bs4 import BeautifulSoup
import webbrowser

link = input("Wikipedia linki:\n")

r = requests.get(link)
soup = BeautifulSoup(r.content,'html.parser')

about = ""

for paragraph in soup.findAll("p"):
    about += paragraph.text    


"""
f = open("about.txt","w",encoding="UTF-8")
f.write(about)
f.close()

webbrowser.open("about.txt")
"""


"""
______________

GELİŞTİRİLİYOR
______________
"""
root = Tk()
root.attributes('-fullscreen',True)
"""
text = Text()
sb = Scrollbar()
text.insert(END,about)
sb.pack(side=RIGHT)
text.pack(side=LEFT)
"""

st = ScrolledText(width=1360,height=760)
st.insert(END,about)
st.pack(expand=True)

root.mainloop()

# print(r.text)