import PySimpleGUI as sg

home_screen = [
    [sg.Text("Click on a Deck to begin Reviewing Cards",
             justification='center')],
    [sg.Text("Deck 1: 14 Cards", justification='center', enable_events=True, key='deck1')],
    [sg.Text("Deck 2: 15 Cards", justification='center', enable_events=True, key='deck2')],
    [sg.Text("Deck 3: 16 Cards", justification='center', enable_events=True, key='deck3')],
    [sg.Text("Deck 4: 1 Card", justification='center', enable_events=True, key='deck4')],
    [sg.Button("Create Deck"), sg.Button("Create Card")],
    [sg.Button("View All Cards")]
]

def review_window():
    review = [
        [sg.Button("Return To Deck"), sg.Button("Edit Card")],
        [sg.Text("Flash Card 1 Front Text")],
        [sg.Text("Flash Card Back Tex")],
        [sg.Button("Reveal Back")],
        [sg.Text("Rate remembering difficulty")],
        [sg.Button("Easy 1"), sg.Button("Normal 2"), sg.Button("Hard 3"), sg.Button("Forgot 4")]

    ]
    review_window = sg.Window(title="Review", layout=review, modal=True)

    while True:
        event, values = review_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Return To Deck":
            review_window.close()

def create_card_window():
    create_card = [
        [sg.Text("Edit your new card to start adding cards")],
        [sg.Text("Deck this card belongs to (Required)"), sg.Input()],
        [sg.Text("Back of cart contents"), sg.Input()],
        [sg.Button("Save Card"), sg.Button("Cancel")]
    ]
    create_card_window = sg.Window(title="Create Card", layout=create_card, modal=True)

    while True:
        event, values = create_card_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Cancel":
            create_card_window.close()

def deck_window():
    deck = [
        [sg.Text("You can Review cards, create them, or view cards in this Deck.",
                 expand_x=True, justification='c')],
        [sg.Text("Deck 1", font=('Helvetica', 14, 'bold'))],
        [sg.Text("CARDS DUE")],
        [sg.Text("4")],
        [sg.Button(
                "Review"), sg.Button("Create Card"), sg.Button("View Cards"), sg.Button("Cancel")]
    ]
    deck_window = sg.Window(title="deck 1", layout=deck, modal=True)

    while True:
        event, values = deck_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Review":
            review_window()
        elif event == "Create Card":
            create_card_window()
        elif event == "View Cards":
            sg.popup_scrolled("Created Flash Cards Go Here\nCreated Flash Cards Go Here \n", title="scrolled popup")
        elif event == "Cancel":
            deck_window.close()

def view_cards_window():
    layout1= [
        [sg.Text("Card 1")],
        [sg.Text("Card 2")]
    ]
    view_cards = [
        [sg.Column(layout1, size=(400, 200), scrollable=True, key = "Column")],
        [sg.Button("View"), sg.Button("Delete"), sg.Button("Cancel")]
    ]
    view_cards_window = sg.Window(title="View Cards", layout=view_cards)

    while True:
        event, values = view_cards_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Delete":
            sg.popup_yes_no("Do you want to delete this card?", title="Delete Card?")
        elif event == "Cancel":
            view_cards_window.close()


window = sg.Window(title="hello", layout=home_screen)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Create Deck":
        text = sg.popup_get_text('Enter Deck Name', title="New Deck")
        print(text)
    elif event == 'deck1':
        deck_window()
    elif event == "Create Card":
        create_card_window()
    elif event == "View All Cards":
        view_cards_window()


window.close()
