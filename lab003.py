import lab_chat as lc

## Part 1.
def get_username():
    username = input('Enter your desired username: ')
    return username.strip().upper()

def get_group():
    group_name = input("Enter the group name you'd like to join: ")
    return group_name.strip().upper()

def get_message():
    user_message = input('Enter the message you would like to send: ')
    return user_message.strip()

def initialize_chat():
    """
    This function coordinates the setup by calling Part 1 functions
    and passing their results into the peer-to-peer library.
    """
    #1. Capture user data using Part 1 functions
    username = get_username()
    group_name = get_group()

    #2. Use lab_chat functions to connect
    # UNSURE - you lost me here.... but I'll try
    node = lc.get_peer_node(username)
    lc.join_group(node, group_name)

    #3. Information returned by Part 1 functions
    """
    username returns a selected username
    group_name returns a selected group
    user_message returns a selected message
    """
    channel = lc.get_channel(username)

    return channel

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            user_message = input('Enter your message: ')
            channel.send(user_message.encode('utf-8'))
        except KeyboardInterrupt, SystemExit:
            break
    channel.send("Stop.")
    print("FINISHED")