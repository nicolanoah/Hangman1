# hangman.py

def get_secret_word():
    """Fragt das geheime Wort ab (von einer zweiten Person z. B.)."""
    word = input("Bitte das geheime Wort eingeben (ohne Umlaute, keine Leerzeichen): ").strip().lower()
    # Optional: kleine Validierung
    while not word.isalpha():
        print("Bitte nur Buchstaben ohne Leerzeichen eingeben.")
        word = input("Geheimes Wort: ").strip().lower()
    print("\n" * 50)  # „Bildschirm leeren“, damit der Ratende das Wort nicht sieht
    return word


HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def display_game_state(secret_word, guessed_letters, wrong_attempts, max_attempts):
    """Zeigt ASCII-Galgen, den aktuellen Wortzustand und bereits geratene Buchstaben."""
    print(HANGMAN_PICS[wrong_attempts])
    print(f"Fehlversuche: {wrong_attempts} / {max_attempts}")

    # Wort mit Unterstrichen/Buchstaben
    displayed_word = []
    for ch in secret_word:
        if ch in guessed_letters:
            displayed_word.append(ch)
        else:
            displayed_word.append("_")
    print("Wort: ", " ".join(displayed_word))

    # Bereits geratene Buchstaben sortiert anzeigen
    if guessed_letters:
        print("Geratene Buchstaben: ", " ".join(sorted(guessed_letters)))
    print("-" * 30)


def play_game(secret_word):
    secret_word = secret_word.lower()
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1  # 0–6 bei 7 Bildern

    # Hauptspielschleife
    while True:
        display_game_state(secret_word, guessed_letters, wrong_attempts, max_attempts)

        # Check: gewonnen?
        if all(ch in guessed_letters for ch in secret_word):
            print("🎉 Glückwunsch! Du hast das Wort erraten:", secret_word)
            break

        # Check: verloren?
        if wrong_attempts >= max_attempts:
            print("💀 Leider verloren! Das Wort war:", secret_word)
            break

        guess = input("Bitte einen Buchstaben raten: ").strip().lower()

        # einfache Eingabeprüfung
        if len(guess) != 1 or not guess.isalpha():
            print("Bitte genau EINEN Buchstaben eingeben.")
            continue

        if guess in guessed_letters:
            print("Diesen Buchstaben hast du schon geraten!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Gut geraten! '{guess}' ist im Wort.")
        else:
            print(f"Leider falsch. '{guess}' ist nicht im Wort.")
            wrong_attempts += 1


if __name__ == "__main__":
    # Variante 1: Wort per Eingabe
    secret = get_secret_word()

    # Variante 2 (Alternative): Du könntest hier auch ein Wort hart codieren:
    # secret = "hangman"

    play_game(secret)
