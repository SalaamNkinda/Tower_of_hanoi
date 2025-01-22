NUMBER_OF_DISKS = 5

# Initialize the three rods
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Source rod
B = []  # Auxiliary rod
C = []  # Target rod


def move(n, source, auxiliary, target):
    """
    Solves the Tower of Hanoi problem recursively.

    Args:
        n (int): The number of disks to move.
        source (list): The source rod.
        auxiliary (list): The auxiliary rod.
        target (list): The target rod.
    """
    if n <= 0:
        return

    # Move n-1 disks from source to auxiliary
    move(n - 1, source, target, auxiliary)

    # Move the nth disk from source to target
    target.append(source.pop())

    # Display progress
    print(f"Source: {A}, Auxiliary: {B}, Target: {C}\n")

    # Move the n-1 disks from auxiliary to target
    move(n - 1, auxiliary, source, target)


# Start the recursive solution
if __name__ == "__main__":
    print("Initial State:")
    print(f"Source: {A}, Auxiliary: {B}, Target: {C}\n")
    move(NUMBER_OF_DISKS, A, B, C)
