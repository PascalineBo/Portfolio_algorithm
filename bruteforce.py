from itertools import combinations

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
        self.share_name = share_name
        self.share_face_value = share_face_value
        self.share_2yrs_profit_percentage = share_2yrs_profit_percentage


class Controller:
    """initializes shares' list"""
    def __init__(self, view):
        # model
        self.shares = []

        # views
        self.view = view

    def get_shares_data(self):
        """récupère les données actions"""
        self.shares = []  # initialise la liste des actions
        while len(self.shares) < SHARES_NUMBER:
            share_name = self.view.prompt_for_share_name()
            share_face_value = int(self.view.prompt_for_share_face_value())
            share_2yrs_profit_percentage = self.view.prompt_for_profit()
            if not share_name:
                return
            elif not share_face_value:
                return
            elif not share_2yrs_profit_percentage:
                return

            share = Share(share_name, share_face_value, share_2yrs_profit_percentage)
            self.shares.append(share)
        return self.shares

    def shares_lists_possibilities(self):
        """lists shares in different order"""
        combinations_dic = {}
        for i in range(len(self.shares), 0, -1):
            possible_lists = combinations(self.shares, i)
            for shares_portfolio in possible_lists:
                shares_sum = sum(share.share_face_value for share in shares_portfolio)
                if shares_sum <= MAX_INVESTMENT:
                    benefit_sum = sum(share.share_face_value
                                      * share.share_2yrs_profit_percentage
                                      for share in shares_portfolio)
                    combinations_dic[shares_portfolio] = benefit_sum
        """looks for max benefit in the dictionnary"""
        max_benefit = round(max(combinations_dic.values()), 2)
        print("le rendement maximum est:" + str(max_benefit) + " EUR")

        """retrieves the best-yield portfolio: """
        max_portfolio = max(combinations_dic, key=combinations_dic.get)

        print("le Portefeuille le plus optimisé est:")
        for share in max_portfolio:
            print(share.share_name, ", valeur: " + str(share.share_face_value))

    def run(self):
        """runs the functions"""
        self.get_shares_data()
        for share in self.shares:
            print(share.share_face_value, share.share_2yrs_profit_percentage)
        self.shares_lists_possibilities()


def main():
    view = View()
    forcebrute = Controller(view)
    forcebrute.run()


main()
