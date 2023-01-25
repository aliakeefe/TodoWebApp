def read_todo_list(filepath='todo_list.txt'):
    '''
    Read the .txt file and appends each item to a list
    :param filepath: .txt file
    :return: the list
    '''
    with open(filepath, 'r') as file:
        todo_list = file.readlines()
    return todo_list


def write_todo_list(todo_arg, filepath='todo_list.txt'):
    '''
    Updates the .txt file with the updated list
    :param todo_arg: A list of all the items to do
    :param filepath: .txt file
    :return:
    '''
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
