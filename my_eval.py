

def my_eval(expression):
    """
    Simple eval function that supports:
    - Positive integers
    - Operations: +, -, *, /
    - Parentheses for grouping  
    
    Args:
        expression: String containing a mathematical expression
    
    Returns:
        Result of evaluating the expression (as integer or float)
    """
    expression = expression.replace(' ', '')  # Remove whitespace
    pos = [0]  # Use list to allow modification in nested calls
    
    def parse_expression():
        """Parse addition and subtraction (lowest precedence)."""
        result = parse_term()
        while pos[0] < len(expression) and expression[pos[0]] in '+-':
            op = expression[pos[0]]
            pos[0] += 1
            right = parse_term()
            if op == '+':
                result = result + right
            else:  # op == '-'
                result = result - right
        return result
    
    def parse_term():
        """Parse multiplication and division (higher precedence)."""
        result = parse_factor()
        while pos[0] < len(expression) and expression[pos[0]] in '*/':
            op = expression[pos[0]]
            pos[0] += 1
            right = parse_factor()
            if op == '*':
                result = result * right
            else:  # op == '/'
                result = result / right
        return result
    
    def parse_factor():
        """Parse numbers and parenthesized expressions."""
        if pos[0] >= len(expression):
            raise ValueError("Unexpected end of expression")
        
        if expression[pos[0]] == '(':
            # Handle parentheses
            pos[0] += 1  # Skip '('
            result = parse_expression()
            if pos[0] >= len(expression) or expression[pos[0]] != ')':
                raise ValueError("Missing closing parenthesis")
            pos[0] += 1  # Skip ')'
            return result
        else:
            # Parse a positive integer
            return parse_number()
    
    def parse_number():
        """Parse a positive integer."""
        if pos[0] >= len(expression):
            raise ValueError("Unexpected end of expression")
        
        start = pos[0]
        # Check if first character is a digit
        if not expression[pos[0]].isdigit():
            raise ValueError(f"Expected positive integer, found '{expression[pos[0]]}'")
        
        # Read all consecutive digits
        while pos[0] < len(expression) and expression[pos[0]].isdigit():
            pos[0] += 1
        
        num_str = expression[start:pos[0]]
        return int(num_str)
    
    if not expression:
        raise ValueError("Empty expression")
    
    result = parse_expression()
    
    # Check if we parsed the entire expression
    if pos[0] < len(expression):
        raise ValueError(f"Unexpected character '{expression[pos[0]]}' at position {pos[0]}")
    
    return result


# Example usage and tests
if __name__ == "__main__":
    # Basic arithmetic
    assert my_eval("2 + 3") == 5
    assert my_eval("10 - 4") == 6
    assert my_eval("3 * 4") == 12
    assert my_eval("15 / 3") == 5.0
    assert my_eval("8 / 3") == 8 / 3
    
    # Operator precedence
    assert my_eval("2 + 3 * 4") == 14
    assert my_eval("10 - 4 / 2") == 8.0
    assert my_eval("2 * 3 + 4") == 10
    
    # Parentheses
    assert my_eval("(2 + 3) * 4") == 20
    assert my_eval("2 * (3 + 4)") == 14
    assert my_eval("(10 - 4) / 2") == 3.0
    assert my_eval("((2 + 3) * 4)") == 20
    
    # Complex expressions
    assert my_eval("1 + 2 * 3 + 4") == 11
    assert my_eval("(1 + 2) * (3 + 4)") == 21
    assert my_eval("100 / 10 / 2") == 5.0
    
    print("All tests passed!")
