def len_file():
    with open('log.txt', 'r') as file:
        data = file.read()
        return data


def delete_logs():
    with open('log.txt', 'w') as file:
        file.write('')
