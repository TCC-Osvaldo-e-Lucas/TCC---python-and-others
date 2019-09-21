from PIL import Image

img = Image.open(r'C:\Users\Osvaldo\Documents\POLITECNICA\TCC - TrancMusicaPartitura\Python\greensleves_cqt_chroma.png')


print(img.size)

img_cut=img.crop((0,0,1,480))
img_cut.save('faixa 1.png','png')