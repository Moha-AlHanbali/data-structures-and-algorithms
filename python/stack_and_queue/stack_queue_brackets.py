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

    string_queue = Queue()
    queue_counter = 0
    string_stack = Stack()
    stack_counter = 0

    alternate = True
    validation = True

    for char in string:
        if (char in brackets.values()) and (alternate == True):
            string_queue.enqueue(char)
            alternate = False
            queue_counter += 1
            continue

        if (char in brackets.values()) and (alternate == False):
            string_stack.push(char)
            alternate = True
            stack_counter += 1
            continue

    if not queue_counter == stack_counter:
        validation = False
        print(validation)
        return validation

    queue_node = string_queue.front
    stack_node = string_stack.top


    while queue_node:

        validation = False

        if queue_node.value == brackets["round_bracket_open"]:
            expected_value = brackets["round_bracket_close"]

        elif queue_node.value == brackets["square_bracket_open"]:
            expected_value = brackets["square_bracket_close"]

        elif queue_node.value == brackets["curly_bracket_open"]:
            expected_value = brackets["curly_bracket_close"]

        elif queue_node.value == brackets["round_bracket_close"]:
            expected_value = brackets["round_bracket_open"]

        elif queue_node.value == brackets["square_bracket_close"]:
            expected_value = brackets["square_bracket_open"]

        elif queue_node.value == brackets["curly_bracket_close"]:
            expected_value = brackets["curly_bracket_open"]



        stack_node = string_stack.top

        while stack_node:
            print("passing", queue_node.value, stack_node.value, expected_value)
            if stack_node.value == expected_value:
                print("REAL", queue_node.value, stack_node.value, expected_value)
                stack_node.value = ""
                validation = True

                break

            stack_node = stack_node.next


        queue_node = queue_node.next

    print(validation)
    return validation


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
    # validate_brackets("{(})")
