import requests

# USSD Application for GreenBin

def start_ussd_session():
    display_menu()

def select_ecogreen_tune():
    tunes = {
        "1": "EcoGreen Tune 1 - Nature's Call",
        "2": "EcoGreen Tune 2 - Save the Planet",
        "3": "EcoGreen Tune 3 - Green Future",
        "4": "EcoGreen Tune 4 - Love Nature",
        "5": "EcoGreen Tune 5 - Go Green",
    }

    print("Select an EcoGreen Skiza Tune:")
    for key, value in tunes.items():
        print(f"{key}. {value}")

    choice = get_user_input("Enter the number of your choice: ")
    
    if choice in tunes:
        set_skiza_tune(tunes[choice])
    else:
        print("Invalid choice. Please try again.")
        select_ecogreen_tune()

def set_skiza_tune(tune):
    # Logic to set the Skiza tune for the user
    response = call_api('POST', '/api/skiza/set', {'tune': tune})
    print(response.get('message', 'Failed to set Skiza tune.'))

def display_menu():
    print("Welcome to GreenBin - Nature Diversity")
    print("1. Register Business/School/Organization")
    print("2. Buy Goods")
    print("3. Donate Points")
    print("4. Pay for WiFi")
    print("5. Pay Transport")
    print("6. Transfer GCPs")
    print("7. Check GCPs Balance")
    print("8. Voice Mall Services")
    print("9. Apply for GreenBank Card")
    print("10. Report Fraud")
    print("11. Withdraw/Deposit Points")
    print("0. Exit")
    
    choice = get_user_input("Select an option: ")
    navigate_choice(choice)

def navigate_choice(choice):
    if choice == "1":
        register_business()
    elif choice == "2":
        buy_goods()
    elif choice == "3":
        donate_points()
    elif choice == "4":
        pay_wifi()
    elif choice == "5":
        pay_transport()
    elif choice == "6":
        transfer_gcps()
    elif choice == "7":
        check_gcps_balance()
    elif choice == "8":
        select_ecogreen_tune()
    elif choice == "9":
        apply_greenbank_card()
    elif choice == "10":
        report_fraud()
    elif choice == "11":
        withdraw_deposit_points()
    elif choice == "0":
        exit_application()
    else:
        print("Invalid choice. Please try again.")
        display_menu()

def register_business():
    business_name = get_user_input("Enter business name: ")
    national_card = get_user_input("Enter your ID Number: ")
    phone_number = get_user_input("Enter phone number: ")
    license_number = get_user_input("Enter License number: ")
    response = call_api('POST', '/api/business/register', {'name': business_name, 'phoneNumber': phone_number, 'national_card': national_card, 'license_number': license_number})
    print(response.get('message', 'Registration failed.'))

def buy_goods():
    code = get_user_input("Enter shop/supermarket code: ")
    response = call_api('POST', '/api/goods/buy', {'code': code})
    print(response.get('message', 'Purchase failed.'))

def donate_points():
    points = get_user_input("Enter points to donate: ")
    choose_disaster = get_user_input("choose disaster: ")  # list disasters options to choose from
    response = call_api('POST', '/api/donations', {'points': points})
    print(response.get('message', 'Donation failed.'))

def pay_wifi():
    wifi_code = get_user_input("Enter WiFi code: ")
    plan = get_user_input("Choose plan: ")
    response = call_api('POST', '/api/wifi/pay', {'wifiCode': wifi_code, 'plan': plan})
    print(response.get('message', 'Payment failed.'))

def pay_transport():
    bus_code = get_user_input("Enter bus code: ")
    amount = get_user_input("Enter amount: ")
    response = call_api('POST', '/api/transport/pay', {'busCode': bus_code, 'amount': amount})
    print(response.get('message', 'Payment failed.'))

def transfer_gcps():
    method = get_user_input("Select transfer method (Bank, M-Pesa, Airtel Money, Bitcoin): ")
    response = call_api('POST', '/api/gcps/transfer', {'method': method})
    print(response.get('message', 'Transfer failed.'))

def check_gcps_balance():
    response = call_api('GET', '/api/gcps/balance')
    print(f"Your GCPs balance is: {response.get('balance', 'Unable to retrieve balance.')}")

def voice_mall_services():
    response = call_api('GET', '/api/voice-services')
    print(response.get('message', 'Unable to retrieve services.'))

def apply_greenbank_card():
    fullnames = get_user_input("Enter full names: ")
    id_number = get_user_input("Enter ID number: ")
    bank_account_number = get_user_input("Enter Green Bank account number: ")
    response = call_api('POST', '/api/greenbank/apply', {'fullNames': fullnames, 'idNumber': id_number, 'bankAccountNumber': bank_account_number})
    print(response.get('message', 'Application failed.'))

def report_fraud():
    details = get_user_input("Enter fraud details: ")
    response = call_api('POST', '/api/fraud/report', {'details': details})
    print(response.get('message', 'Reporting failed.'))

def withdraw_points():
    method = get_user_input("Select method (GreenBank, GCP wallet  ): ") # options 1 and 2
    amount = get_user_input("Enter amount: ")
    response = call_api('POST', '/api/points/transaction', {'method': method, 'amount': amount})
    print(response.get('message', 'Transaction failed.'))

def deposit_points():
    method = get_user_input("Select method (M-Pesa, AirtelMoney): ") # options 1 and 2
    amount = get_user_input("Enter amount: ")
    response = call_api('POST', '/api/points/transaction', {'method': method, 'amount': amount})
    print(response.get('message', 'Transaction failed.'))

def exit_application():
    print("Thank you for using GreenBin. Earn more GCPs!")

def get_user_input(prompt):
    return input(prompt)  # Replace with the appropriate method for USSD input

def call_api(method, endpoint, data=None):
    url = f"http://your-api-url.com{endpoint}"  # Replace with your actual API URL
    try:
        if method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'GET':
            response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {}

# Start the USSD session
start_ussd_session()
