def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Example usage
if __name__ == "__main__":
    num_disks = 3  # You can change this number
    print(f"Steps to solve Tower of Hanoi with {num_disks} disks:\n")
    tower_of_hanoi(num_disks, "A", "B", "C")
