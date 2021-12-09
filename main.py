from game import Player
from game_manager import GameManager

def hello():
    print(
        '''
    888~-_            888   _                          ,d88~~\                                             
    888   \   e88~-_  888 e~ ~   e88~~8e  888-~\       8888     e88~~8e  888-~\ Y88b    /  e88~~8e  888-~\ 
    888    | d888   i 888d8b    d888  88b 888          `Y88b   d888  88b 888     Y88b  /  d888  88b 888    
    888   /  8888   | 888Y88b   8888__888 888           `Y88b, 8888__888 888      Y88b/   8888__888 888    
    888_-~   Y888   ' 888 Y88b  Y888    , 888             8888 Y888    , 888       Y8/    Y888    , 888    
    888       "88_-~  888  Y88b  "88___/  888          \__88P'  "88___/  888        Y      "88___/  888    
    
    > Bem vindo!
        '''
    )

def main():
    hello()

    p1_name = input("Qual seu nome? ")
    print("");

    game_manager = GameManager();
    game_manager.create_game(Player(p1_name), Player("Bot Bob"));
    # game_manager.describe();
    game_manager.start_game();

if __name__ == '__main__':
    main()

