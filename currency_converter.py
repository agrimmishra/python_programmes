def to_USA_dollar(currency):
    """
    Converts an amount from Indian Rupees (INR) to US Dollars (USD).

    Parameters:
    currency (float): The amount in Indian Rupees to be converted.

    Returns:
    float: The equivalent amount in US Dollars.
    """
    return currency * 0.012

def to_EURO(currency):
    """
    Converts an amount from Indian Rupees (INR) to Euros (EUR).

    Parameters:
    currency (float): The amount in Indian Rupees to be converted.

    Returns:
    float: The equivalent amount in Euros.
    """
    return currency * 0.011

def to_YUAN(currency):
    """
    Converts an amount from Indian Rupees (INR) to Chinese Yuan (CNY).

    Parameters:
    currency (float): The amount in Indian Rupees to be converted.

    Returns:
    float: The equivalent amount in Chinese Yuan.
    """
    return currency * 0.087

def main():
    """
    Main function to execute currency conversion.
    """
    try:
        # Input amount in Indian Rupees
        currency = float(input("Enter Indian currency (INR): "))

        # Validate input
        if currency < 0:
            print("Amount cannot be negative.")
            return

        # Perform conversions
        usd = to_USA_dollar(currency)
        eur = to_EURO(currency)
        yuan = to_YUAN(currency)

        # Print results
        print(f"{currency:.2f} INR is {usd:.2f} USD")
        print(f"{currency:.2f} INR is {eur:.2f} EUR")
        print(f"{currency:.2f} INR is {yuan:.2f} CNY")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
