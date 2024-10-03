class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.hole_cards = []
        self.chips = chips
        self.current_bet = 0
        self.is_active = True  # Indicates if the player is still in the current hand

    def receive_cards(self, cards):
        self.hole_cards.extend(cards)

    def show_hole_cards(self):
        return [str(card) for card in self.hole_cards]

    def place_bet(self, amount):
        if amount > self.chips:
            amount = self.chips  # All-in
        self.chips -= amount
        self.current_bet += amount
        return amount

    def reset_for_new_round(self):
        self.hole_cards = []
        self.current_bet = 0
        self.is_active = True
