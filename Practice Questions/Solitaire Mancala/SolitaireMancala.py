class SolitaireMancala:
    
    def __init__(self):
        self.houses = [0]
    
    def set_board(self, configuration):
        self.houses = list(configuration)
    
    def __str__(self):
        aux = self.houses
        aux.reverse()
        return str(aux)
    
    def get_num_seeds(self, house_num):
        return self.houses[house_num]
    
    def is_legal_move(self, house_num):
        if house_num > 0 and house_num < len(self.houses):
            return self.houses[house_num] == house_num
    
    def apply_move(self, house_num):
        house_value = self.houses[house_num]
        
        if self.is_legal_move(house_num):
            for i in range(house_num):
                self.houses[i] += 1
             
            self.houses[house_num] = 0
    
    def choose_move(self):
        for i in range(1, len(self.houses)):
            if self.is_legal_move(i):
                return i
        return 0
    
    def is_game_won(self):
        for i in range(1, len(self.houses)):
            if self.houses[i] != 0:
                return False
        return True
    
    
    
import poc_mancala_gui
poc_mancala_gui.run_gui(SolitaireMancala())
                
        
        