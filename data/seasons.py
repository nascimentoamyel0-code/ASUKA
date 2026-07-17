from datetime import datetime


class SeasonEngine:
    def __init__(self):
        self.today = datetime.now()

    def get_current_season(self):
        day = self.today.day
        month = self.today.month

        if day == 31 and month == 10:
            return "halloween"

        if day == 25 and month == 12:
            return "christmas"

        if day == 1 and month == 1:
            return "new_year"

        if day == 30 and month == 6:
            return "asuka_birthday"

        return None

    def get_season_message(self):
        season = self.get_current_season()

        if season == "halloween":
            return "🎃 Feliz Halloween... você ouviu isso também?"

        if season == "christmas":
            return "🎄 Feliz Natal! Espero que seu dia seja bem especial."

        if season == "new_year":
            return "🎆 Feliz Ano Novo! Vamos construir coisas incríveis este ano."

        if season == "asuka_birthday":
            return "Hoje é meu aniversário... obrigada por continuar me evoluindo. 💙"

        return None