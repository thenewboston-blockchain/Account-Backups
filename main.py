import os
from datetime import datetime

from thenewboston.utils.network import fetch

from config.settings import ACCOUNT_BACKUPS_DIR
from utils.files import write_json
from utils.format_results import format_results

PRIMARY_VALIDATOR_IP = '54.183.17.224'


def fetch_account_data():
    """
    Fetch all account data from primary validator
    Return list of accounts
    """

    results = []

    next_url = f'http://{PRIMARY_VALIDATOR_IP}/accounts'

    while next_url:
        print(next_url)
        data = fetch(url=next_url, headers={})
        accounts = data['results']
        results += accounts
        next_url = data['next']

    return results


def run():
    """
    Run main application
    """

    now = datetime.now()
    date_time = now.strftime('%Y-%m-%d-%H:%M:%S')
    file_path = os.path.join(ACCOUNT_BACKUPS_DIR, f'{date_time}.json')
    write_json(
        file=file_path,
        data=format_results(fetch_account_data())
    )


if __name__ == '__main__':
    run()
