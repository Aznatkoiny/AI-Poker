from game import PokerGame

if __name__ == "__main__":
    game = PokerGame(num_players=4)
    rounds_to_play = 5
    for _ in range(rounds_to_play):
        game.play_round()

