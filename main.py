class Token:

    def __init__(self, tok_type, lexeme):
        self.token = tok_type
        self.lexeme = lexeme


class Lexer:

    def __init__(self, input_file):             #input file is source, index is pos
        self.input_file = input_file
        self.index = 0
        self.length = len(input_file)

        self.keywords = {
            'integer','if','else', 'fi', 'while',
                         'return', 'get', 'put', 'boolean', 'real',
                         'function', 'true', 'false'
        }

    def skip_comm_ws(self):

        while self.index < self.length:
            curr_char = self.input_file[self.index]

            if curr_char in [' ', '\t', '\n', '\r']:
                self.index += 1
                continue

            if curr_char == "!":
                self.index += 1


                while self.index < self.length and self.input_file[self.index] != "!":
                    self.index += 1

                self.index += 1
                continue
            break


    def fsm_identifier(self):
       state = 1
       lexeme = ""

       while self.index < self.length:
           char = self.input_file[self.index]

           if state == 1:
               if char.isalpha() or char.isdigit() or char == '.':
                   lexeme += char
                   self.index += 1
               else:
                   break


       if lexeme.lower() in self.keywords:
           return Token("keyword", lexeme.lower())
       else:
           return Token("identifier", lexeme)


    def fsm_int(self):
        lexeme = ""

        while self.index < self.length:
            char = self.input_file[self.index]

            if char.isdigit():
                lexeme += char
                self.index += 1
            elif char == ".":
                return self.fsm_real(lexeme)
            else:
                break
        return Token("integer",lexeme)

    def fsm_real(self,curr_lexeme=""):
        lexeme = curr_lexeme

        if self.index < self.length and self.input_file[self.index] == ".":
            lexeme += '.'
            self.index += 1

        more_digits = False

        while self.index < self.length:
            char = self.input_file[self.index]

            if char.isdigit():
                more_digits = True
                lexeme += char
                self.index += 1
            else:
                break

        if more_digits:
            return Token("real",lexeme)
        else:
            return Token("unknown", lexeme)

    def lexer(self):

        self.skip_comm_ws()

        if self.index >= self.length:
            return None

        curr_char = self.input_file[self.index]

        if curr_char.isalpha():
            return self.fsm_identifier()
        elif curr_char.isdigit():
            return self.fsm_int()
        elif curr_char == ".":
            return self.fsm_real()

        else:
            self.index += 1

            if self.index < self.length:
                next_char = self.input_file[self.index]
                two_char = curr_char + next_char

                if two_char in ['==', '!=', '<=', '>=']:
                    self.index += 1
                    return Token("operator", two_char)
            if curr_char in ['=', '>', '<', '+', '-', '*', '/']:
                return Token("operator", curr_char)
            elif curr_char in [';', ',', '(', ')', '{', '}', '@']:
                return Token("separator", curr_char)

        return Token("unknown",curr_char)


def main():
    inputFile_1 = "test_1.txt"
    outputFile_1 = "output_1.txt"

    inputFile_2 = "test_2.txt"
    outputFile_2 = "output_2.txt"

    inputFile_3 = "test_3.txt"
    outputFile_3 = "output_3.txt"

    #process 1
    with open(inputFile_1,'r') as input_f:
        input_file = input_f.read()

    analyzer_1 = Lexer(input_file)

    with open(outputFile_1,'w') as output_file:
        output_file.write(f"{'Token':<20} {'Lexeme'}\n")
        output_file.write("-"* 40 + "\n")

        while True:
            tokens = analyzer_1.lexer()

            if tokens is None:
                break

            print(f"{tokens.token:<20} {tokens.lexeme}")

            output_file.write(f"{tokens.token:<20} {tokens.lexeme}\n")

    #process 2
    with open(inputFile_2,'r') as input_f:
        input_file = input_f.read()

    analyzer_2 = Lexer(input_file)

    with open(outputFile_2,'w') as output_file:
        output_file.write(f"{'Token':<20} {'Lexeme'}\n")
        output_file.write("-"* 40 + "\n")

        while True:
            tokens = analyzer_2.lexer()

            if tokens is None:
                break

            print(f"{tokens.token:<20} {tokens.lexeme}")

            output_file.write(f"{tokens.token:<20} {tokens.lexeme}\n")

    #process 3

    with open(inputFile_3,'r') as input_f:
        input_file = input_f.read()

    analyzer_3 = Lexer(input_file)

    with open(outputFile_3,'w') as output_file:
        output_file.write(f"{'Token':<20} {'Lexeme'}\n")
        output_file.write("-"* 40 + "\n")

        while True:
            tokens = analyzer_3.lexer()

            if tokens is None:
                break

            print(f"{tokens.token:<20} {tokens.lexeme}")

            output_file.write(f"{tokens.token:<20} {tokens.lexeme}\n")

if __name__ == "__main__":
    main()

