import os
from operator import itemgetter

from config.settings import ACCOUNT_BACKUPS_DIR
from utils.files import read_json

EXCLUDED_ACCOUNTS = {
    'Payments (Rajput Usman)': 'addf211d203c077bc5c6b78f41ddc68481804539de4bd3fd736fa853514551c0',
    'Payments (Taiwo Odetola)': 'f0fe0fdff41db888a0938882502ee809f6874c015aa09e11e38c8452d4175535',
    'Treasury': '6ad6deef2a65642a130fb081dacc2010c7521678986ed44b53a845bc00dd3924',
}
EXCLUDED_ACCOUNT_NUMBERS = EXCLUDED_ACCOUNTS.values()


def run():
    """
    Run main application
    """

    file_path = os.path.join(ACCOUNT_BACKUPS_DIR, '2020-12-02-14:47:37.json')
    data = read_json(file_path)
    dict_list = [{'account_number': k, **v} for k, v in data.items()]

    rows_by_balance = sorted(dict_list, key=itemgetter('balance'), reverse=True)
    rows_by_balance = [i for i in rows_by_balance if i['account_number'] not in EXCLUDED_ACCOUNT_NUMBERS]

    for row in rows_by_balance:
        print(row)


if __name__ == '__main__':
    run()
