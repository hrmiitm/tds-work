import pymupdf

doc = pymupdf.open("Book.pdf")

print(len(doc)) # 285


print('-'*30)
print(doc[7].get_text())
print('-'*30)

# can we ["page1 data", "page2 text",.....]
# [doc[0], doc[1], doc[2], ...., doc[284]]

all_pages_array = [ page.get_text() for page in doc ]

print(all_pages_array[7])