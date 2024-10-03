from deck import Deck
from player import Player
from hand_evaluator import evaluate_hand
from ai_agent import AIAgent

class PokerGame:
    def __init__(self, num_players=4):
        self.deck = Deck()
        self.players = [AIAgent(f"AI Player {i+1}") for i in range(num_players)]
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0

    def start_new_round(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        for player in self.players:
            player.reset_for_new_round()

    def deal_hole_cards(self):
        for player in self.players:
            player.receive_cards(self.deck.deal(2))

    def deal_community_cards(self, number):
        self.deck.deal(1)  # Burn a card
        self.community_cards.extend(self.deck.deal(number))
   
    def show_community_cards(self):
        return [str(card) for card in self.community_cards]

    def betting_round(self):
        for player in self.players:
            if player.is_active and player.chips > 0:
                action_str = self.get_player_action(player)
                action_parts = action_str.lower().split()
                action = action_parts[0]
    
                if action == 'fold':
                    player.is_active = False
                elif action == 'call':
                    amount_to_call = self.current_bet - player.current_bet
                    player.place_bet(amount_to_call)
                    self.pot += amount_to_call
                    player.current_bet += amount_to_call
                elif action == 'raise':
                    raise_amount = int(action_parts[1])
                    total_bet = self.current_bet - player.current_bet + raise_amount
                    player.place_bet(total_bet)
                    self.current_bet += raise_amount
                    self.pot += total_bet
                    player.current_bet += total_bet
                else:
                    print(f"Invalid action '{action}' by {player.name}.")

    def get_player_action(self, player):
        if not player.is_active or player.chips == 0:
            return 'fold'
    
        # Prepare the game state for the AI agent
        game_state = {
            'community_cards': [str(card) for card in self.community_cards],
            'pot': self.pot,
            'current_bet': self.current_bet,
            'opponents_actions': [p.current_bet for p in self.players if p != player]
        }
    
        # Use the AI agent's decide_action method
        action = player.decide_action(game_state)
        print(f"{player.name} decides to {action}.")
    
        return action

    def play_round(self):
        self.start_new_round()
        self.deal_hole_cards()
        print("Hole Cards:")
        for player in self.players:
            if player.is_active:
                print(f"{player.name}: {player.show_hole_cards()} (Chips: {player.chips})")

        # Pre-Flop Betting
        self.betting_round()

        # Flop
        self.deal_community_cards(3)
        print("\nFlop:")
        print(self.show_community_cards())
        self.betting_round()

        # Turn
        self.deal_community_cards(1)
        print("\nTurn:")
        print(self.show_community_cards())
        self.betting_round()

        # River
        self.deal_community_cards(1)
        print("\nRiver:")
        print(self.show_community_cards())
        self.betting_round()

        # Determine Winner
        self.determine_winner()

    def determine_winner(self):
        active_players = [p for p in self.players if p.is_active]
        if len(active_players) == 1:
            winner = active_players[0]
            winner.chips += self.pot
            print(f"\nAll other players folded. {winner.name} wins the pot of {self.pot} chips!")
        else:
            player_scores = []
            for player in active_players:
                score = evaluate_hand(player.hole_cards, self.community_cards)
                player_scores.append((player, score))
            # Find the player(s) with the best (lowest) score
            min_score = min(s for p, s in player_scores)
            winners = [p for p, s in player_scores if s == min_score]
    
            if len(winners) > 1:
                print("\nIt's a tie between:")
                for winner in winners:
                    print(f"{winner.name}")
                split_pot = self.pot // len(winners)
                for winner in winners:
                    winner.chips += split_pot
                print(f"Each winner receives {split_pot} chips.")
            else:
                winner = winners[0]
                winner.chips += self.pot
                print(f"\nWinner: {winner.name} wins the pot of {self.pot} chips!")
        # Reset pot and bets
        self.pot = 0
        for player in self.players:
            player.current_bet = 0
            player.is_active = True
        # Display players' chip counts
        print("\nPlayers' Chip Counts:")
        for player in self.players:
            print(f"{player.name}: {player.chips} chips")


