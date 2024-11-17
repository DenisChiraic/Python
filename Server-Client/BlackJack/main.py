import socket
import random

# Funcție pentru generarea unui pachet complet de 52 de cărți
def playing_deck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♣', '♥', '♦']
    return [f"{value}{suit}" for value in values for suit in suits]

# Funcție pentru calcularea valorii mâinii
def calculate_hand(hand):
    value = 0
    aces = 0
    for card in hand:
        card_value = card[:-1]  # Extrage valoarea cărții (fără simbol)
        if card_value.isdigit():
            value += int(card_value) # Valoare numerică
        elif card_value in ['J', 'Q', 'K']:
            value += 10 # Figuri (J, Q, K) au valoarea 10
        else:
            value += 11 # Așii valorează 11 implicit
            aces += 1
     # Ajustează valoarea Asului la 1 dacă totalul depășește 21
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Funcție principală care gestionează conexiunile și logica jocului
def start_server():
    # Inițializează serverul
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555)) # Se leagă la localhost pe portul 5555
    server_socket.listen(1) # Ascultă pentru conexiuni
    print("Serverul este pornit și așteaptă conexiuni...")

    # Creează pachetul de cărți și îl amestecă
    deck = playing_deck()
    random.shuffle(deck)

    while True:
        client_socket, addr = server_socket.accept() # Acceptă o conexiune de la client
        print(f"Conectat la {addr}")

        # Distribuie câte două cărți pentru jucător și dealer
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Trimite mâna inițială și cartea vizibilă a dealerului
        initial_response = ",".join(player_hand) + '|' + dealer_hand[0] + "\n"
        print(f"Trimit mâna inițială: {initial_response.strip()}")
        client_socket.sendall(initial_response.encode())

        while True:
            # Așteaptă comanda clientului (hit sau stand)
            data = client_socket.recv(1024).decode().strip()
            print(f"Am primit de la client: {data}")

            if data == "hit":
                # Adaugă o carte la mâna jucătorului
                player_hand.append(deck.pop())
                # Dacă jucătorul depășește 21, pierde jocul
                if calculate_hand(player_hand) > 21:
                    result = "bust"
                    break
            elif data == "stand":
                # Dealerul joacă conform regulilor (trage până la minim 17)
                while calculate_hand(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
                # Compară scorurile și determină rezultatul
                player_score = calculate_hand(player_hand)
                dealer_score = calculate_hand(dealer_hand)
                if dealer_score > 21 or player_score > dealer_score:
                    result = "win"
                elif player_score == dealer_score:
                    result = "draw"
                else:
                    result = "lose"
                break

            # Trimite actualizarea mâinii jucătorului
            player_status = ",".join(player_hand) + "|" + str(calculate_hand(player_hand)) + "\n"
            client_socket.sendall(player_status.encode())

        # Trimite rezultatul final și mâna dealerului
        final_response = result + "|" + ",".join(dealer_hand) + "|" + str(calculate_hand(dealer_hand)) + "\n"
        client_socket.sendall(final_response.encode())
        client_socket.close() # Închide conexiunea cu clientul
        break

    server_socket.close()  # Oprește serverul după terminarea conexiunii

if __name__ == '__main__':
    start_server()
