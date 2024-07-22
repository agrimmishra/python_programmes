from collections import defaultdict

def create_calendar():
    """Create an empty calendar."""
    return defaultdict(list)

def add_event(calendar, date, event):
    """Add an event to the calendar for the given date."""
    calendar[date].append(event)

def view_calendar(calendar):
    """View the entire calendar."""
    for date, events in calendar.items():
        print(f"{date}:")
        for event in events:
            print(f"  - {event}")

def main():
    calendar = create_calendar()

    while True:
        print("\nCalendar Menu:")
        print("1. Add Event")
        print("2. View Calendar")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            event = input("Enter event: ")
            add_event(calendar, date, event)
            print("Event added successfully!")

        elif choice == '2':
            print("\nCalendar:")
            view_calendar(calendar)

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
