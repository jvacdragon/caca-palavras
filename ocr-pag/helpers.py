import cv2
import pytesseract
import re

#Cortando a imagem para leitura de linhas do caça palavras
def cut(image, lines):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    x_axis = image.shape[0]
    y_axis = image.shape[1]
    height = round((y_axis/lines))

    top = 0
    bottom = round(height)
    
    return(gray, top, bottom, x_axis, height)

#achando a palavra no caça palavras e indicando sua localização baseada na coluna e index inicial
def find(arr, look_for):    
    words_finded = []
    

    for key in look_for:
            for i, line in enumerate(arr[0]):
                
                match = re.search(key, line)
                
                if(match):
                    word = match.group()
                    word_line = i + 1
                    word_index = match.start() + 1
                    
                    words_finded.append({"word": word, "line": word_line, "index": word_index})
                    break
            
            for i, column in enumerate(arr[1]):
                
                match = re.search(key, column)
                
                if(match):
                    word = match.group()
                    word_column = i + 1
                    word_index = match.start() + 1
                    
                    words_finded.append({"word": word, "column": word_column, "index": word_index})
                    break
                    
    return words_finded

#procedimento padrão para processamento dos textos da imagem
def process_image_text(image, customConfig):
        data_line = pytesseract.image_to_string(image, config=customConfig)
        data_line = re.sub(r'[^A-Z]', '', data_line)
        return data_line.replace("\n", "")