from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str,
                 favourite_dish: str, hammer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hammer_level = hammer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. "
                f"{self.nickname} "
                f"has a hummer of the {self._hammer_level} level")

    def get_rating(self) -> int:
        return self._hammer_level + 4
