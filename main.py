
def input_error(func):
    def wrapper(a):
        print("\n{:_^50}\n|".format("LETS GOO!"))
        try:
            result = func(a)
            return result
        except TypeError:
            print('Oh nooo... , its TypeError')
        except IndexError:
            print('Oh nooo... , its IndexError')
        except KeyError:
            print('Oh nooo... , its KeyError')
@input_error
def add_contact(string):
    contact[string[0]] = string[1]


@input_error
def change(string):
    contact[string[0]] = string[1]


@input_error
def phone(string):
    print(contact[string[0]])



def main():
    commands = {
        'add': add_contact,
        'change': change,
        'phone': phone,
    }

    break_commands = [
        'break', 'quit', 'stop',
        'exit', 'good bye', 'close', 'q'
    ]

    print("\n{:_^50}\n|".format('CACTUS'))
    process = True
    while process:
        sentence = input("|-- ").lower().strip()
        command = sentence.split()

        if sentence == "":
            continue
        elif sentence in break_commands:
            print('| Goog bye')
            process = False

        elif sentence == "hello":
            print("| How can i help u?")

        elif sentence == "show all":
            for i in contact:
                print(i, contact[i])

        elif command[0] in commands:
            commands[command[0]](command[1:])

        else:
            print("Sry , but i dont understand Pls try again")

if __name__ == "__main__":
    contact = {
        'Ramaha': '+380980498023'
    }
    main()

