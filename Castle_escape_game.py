def play_game(current_room):
    """Move between rooms until the player reaches the garden."""
    while True:
        print(f"\n--- You are in the {current_room.upper()} ---")

        if current_room == "hallway":
            print("Two doors lead to the KITCHEN and the GARDEN.")
            choice = input("Where do you go? (kitchen/garden): ").lower().strip()
            if choice in ("kitchen", "garden"):
                current_room = choice
            else:
                print("Invalid choice. You stay in the hallway.")
        elif current_room == "kitchen":
            print("You find a shiny silver key on the counter!")
            input("Press Enter to return to the hallway...")
            current_room = "hallway"
        elif current_room == "garden":
            print("Congratulations! You found the garden and won the game!")
            return
        else:
            return


def main():
    print("Welcome to the Castle Escape Game!")
    try:
        play_game("hallway")
    except (EOFError, KeyboardInterrupt):
        print("\nGame ended.")


if __name__ == "__main__":
    main()
