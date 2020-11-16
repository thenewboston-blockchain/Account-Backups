def format_results(data):
    """
    Format result to match the shape of the root account file
    Return results as Python object
    """
    results = dict()
    for entry in data:
        account_id = entry["account_number"]
        balance = entry["balance"]
        balance_lock = entry["balance_lock"]
        results[account_id] = {
            "balance": balance,
            "balance_lock": balance_lock
        }
    
    return results
