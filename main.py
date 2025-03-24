from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx import Document
from docx.shared import Pt
from bs4 import BeautifulSoup
import requests
import re


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
ocnovnoy = soup.find('div', class_="mw-content-ltr mw-parser-output")
tosh_divan = ocnovnoy.find_all(['p', "h1", "h2", "h3", "h4", "h5", "h6", "img"])
tosh_divan = [some_headline] + tosh_divan

#удоление пустЮ разд-ов

for i in range(len(tosh_divan) - 1, -1, -1):
    if "<h" not in str(tosh_divan[i]):
        w = i
        break

qyqy = tosh_divan[:w + 1]

doc = Document()

doc = dngffdfkg(doc)


for teg in qyqy:
    if "<p>" in str(teg):
        w = re.sub(r'\[.*?\]', '', teg.text)
        s = doc.add_paragraph(w)
        s.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if "<h1" in str(teg):
        head = doc.add_heading(teg.text, level=1)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h2" in str(teg):
        head = doc.add_heading(teg.text, level=2)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h3" in str(teg):
        head = doc.add_heading(teg.text, level=3)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h4" in str(teg):
        head = doc.add_heading(teg.text, level=4)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h5" in str(teg):
        head = doc.add_heading(teg.text, level=5)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h6" in str(teg):
        head = doc.add_heading(teg.text, level=6)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<img" in str(teg):
       print("<img")

doc.save('test.docx')

