class ClubCard:
    def __init__(self, card_id, cost, card_type, available_activities, validity_period):
        self.card_id = card_id
        self.cost = cost
        self.card_type = card_type
        self.available_activities = available_activities
        self.validity_period = validity_period

# cream obiectele 
card1 = ClubCard(1, 5000, "Basic", ["Gym", "Yoga"], 30)
card2 = ClubCard(2, 8000, "Premium", ["Gym", "Yoga", "Innot"], 60)
card3 = ClubCard(3, 3000, "Starter", ["Gym"], 15)
card4 = ClubCard(4, 6000, "Starter", ["Sauna , Innot"], 35)

# salvarea obiectelor
club_cards = {
    card1.card_id: card1,
    card2.card_id: card2,
    card3.card_id: card3,
    card4.card_id: card4,
}

# afisarea informatiilor sdespre carduri
for card_id, card in club_cards.items():
    print(f"Cardul #{card.card_id}")
    print(f"Pret: {card.cost} руб.")
    print(f"Tip: {card.card_type}")
    print(f"Activitati disponibile: {', '.join(card.available_activities)}")
    print(f"Termen de valabilitate: {card.validity_period} zile")
    print("-" * 30)
