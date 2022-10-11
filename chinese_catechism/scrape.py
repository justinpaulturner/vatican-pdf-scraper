import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfMerger

URL = "https://www.vatican.va/chinese/ccc_zh.htm"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
pdf_urls = ["https://www.vatican.va/chinese/" + e.find("a").get("href") for e in soup.find_all("li")]

for url in pdf_urls:
    response = requests.get(url)
    s_path = "files/" + url.split("/")[-1]
    with open(s_path, 'wb') as f:
        f.write(response.content)

pdf_files = ["files/" + url.split("/")[-1] for url in pdf_urls]

with PdfMerger() as merger:

    for pdf in pdf_files:
        merger.append(pdf)

    merger.write("Chinese_Catechism_Full.pdf")
