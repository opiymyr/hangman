import game

game.load_words()
game.choose_word()
game.prepare_mask()
game.show_welcome()

while game.is_game_on():
    game.show_state()
    letter = game.ask_letter()
    if game.is_repeated(letter):
        game.show_repeated()
    elif game.is_in_word(letter):
        game.open_letter(letter)
        game.show_hit()
    else:
        game.add_mistake(letter)
        game.show_miss()

game.show_result()
