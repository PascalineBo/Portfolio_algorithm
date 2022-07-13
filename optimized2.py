import csv
import math

MAX_INVESTMENT = 500


class Share:
    """Stocke les données d'une action"""
    def __init__(self, share_name, share_face_value, share_2yrs_profit_percentage):
        self.name = share_name
        self.face_value = share_face_value
        self._2yrs_profit_percentage = share_2yrs_profit_percentage


class Controller:
    """initializes shares' list"""
    def __init__(self):
        # model
        self.shares = []

    def get_shares_data(self):
        """récupère les données actions"""
        self.shares = []  # initialise la liste des actions

        # get the data from csv file under a dictionnary form
        with open('dataset1_Python+P7.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(float(row['price'])) > 0:
                    name = row['name']
                    face_value = math.ceil(float(row['price']))# rounds share price
                    # to higher integer
                    _2yrs_profit_percentage = float(row['profit'])/100
                    share = Share(name, face_value, _2yrs_profit_percentage)
                    self.shares.append(share)
                else:
                    print("Mauvaise saisie de l'action:", row['name'], row['price'], row['profit'])

        return self.shares

    def portfolio_combinations(self, MAX_INVESTMENT, shares):
        shares = self.shares
        # matrix creation for portfolio value calculation,
        # in order to optimize portfolio yield:
        matrix = [[0 for x in range(MAX_INVESTMENT+1)] for x in range(len(shares)+1)]

        # matrix population:
        print(len(shares)+1)
        for i in range(1, len(shares) + 1):
            for portfolio_investment in range(1, MAX_INVESTMENT + 1):
                if shares[i-1].face_value <= portfolio_investment:
                    matrix[i][portfolio_investment] \
                        = max(shares[i-1]._2yrs_profit_percentage*shares[i-1].face_value
                              + matrix[i-1][portfolio_investment-shares[i-1].face_value],
                              matrix[i-1][portfolio_investment])
                else:
                    matrix[i][portfolio_investment] = matrix[i-1][portfolio_investment]

        # get the portfolio content corresponding to portfolio optimized yield
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
        print("Soit un nombre total d'actions de: ", len(shares_selection))

        """write best portfolio data in csv file"""
        with open('best_portfolio.csv', 'w', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=',')
            # write headers in csv file
            writer.writerow(['Share_Name', 'Share_face_value'])
            # wites share names and shares values in csv file
            for share in shares_selection:
                writer.writerow((share.name, share.face_value))

        return matrix[-1][-1]

    def run(self):
        self.get_shares_data()
        self.portfolio_combinations(MAX_INVESTMENT, self.shares)
        print("Le rendement optimal du portefeuille est: ",
              round(self.portfolio_combinations(MAX_INVESTMENT, self.shares), 2))


def main():
    optimization = Controller()
    optimization.run()


main()
