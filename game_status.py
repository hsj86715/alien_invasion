class GameStatus():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_status()

        # 让游戏一开始处于非活动状态
        self.game_active = False
        # 在任何情况下都不应该重置最高得分
        self.highest_score = 0
        self.file_name = "game_status.txt"
        self.read_highest_score()

    def reset_status(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_highest_score(self):
        try:
            with open(self.file_name, 'r') as file_obj:
                self.highest_score = int(file_obj.read())
        except FileNotFoundError:
            print(self.file_name + " Not found!")
        except ValueError:
            print("invalid literal")

    def upgrade_highest_score(self):
        self.highest_score = self.score
        with open(self.file_name, 'w') as file_obj:
            file_obj.write(str(int(self.highest_score)))
