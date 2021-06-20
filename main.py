import os
from datetime import datetime

from thenewboston.constants.network import MAX_POINT_VALUE
from thenewboston.utils.network import fetch

from config.settings import ACCOUNT_BACKUPS_DIR, LATEST_BACKUP_DIR
from utils.files import write_json
from utils.format_results import format_results

PRIMARY_VALIDATOR_IP = '54.219.183.128'


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
    account_backup_file_path = os.path.join(ACCOUNT_BACKUPS_DIR, f'{date_time}.json')
    latest_backup_file_path = os.path.join(LATEST_BACKUP_DIR, 'latest.json')

    data = format_results(fetch_account_data())
    verify_results(data=data)

    write_json(file=account_backup_file_path, data=data)
    write_json(file=latest_backup_file_path, data=data)


def verify_results(*, data):
    """
    Ensure total coins is equal to
    """

    total = sum(v['balance'] for k, v in data.items())

    if total == MAX_POINT_VALUE:
        print('\nValid')
    else:
        print('\nInvalid')


if __name__ == '__main__':
    run()
