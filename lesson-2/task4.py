for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif remainder == 0:
        print('У вас', + messages_count + 'новых сообщений.')
    elif remainder >= 5:
        print('У вас', + messages_count + 'новых сообщений.')

    else:
        print('У вас', + str(messages_count) + 'новых сообщения.')