def is_braces_sequence_correct(s:str):
    """ Проверяет корректность скобочной последовательности
        из круглых '()' и квадратных '[]' скобок.
    """
    A_stack = []
    for brace in s:
        if brace not in "()[]":
            continue
        
        if brace in "([":
            A_stack.append(brace)
        else:
            assert brace in ")]", f"Ожидалась закрывающая скобка: {str(brace)}"
            if len(A_stack) == 0:
                return False
                
            left = A_stack.pop()
            assert left in "([", f"Ожидалась открывающая скобка: {str(brace)}"
            right = ")" if left == "(" else "]"
        
            if right != brace:
                return False

    return len(A_stack) == 0
            

if __name__ == "__main__":
    seq = "(norm[i])"
    print(f"Correct braces:\n\tinp {seq}\n\tout {is_braces_sequence_correct(seq)}")

    seq = "unnorm([)])"
    print(f"Correct braces:\n\tinp {seq}\n\tout {is_braces_sequence_correct(seq)}")