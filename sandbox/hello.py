#!/usr/bin/env python3
"""
Simple test script to verify Python environment is working.
"""

def main():
    print("Hello from Python!")
    print(f"Python environment is ready to use.")

    # Test basic Python features
    numbers = [1, 2, 3, 4, 5]
    squared = [n**2 for n in numbers]
    print(f"Squared numbers: {squared}")

if __name__ == "__main__":
    main()
