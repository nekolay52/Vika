from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx import Document
from docx.shared import Pt
from bs4 import BeautifulSoup
import requests


def dngffdfkg(doc):
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    return doc

url = "https://ru.wikipedia.org/wiki/Rust_(игра)"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, features="html.parser")
some_headline = soup.find('h1', class_="firstHeading mw-first-heading")
divan = soup.find('div', class_="mw-content-ltr mw-parser-output")
tosh_divan = divan.find_all(['p', "h1", "h2", "h3", "h4", "h5"])

# print(some_headline.text)
# for i in tosh_divan:
#     print(i.text)

doc = Document()

doc = dngffdfkg(doc)

for teg in tosh_divan:
    if "<p>" in str(teg):
        s = doc.add_paragraph(teg.text)
        s.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# head = doc.add_heading('Добавление заголовка документа', level=1)
# head2 = doc.add_heading(' заголовка документа', level=2)
# head.alignment = WD_ALIGN_PARAGRAPH.CENTER
# head2.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save('test.docx')

print(tosh_divan[0])