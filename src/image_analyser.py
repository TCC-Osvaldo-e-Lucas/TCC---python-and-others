from PIL import Image

img = Image.open("images\\teste2_greensleves_cqt_chroma.png")


print(img.size)

img_cut=img.crop((0,0,1,480))
img_cut.save("images\\faixa teste.png","png")