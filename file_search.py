
def file_search(folder, filename):
    result = False

    for i in range(1, len(folder)):

        if type(folder[i]) == list:
            local_result = file_search(folder[i], filename)

            if not local_result == False:
                result = folder[0] + '/' + local_result

        elif type(folder[i] == str):

            if folder[i] == filename:
                result = folder[0] + '/' + folder[i]

    return result

res = file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
print(res)