from xml.etree.ElementTree import parse
import json, codecs, sys

dir = sys.argv[1]

tree = parse(dir)

root = tree.getroot()
pages = root.findall("page")[1:]

dic = dict()
for page in pages:
    title=page.findtext("title")
    text=page.find("revision").findtext("text")
    dic[title] = text

with open('wiki.json','wb') as f:
    json.dump(dic, codecs.getwriter('utf-8')(f), ensure_ascii=False)