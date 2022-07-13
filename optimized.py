
SHARES_NUMBER = 20
MAX_INVESTMENT = 500


class View:

    def prompt_for_share_name(self):
        """demande le nom de l'action"""
        share_name = input("tapez le NOM de l'action: ")
        while share_name == "":
            share_name = input("Invalide! veuillez ressaisir")
        return share_name

    def prompt_for_share_face_value(self):
        """demande la valeur faciale de l'action"""
        share_face_value = input("tapez la valeur faciale de l'action: ")
        while (share_face_value == ""):
            share_face_value = input("Invalide! veuillez ressaisir "
                                     "la valeur faciale de l'action:")
        return share_face_value

    def prompt_for_profit(self):
        """demande le genre du joueur ou de la joueuse"""
        try:
            share_2yrs_profit_percentage = float(input("tapez le % de profit après 2 ans:"))
            while (share_2yrs_profit_percentage == ""):
                share_2yrs_profit_percentage = input("Invalide! veuillez ressaisir"
                                                     "le % de profit:")
            return share_2yrs_profit_percentage
        except ValueError:
            print("veuillez saisir un %")


class Share:
    """Stocke les données d'une action"""

    def __init__(self, share_name, share_face_value, share_2yrs_profit_percentage):
        self.name = share_name
        self.face_value = share_face_value
        self._2yrs_profit_percentage = share_2yrs_profit_percentage


class Controller:
    """initializes shares' list"""
    def __init__(self, view):
        # model
        self.shares = []

        # views
        self.view = View

    def get_shares_data(self):
        """récupère les données actions"""
        self.shares = []  # initialise la liste des actions
        while len(self.shares) < SHARES_NUMBER:
            name = self.view.prompt_for_share_name(self)
            face_value = int(self.view.prompt_for_share_face_value(self))
            _2yrs_profit_percentage = self.view.prompt_for_profit(self)
            if not name:
                return
            elif not face_value:
                return
            elif not _2yrs_profit_percentage:
                return

            share = Share(name, face_value, _2yrs_profit_percentage)
            self.shares.append(share)
        return self.shares

    def portfolio_combinations(self, MAX_INVESTMENT, shares):
        shares = self.shares
        matrix = [[0 for x in range(MAX_INVESTMENT+1)] for x in range(len(shares)+1)]
        # matrix creation for portfolio value calculation, in order to optimize portfolio yield

        """matrix population"""
        print(len(shares)+1)
        for i in range(1, len(shares) + 1):
            for portfolio_investment in range(1, MAX_INVESTMENT + 1):
                if shares[i-1].face_value <= portfolio_investment:
                    matrix[i][portfolio_investment] \
                        = max(shares[i-1].face_value * shares[i-1]._2yrs_profit_percentage
                              + matrix[i-1][portfolio_investment-shares[i-1].face_value],
                              matrix[i-1][portfolio_investment])
                    print("Matrice", matrix[i][portfolio_investment])
                else:
                    matrix[i][portfolio_investment] = matrix[i-1][portfolio_investment]

        """get the portfolio content corresponding to portfolio optimized yield"""
        portfolio_investment = MAX_INVESTMENT
        n = len(shares)
        shares_selection = []
        print("Composition du portefeuille optimisé(face value):")
        while portfolio_investment >= 0 and n > 0:
            share = shares[n-1]
            if matrix[n][portfolio_investment] == matrix[n-1][portfolio_investment-share.face_value] + \
                    share.face_value*share._2yrs_profit_percentage:
                print(share.name, share.face_value)
                shares_selection.append(share)
                portfolio_investment -= share.face_value

            n -= 1

        return matrix[-1][-1]

    def run(self):
        self.get_shares_data()
        self.portfolio_combinations(MAX_INVESTMENT, self.shares)
        print("Le rendement optimal du portefeuille est: ",
              round(self.portfolio_combinations(MAX_INVESTMENT, self.shares), 2))


def main():
    view = View()
    optimization = Controller(view)
    optimization.run()


main()
