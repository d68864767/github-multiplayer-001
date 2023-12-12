'''
This is the network file for the multiplayer github game.
'''

class Network:
    def __init__(self):
        self.players = []

    def connect(self, player):
        # Connect the player to the network
        self.players.append(player)

    def disconnect(self, player):
        # Disconnect the player from the network
        self.players.remove(player)
