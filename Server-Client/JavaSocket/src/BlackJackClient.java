import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class BlackJackClient {
    public static void main(String[] args) {
        String hostname = "localhost";  // Adresa serverului
        int port = 5555;  // Portul serverului

        try (Socket socket = new Socket(hostname, port)) {  // Se conectează la server
            System.out.println("Conectat la server");

            // Inițializează fluxurile de comunicare
            InputStream input = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(input));

            OutputStream output = socket.getOutputStream();
            PrintWriter writer = new PrintWriter(output, true);

            // Primește mâna inițială a jucătorului
            String initialResponse = reader.readLine();
            System.out.println("Mesajul primit de la server: " + initialResponse);

            if (initialResponse != null) {
                // Extrage informațiile despre mâini
                String[] parts = initialResponse.split("\\|");
                String[] playerCards = parts[0].split(",");
                String dealerCard = parts[1];

                // Afișează mâna jucătorului și cartea vizibilă a dealerului
                System.out.println("Mana ta: " + String.join(" ", playerCards));
                System.out.println("Dealer arata: " + dealerCard);

                Scanner scanner = new Scanner(System.in);
                while (true) {
                    // Cere acțiunea jucătorului
                    System.out.print("Vrei sa dai 'hit' sau 'stand'? ");
                    String action = scanner.nextLine().toLowerCase();

                    if (action.equals("hit") || action.equals("stand")) {
                        writer.println(action);  // Trimite acțiunea către server

                        String serverResponse = reader.readLine();  // Primește răspunsul serverului
                        System.out.println("Răspunsul serverului: " + serverResponse);

                        String[] responseParts = serverResponse.split("\\|");
                        if (responseParts.length == 3) {
                            // Jocul s-a terminat (rezultat final)
                            String result = responseParts[0];
                            String[] dealerHand = responseParts[1].split(",");
                            String dealerScore = responseParts[2];

                            // Afișează rezultatul final
                            System.out.println("Rezultat: " + result);
                            System.out.println("Mana dealerului: " + String.join(", ", dealerHand));
                            System.out.println("Scorul dealerului: " + dealerScore);
                            break;
                        } else {
                            // Actualizare în timpul jocului
                            String[] updatedPlayerCards = responseParts[0].split(",");
                            String playerScore = responseParts[1];
                            System.out.println("Mana ta: " + String.join(", ", updatedPlayerCards));
                            System.out.println("Scorul tau: " + playerScore);
                        }
                    } else {
                        // Mesaj de eroare pentru input invalid
                        System.out.println("Alege 'hit' sau 'stand'!");
                    }
                }
            }
            socket.close();  // Închide conexiunea cu serverul
        } catch (IOException ex) {
            System.out.println("Eroare in client: " + ex.getMessage());  // Tratarea erorilor de rețea
        }
    }
}
