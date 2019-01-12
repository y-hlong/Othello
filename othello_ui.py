#Yin Hao Long 49256403
import othello_logic
import check_move_flip

def user_interface():
    '''
    Runs the function that asks for inputs for the game. Also loops and asks players to
    make turn until game ending condition is met.
    '''
    print('FULL')
    print('Input rows, columns, starting color, top left color, and winning conditions (> or <)')
    game_state = get_game_info()
    game_state.initial_board_setup()
    while True:
        if game_state.check_winner()[0] == True:
            print('{}  {}'.format('B: ' + str(game_state.check_number_of_B()), 'W: ' + str(game_state.check_number_of_W())))
            game_state.display_board()
            print(game_state.check_winner()[1])
            return
        print('{}  {}'.format('B: ' + str(game_state.check_number_of_B()), 'W: ' + str(game_state.check_number_of_W())))
        game_state.display_board()
        game_state.check_no_valid_move()
        print("{}".format('TURN: ' + game_state.current_players_turn()))
        game_state.check_no_valid_move()
        if game_state.check_winner()[0] == True:
            print(game_state.check_winner()[1])
            return
        while True:
            input_coordinate = input().split(" ")
            for xy in range(len(input_coordinate)):
                input_coordinate[xy] = int(input_coordinate[xy]) - 1
            if game_state.make_turn(check_move_flip.check_move().test_all_possibilities(input_coordinate, game_state.current_gamestate(), game_state.current_players_turn(), game_state.next_players_turn())[0]) !=  False:
                print('VALID')
                break
            else:
                print('INVALID')
                
        

            
def get_game_info() -> 'board_state':
    '''
    Returns a board_state according to info the user inputs.
    '''
    return othello_logic.board_state(int(input()), int(input()), input(), input(), input())

if __name__ == '__main__':
    user_interface()
    
