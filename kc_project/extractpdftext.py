#from pypdf import PdfReader
#reader = PdfReader("data.pdf")
#page = reader.pages[0]
#print(page.extract_text())
#for i in range(len(reader.pages)):
   # page = reader.pages[i]

#for i in page.images:
  #  with open (i.name, 'wb') as f:
   #     f.write(i.data)
    
#import pdfplumber
#with pdfplumber.open('data.pdf') as f:
#    for i in f.pages:
 #       print(i.extract_tables())


import  fitz
doc = fitz.open('data.pdf')
pages=(doc.page_count)
#print(doc.metadata)
for i in range(pages):
               page = doc.load_page(i)
               print(page.get_text())
