import streamlit as st

num_cards = 5
cards = [
    "card_images/cards/2_of_clubs.png",
    "card_images/cards/3_of_clubs.png",
    "card_images/cards/4_of_clubs.png",
    "card_images/cards/5_of_clubs.png",
    "card_images/cards/6_of_clubs.png",
]

with st.expander("Player 1 Hand", expanded=True):
    columns = st.columns(num_cards)
    for column, card in zip(columns, cards[:num_cards]):
        column.image(card)

with st.expander("Player 2 Hand", expanded=False):
    columns = st.columns(num_cards)
    for column, card in zip(columns, cards[:num_cards]):
        column.image(card)
