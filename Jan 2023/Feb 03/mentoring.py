
# filter task
credit_cards = [
    {"number": "4242 4242 4242 4242", "expired": False},
    {"number": "4242 4242 4242 4243", "expired": False},
    {"number": "4242 4242 4242 4245", "expired": True},
    {"number": "4242 4242 4242 4246", "expired": False},
    {"number": "4242 4242 4242 4247", "expired": True},
    {"number": "4242 4242 4242 4248", "expired": False},
    {"number": "4242 4242 4242 4249", "expired": True},
]
# Extra a new list called "expired_cards" from list of credit_cards. Check whether they are expired and store them there.
# expired_cards = filter(lambda card: card['expired'], credit_cards)
# print(list(expired_cards))
def has_expired(card):
    return card['expired']
expired_cards = filter(has_expired, credit_cards) # filter object
#expired_cards_numbers = map(lambda card: card['number'], list(expired_cards))
#expired_cards = list(expired_cards)
expired_cards_numbers = []
for card in expired_cards:
    expired_cards_numbers.append(card['number'])
#print(list(expired_cards))
print(list(expired_cards_numbers))

