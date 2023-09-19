from PyPDF2 import PdfWriter, PdfReader

wpdf = PdfWriter()

rpdf1 = PdfReader(open('1.pdf', 'rb'))
wpdf.add_page(rpdf1.pages[0])

rpdf2 = PdfReader(open('2.pdf', 'rb'))
wpdf.add_page(rpdf2.pages[0])

with open("output.pdf","wb") as output:
  wpdf.write(output)
