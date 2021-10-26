from stack_and_queue.queue  import Queue
from stack_and_queue.stack  import Stack

# from queue  import Queue
# from stack  import Stack

def validate_brackets(string):
    """
    Representing whether or not the brackets in the string are balanced.

    Round Brackets : ()
    Square Brackets : []
    Curly Brackets : {}

    Arguments:
    string: string

    Return: boolean
    """

    brackets = {
    "round_bracket_open" : "(",
    "round_bracket_close" : ")",

    "square_bracket_open" : "[",
    "square_bracket_close" : "]",

    "curly_bracket_open" : "{",
    "curly_bracket_close" : "}"
    }

    string_queue= Queue()
    for char in string:
        if char in brackets.values():
            string_queue.enqueue(char)

    if string_queue.front:
        seek_mode = True
    else:
        seek_mode = False

    while string_queue.front:
        current = string_queue.front

        if current.value == brackets["round_bracket_open"]:
            expected_value = brackets["round_bracket_close"]

        elif current.value == brackets["square_bracket_open"]:
            expected_value = brackets["square_bracket_close"]

        elif current.value == brackets["curly_bracket_open"]:
            expected_value = brackets["curly_bracket_close"]
        else:
            seek_mode = True
            print(not seek_mode)
            return not seek_mode

        seek_mode = True
        string_queue.dequeue()
        current = string_queue.front
        filter_stack = Stack()
        helper_stack = Stack()


        while current:

            filter_stack.push(current.value)
            string_queue.dequeue()


            if current.value == expected_value:
                filter_stack.pop()
                seek_mode = False
                expected_value = None

            current = string_queue.front

        if seek_mode == True:
            print (not seek_mode)
            return not seek_mode

        while filter_stack.top:
            current = filter_stack.top
            helper_stack.push(current.value)
            filter_stack.pop()
            current = current.next

        if helper_stack.top:
            current = helper_stack.top

        if current:
            current = helper_stack.top
            if current.value == brackets["round_bracket_open"]:
                expected_value = brackets["round_bracket_close"]

            elif current.value == brackets["square_bracket_open"]:
                expected_value = brackets["square_bracket_close"]

            elif current.value == brackets["curly_bracket_open"]:
                expected_value = brackets["curly_bracket_close"]
            else:
                seek_mode = True
                print(not seek_mode)
                return not seek_mode


            seek_mode = True
            string_queue = Queue()
            while current:
                helper_stack.pop()
                string_queue.enqueue(current.value)
                current = helper_stack.top


    print(not seek_mode)
    return not seek_mode









# if __name__ == "__main__":
    # validate_brackets("(abcabc)")
    # validate_brackets("(ab)bc)")
    # validate_brackets("(ab(bc)")
    # validate_brackets("(")
    # validate_brackets("{}{Code}[Fellows](())")
    # validate_brackets("(())")
    # validate_brackets("{)}[)")
    # validate_brackets("[({}]")
    # validate_brackets("(](")
    # validate_brackets("{}(){}")
