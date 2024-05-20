from AccountTransfer.services import read_file
from AccountTransfer.models import Accounts


def run():
    # print(os.getcwd())
    file_path = 'AccountTransfer/accounts.csv'  # Change to your file path

    data = read_file(file_path)
    for user_id, name, balance in zip(data['ID'], data['Name'], data['Balance']):
        Accounts.objects.create(
            user_id=user_id,
            name=name,
            balance=balance
        )
