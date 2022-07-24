import markdown
with open("/Users/naif_tayseer/Desktop/Summer_courses/CS50_WEB/wiki/entries/CSS.md", "r", encoding="utf-8") as input_file:
    text = input_file.read()
html = markdown.markdown(text)
print(html)