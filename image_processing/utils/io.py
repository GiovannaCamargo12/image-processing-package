from skimage.io import imread, imsave

def leia_imagem(path, is_gray = False):
    imagem = imread(path, as_gray = is_gray)
    return imagem

def salve_imagem(imagem, path):
    imsave(path, imagem) 
