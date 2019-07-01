class GameStats:
    """Track statistics for Alien Invasion"""
    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # start Alien Invasion in an inactive state.
        self.game_active = False

        # high score should never be reset.
        file = open("high_score.txt", 'r')
        h_s = file.read()
        self.high_score = int(h_s)
        file.close()

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
