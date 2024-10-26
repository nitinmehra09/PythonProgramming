from main import play_game

class TestPlayGame:

    def test_play_game_invalid_input():
        result = play_game(-2, -1)
        assert result == "Invalid input", f"Expected 'Invalid input' but got {result}"

    def test_play_game_invalid_input():
        result = play_game(0, 2)
        assert result is None, "Expected None for invalid input, but got a result."


    def test_play_game_player1_wins_with_gun():
        result = play_game(0, 1)


    def test_play_game_player1_1_player2_0():
        result = play_game(1, 0)
        assert result == "Player 2 wins!"
    def test_play_game_player1_0_player2_minus1():
        result = play_game(0, -1)
        assert result == "Player 2 wins!"

    def test_play_game_player1_wins_snake_vs_water():
        result = play_game(1, -1)
        assert result == "Player 1 wins!"
        assert result == "Player 1 wins!"
    def test_play_game_invalid_input():
        result = play_game(2, 0)
        assert result == "Invalid input!", f"Expected 'Invalid input!', but got {result}"
    pass

    def test_play_game_tie_water():
        assert play_game(-1, -1) == "It's a tie!"


    def test_play_game_tie_when_both_choose_snake():
        result = play_game(1, 1)
        assert result == "It's a tie!"

    def test_play_game_tie_when_both_choose_gun():
        result = play_game(0, 0)
        assert result == "It's a tie!"
