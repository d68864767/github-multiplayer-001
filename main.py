'''
This is the main file for the multiplayer github game.
'''

import game
import player
import network

def main():
    # Create game instance
    my_game = game.Game()

    # Create player instances
    player1 = player.Player("Player 1")
    player2 = player.Player("Player 2")

    # Create network instance
    my_network = network.Network()

    # Connect players to the network
    my_network.connect(player1)
    my_network.connect(player2)

    # Start the game
    my_game.start()

if __name__ == "__main__":
    main()
