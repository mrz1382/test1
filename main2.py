class Node:
    def init(self, coefficient, power):
        self.coefficient = coefficient
        self.power = power
        self.next = None

class Polynomial:
    def init(self):
        self.head = None

    def add_term(self, coefficient, power):
        new_node = Node(coefficient, power)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add_polynomial(self, other_poly):
        result = Polynomial()
        current_self = self.head
        current_other = other_poly.head

        while current_self and current_other:
            if current_self.power > current_other.power:
                result.add_term(current_self.coefficient, current_self.power)
                current_self = current_self.next
            elif current_self.power < current_other.power:
                result.add_term(current_other.coefficient, current_other.power)
                current_other = current_other.next
            else:
                result.add_term(current_self.coefficient + current_other.coefficient, current_self.power)
                current_self = current_self.next
                current_other = current_other.next

        while current_self:
            result.add_term(current_self.coefficient, current_self.power)
            current_self = current_self.next

        while current_other:
            result.add_term(current_other.coefficient, current_other.power)
            current_other = current_other.next

        return result

    def multiply_polynomial(self, other_poly):
        result = Polynomial()
        current_self = self.head

        while current_self:
            current_other = other_poly.head
            while current_other:
                coefficient = current_self.coefficient * current_other.coefficient
                power = current_self.power + current_other.power
                result.add_term(coefficient, power)
                current_other = current_other.next
            current_self = current_self.next

        return result

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.power}", end=" ")
            if current.next:
                print("+", end=" ")
            current = current.next
        print()

# Input two polynomials
def input_polynomial():
    poly = Polynomial()
    n = int(input("Enter the number of terms in the polynomial: "))
    for _ in range(n):
        coefficient = int(input("Enter the coefficient: "))
        power = int(input("Enter the power: "))
        poly.add_term(coefficient, power)
    return poly

# Create and display two polynomials
print("Enter the first polynomial:")
poly1 = input_polynomial()
poly1.display()

print("Enter the second polynomial:")
poly2 = input_polynomial()
poly2.display()

# Calculate and display the sum of polynomials
print("Sum of polynomials:")
sum_poly = poly1.add_polynomial(poly2)
sum_poly.display()

# Calculate and display the product of polynomials
print("Product of polynomials:")
product_poly = poly1.multiply_polynomial(poly2)
product_poly.display()