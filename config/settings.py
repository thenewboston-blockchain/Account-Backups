import os

# Core
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directories
ACCOUNT_BACKUPS_DIR = os.path.join(BASE_DIR, 'account_backups')
LATEST_BACKUP_DIR = os.path.join(BASE_DIR, 'latest_backup')
