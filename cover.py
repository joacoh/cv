import pymupdf

doc = pymupdf.open('cv.pdf')
page = doc.load_page(0) 
pix = page.get_pixmap(dpi=300)
pix.save('cover.png')