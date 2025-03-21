import cv2


from helpers import cut, find, process_image_text

#passando parametros para que a funcione: caminho para imagem, quantidade de linhas do caça palavras quantidade de colunas do caça palavras e um array com as palavras a serem encontradas
image_path = "./src/caca_palavras2.jpg"
find_elements = ["WTF", "NEO", "BLEED", "RUSU"]
lines = 7
columns = 7
#leitura inicial da imagem
original_image = cv2.imread(image_path)

def main(original_image, lines, columns):
    gray, top, bottom, x_axis, height = cut(original_image, lines)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    data = [[], []]

    for x in range(lines):

        left = 0

        #cortando a imagem
        cropped_image = thresh[top:bottom, left:x_axis]

        #fazendo leitura inicial da imagem cortada para identificação das letras
        customConfig = '--oem 3 --psm 6'
        
        data_line = process_image_text(cropped_image, customConfig)
            
        #mudando diminuindo o zoom caso tenham mais de 1 letra a mais encontradas na linha para melhor identificação delas
        if(len(data_line) >= (columns+2)):
            resized_image = cv2.resize(original_image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
            
            new_gray, new_top, new_bottom, new_x_axis, new_height = cut(resized_image, lines, columns)
            
            _, new_thresh = cv2.threshold(new_gray, 200, 255, cv2.THRESH_BINARY)

            new_left = 0
            
            if(x>=1):
                new_bottom = (new_bottom + new_height*x)
                new_top = (new_top + new_height*x)
                    
            new_cropped_image = new_thresh[new_top:new_bottom, new_left:new_x_axis]
            
            data_line = process_image_text(new_cropped_image, customConfig)

        #mudando arbitrariamente o threshold da imagem caso sejam identificadas menos letras ou apenas uma letra a mais do que deveria
        if (len(data_line) == (columns+1) or len(data_line) < columns):
            _, thresh_replace = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
            cropped_image = thresh_replace[top:bottom, left:x_axis]
            
            data_line = process_image_text(cropped_image, customConfig)
        
        data[0].append(data_line)
        
        #adicionando colunas no array baseado ja nas linhas escaneadas
        for i, letter in enumerate(data[0][x]):
            if(len(data[1]) <= i):
                data[1].append(letter)
            else:
                data[1][i] = data[1][i] + letter
          
        
        data_line = ""
        
        #calculo para a altura da próxima linha a ser lida
        bottom = bottom + height
        top = top + height
            
    return find(data, find_elements)

print(main(original_image, lines, columns))