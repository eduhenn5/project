from game2dboard import*

def mouse(btn, lin,col):# jogada botão 1 e 3 "gravando sua posição"
    if btn == 1 and v[lin][col] is None: 
        v[lin][col] = "1"
        posicao()
    if btn == 3 and v[lin][col] is None:
        v[lin][col] = "3"
        posicao()
        
def posicao():
    for i in range(3): #Linhas
        if(v[i][0] == v[i][1] == v[i][2] and v[i][0]):
            return v.print('Venceu! Pressione t para reniciar o jogo!')
    
    for i in range(3): #Colunas
        if(v[0][i] == v[1][i] and v[1][i] == v[2][i] and v[0][i]):
            return v.print('Venceu! Pressione t para reniciar o jogo!')
        
   
        #Diagonal principal
    if(v[1][1] == v[0][0] and v[0][0] == v[1][1] and v[1][1] == v[2][2]):
        return v.print('Venceu! Pressione t para reniciar o jogo!')
        
        
        #Diagonal secundaria
    if(v[0][2] == v[0][2] and v[0][2] == v[1][1] and v[1][1] == v[2][0]):
        return v.print('Venceu! Pressione t para reniciar o jogo!')
    
    for i in range(3):#analisa a matriz se possui valores diferentes retorna empate.
        for j in range(3):
            if(v[i][j] == 0):
                return False
    return v.print('empate')
      
    
def tecladofn(key):
    if key == "t":
        v.clear() 
         
v = Board(3, 3)
v.title = "Jogo da Velha"
v.cell_size = 90
v.cell_color = "#ffffff"
v.cell_spacing = 5
v.grid_color = "#00264d"
v.on_mouse_click = mouse
v.on_key_press = tecladofn
v.create_output()
v.show()