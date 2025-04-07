from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx import Document
from docx.shared import Pt
from bs4 import BeautifulSoup
from docx.shared import Mm
import requests
import re


def dngffdfkg(doc):
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    return doc

while True:
    url = input("введите ссылку на статью Википедии: ")

    if "https://ru.wikipedia.org" not in url:
        print("ну мы тебя же просили типа ввести статью на Википедию что ты делаешь")
    else:
        break

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, features="html.parser")
some_headline = soup.find('h1', class_="firstHeading mw-first-heading")
news_block = soup.find('div', class_="mw-content-ltr mw-parser-output")
tags = news_block.find_all(['p', "h1", "h2", "h3", "h4", "h5", "h6", "img"])
tags = [some_headline] + tags


for i in range(len(tags) - 1, -1, -1):
    if "<p" in str(tags[i]):
        w = i
        break

tags = tags[:w + 1]

doc = Document()

doc = dngffdfkg(doc)


for tag in tags:
    if "<p>" in str(tag):
        paragraph = doc.add_paragraph(re.sub(r'\[.*?\]', '', tag.text))
        paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if "<h1" in str(tag):
        head = doc.add_heading(tag.text, level=1)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h2" in str(tag):
        head = doc.add_heading(tag.text, level=2)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h3" in str(tag):
        head = doc.add_heading(tag.text, level=3)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h4" in str(tag):
        head = doc.add_heading(tag.text, level=4)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h5" in str(tag):
        head = doc.add_heading(tag.text, level=5)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<h6" in str(tag):
        head = doc.add_heading(tag.text, level=6)
        head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if "<img" in str(tag):
        response = requests.get("https:" + tag['src'], headers=headers)
        response.raise_for_status()
        with open('filename.png', "wb") as f:
            f.write(response.content)
        doc.add_picture('filename.png')
        imag = doc.paragraphs[-1]
        imag.alignment = WD_ALIGN_PARAGRAPH.CENTER
doc.save('test.docx')


