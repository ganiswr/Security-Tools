# import semua fitur dari file lain
import subprocess
from socket import *
import time
import phonenumbers
from test import number
from phonenumbers import geocoder, carrier

# Fitur 1: Port Scanner
def port_scanner():
    starttime = time.time()
    target = input('Enter host for scanning: ')
    t_IP = gethostbyname(target)
    print('Starting scanning on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('port %d: OPEN' % (i,))
        s.close()
    print("Time taken:", time.time() - starttime)

# Fitur 2: Track Phone Number
def track_phonenumber():
    ch_number = phonenumbers.parse(number, "CH")
    print("Country:", geocoder.description_for_number(ch_number, "en"))

    service_number = phonenumbers.parse(number, "RO")
    print("Carrier:", carrier.name_for_number(service_number, "en"))

# Fitur 3: Find Available WiFi
def check_wifi():
    nw = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    decoded_nw = nw.decode('ascii')
    print(decoded_nw)
    input("Press Enter to return to the menu...")

# Menu
def menu():

    while True:
        print("\nSELAMAT DATANG DI TOSDO")
        print("\nCyber Security Tool Menu:")
        print("1. Port Scanner")
        print("2. Track Phone Number")
        print("3. Find Available WiFi")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            port_scanner()
        elif choice == '2':
            track_phonenumber()
        elif choice == '3':
            check_wifi()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
