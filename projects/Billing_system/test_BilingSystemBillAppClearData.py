# ********RoostGPT********
"""
Test generated by RoostGPT for test ZBIO-5249 using AI Type Claude AI and AI Model claude-3-opus-20240229

ROOST_METHOD_HASH=biling_system_Bill_App_clear_data_039b9b5ff8
ROOST_METHOD_SIG_HASH=biling_system_Bill_App_clear_data_75709990c7

================================VULNERABILITIES================================
Vulnerability: CWE-20: Improper Input Validation
Issue: The code directly uses user-supplied input in the 'messagebox.askyesno()' function without proper validation or sanitization. This could potentially allow an attacker to inject malicious input and manipulate the program's behavior.
Solution: Implement strict input validation and sanitization techniques to ensure that user input conforms to expected formats and does not contain any malicious content. Use secure input handling libraries or built-in functions to validate and clean user input before processing it.

Vulnerability: CWE-798: Use of Hard-coded Credentials
Issue: The code uses hard-coded values for setting various variables, such as 'self.sanitizer.set(0)', 'self.mask.set(0)', etc. If these values are meant to represent some form of credentials or sensitive information, storing them directly in the code poses a security risk. If an attacker gains access to the codebase, they can easily retrieve these hard-coded values.
Solution: Avoid hard-coding sensitive information directly in the code. Instead, use secure methods to store and retrieve such data, such as environment variables, configuration files, or secure key management systems. Ensure that sensitive information is properly encrypted and protected from unauthorized access.

Vulnerability: CWE-330: Use of Insufficiently Random Values
Issue: The code generates a random bill number using 'random.randint(1000, 9999)'. However, the random module in Python is not cryptographically secure and should not be used for generating sensitive or security-critical values. An attacker may be able to predict or guess the generated bill numbers.
Solution: Use a cryptographically secure random number generator, such as the 'secrets' module in Python, for generating sensitive values like bill numbers. The 'secrets' module provides secure random number generation suitable for security-sensitive applications.

================================================================================
Here are the test scenarios for the given clear_data method:

Scenario 1: Clear Data Confirmation
Details:
  TestName: test_clear_data_confirmed
  Description: Verify that when the user confirms the clear operation, all the relevant data fields are reset to their default values.
Execution:
  Arrange: Create an instance of the Bill_App class and set some initial values for the data fields.
  Act: Call the clear_data method and simulate the user confirming the clear operation by returning True from the messagebox.askyesno function.
  Assert: Check that all the data fields (sanitizer, mask, hand_gloves, etc.) are reset to 0, and the price, tax, and customer details fields are reset to empty strings. Verify that a new random bill number is generated.
Validation:
  This test ensures that the clear_data method correctly resets all the relevant data fields when the user confirms the clear operation, which is essential for maintaining data integrity and avoiding any leftover data from previous transactions.

Scenario 2: Clear Data Cancellation
Details:
  TestName: test_clear_data_cancelled
  Description: Verify that when the user cancels the clear operation, no data fields are modified.
Execution:
  Arrange: Create an instance of the Bill_App class and set some initial values for the data fields.
  Act: Call the clear_data method and simulate the user canceling the clear operation by returning False from the messagebox.askyesno function.
  Assert: Check that all the data fields retain their original values and no changes are made.
Validation:
  This test ensures that the clear_data method does not modify any data when the user cancels the clear operation, preventing accidental data loss and maintaining the state of the application.

Scenario 3: Welcome Bill Generation
Details:
  TestName: test_welcome_bill_generation
  Description: Verify that the clear_data method calls the welcome_bill method to generate a new welcome bill after clearing the data.
Execution:
  Arrange: Create an instance of the Bill_App class and set some initial values for the data fields. Mock the welcome_bill method to track if it is called.
  Act: Call the clear_data method and simulate the user confirming the clear operation by returning True from the messagebox.askyesno function.
  Assert: Verify that the welcome_bill method is called once after clearing the data.
Validation:
  This test ensures that the clear_data method correctly generates a new welcome bill after clearing the data, which is important for starting a new transaction and maintaining the proper flow of the billing process.

Scenario 4: Bill Number Generation
Details:
  TestName: test_bill_number_generation
  Description: Verify that a new random bill number is generated within the specified range when the data is cleared.
Execution:
  Arrange: Create an instance of the Bill_App class.
  Act: Call the clear_data method and simulate the user confirming the clear operation by returning True from the messagebox.askyesno function.
  Assert: Check that the bill_no field is set to a string representation of a random integer between 1000 and 9999 (inclusive).
Validation:
  This test ensures that the clear_data method generates a new unique bill number within the specified range, which is crucial for tracking and identifying individual transactions.

These test scenarios cover the main aspects of the clear_data method's business logic, including data clearing, user confirmation, welcome bill generation, and bill number generation. They help ensure the correctness and reliability of the billing system's data management functionality.
"""

# ********RoostGPT********
import pytest
from unittest.mock import patch
import random
# Import the required Tkinter module
import tkinter as tk
from biling_system import Bill_App

class TestBilingSystemBillAppClearData:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Create an instance of the Bill_App class using Tkinter's Tk()
        root = tk.Tk()
        self.bill_app = Bill_App(root)

    def set_initial_values(self):
        self.bill_app.sanitizer.set(10)
        self.bill_app.mask.set(20)
        self.bill_app.hand_gloves.set(30)
        self.bill_app.dettol.set(40)
        self.bill_app.newsprin.set(50)
        self.bill_app.thermal_gun.set(60)
        self.bill_app.rice.set(70)
        self.bill_app.food_oil.set(80)
        self.bill_app.wheat.set(90)
        self.bill_app.daal.set(100)
        self.bill_app.flour.set(110)
        self.bill_app.maggi.set(120)
        self.bill_app.sprite.set(130)
        self.bill_app.limka.set(140)
        self.bill_app.mazza.set(150)
        self.bill_app.coke.set(160)
        self.bill_app.fanta.set(170)
        self.bill_app.mountain_duo.set(180)
        self.bill_app.medical_price.set("10.50")
        self.bill_app.grocery_price.set("20.75")
        self.bill_app.cold_drinks_price.set("30.25")
        self.bill_app.medical_tax.set("2.50")
        self.bill_app.grocery_tax.set("3.75")
        self.bill_app.cold_drinks_tax.set("4.25")
        self.bill_app.c_name.set("John Doe")
        self.bill_app.c_phone.set("1234567890")
        self.bill_app.bill_no.set("5678")
        self.bill_app.search_bill.set("9012")

    @patch("tkinter.messagebox.askyesno")
    def test_clear_data_confirmed(self, mock_askyesno):
        mock_askyesno.return_value = True
        self.set_initial_values()

        with patch.object(self.bill_app, "welcome_bill") as mock_welcome_bill:
            self.bill_app.clear_data()

            assert self.bill_app.sanitizer.get() == 0
            assert self.bill_app.mask.get() == 0
            assert self.bill_app.hand_gloves.get() == 0
            assert self.bill_app.dettol.get() == 0
            assert self.bill_app.newsprin.get() == 0
            assert self.bill_app.thermal_gun.get() == 0
            assert self.bill_app.rice.get() == 0
            assert self.bill_app.food_oil.get() == 0
            assert self.bill_app.wheat.get() == 0
            assert self.bill_app.daal.get() == 0
            assert self.bill_app.flour.get() == 0
            assert self.bill_app.maggi.get() == 0
            assert self.bill_app.sprite.get() == 0
            assert self.bill_app.limka.get() == 0
            assert self.bill_app.mazza.get() == 0
            assert self.bill_app.coke.get() == 0
            assert self.bill_app.fanta.get() == 0
            assert self.bill_app.mountain_duo.get() == 0
            assert self.bill_app.medical_price.get() == ""
            assert self.bill_app.grocery_price.get() == ""
            assert self.bill_app.cold_drinks_price.get() == ""
            assert self.bill_app.medical_tax.get() == ""
            assert self.bill_app.grocery_tax.get() == ""
            assert self.bill_app.cold_drinks_tax.get() == ""
            assert self.bill_app.c_name.get() == ""
            assert self.bill_app.c_phone.get() == ""
            assert self.bill_app.search_bill.get() == ""

            bill_no = self.bill_app.bill_no.get()
            assert bill_no.isdigit()
            assert 1000 <= int(bill_no) <= 9999

            mock_welcome_bill.assert_called_once()

    @patch("tkinter.messagebox.askyesno")
    def test_clear_data_cancelled(self, mock_askyesno):
        mock_askyesno.return_value = False
        self.set_initial_values()

        with patch.object(self.bill_app, "welcome_bill") as mock_welcome_bill:
            self.bill_app.clear_data()

            assert self.bill_app.sanitizer.get() == 10
            assert self.bill_app.mask.get() == 20
            assert self.bill_app.hand_gloves.get() == 30
            assert self.bill_app.dettol.get() == 40
            assert self.bill_app.newsprin.get() == 50
            assert self.bill_app.thermal_gun.get() == 60
            assert self.bill_app.rice.get() == 70
            assert self.bill_app.food_oil.get() == 80
            assert self.bill_app.wheat.get() == 90
            assert self.bill_app.daal.get() == 100
            assert self.bill_app.flour.get() == 110
            assert self.bill_app.maggi.get() == 120
            assert self.bill_app.sprite.get() == 130
            assert self.bill_app.limka.get() == 140
            assert self.bill_app.mazza.get() == 150
            assert self.bill_app.coke.get() == 160
            assert self.bill_app.fanta.get() == 170
            assert self.bill_app.mountain_duo.get() == 180
            assert self.bill_app.medical_price.get() == "10.50"
            assert self.bill_app.grocery_price.get() == "20.75"
            assert self.bill_app.cold_drinks_price.get() == "30.25"
            assert self.bill_app.medical_tax.get() == "2.50"
            assert self.bill_app.grocery_tax.get() == "3.75"
            assert self.bill_app.cold_drinks_tax.get() == "4.25"
            assert self.bill_app.c_name.get() == "John Doe"
            assert self.bill_app.c_phone.get() == "1234567890"
            assert self.bill_app.bill_no.get() == "5678"
            assert self.bill_app.search_bill.get() == "9012"

            mock_welcome_bill.assert_not_called()

    @patch("tkinter.messagebox.askyesno")
    def test_welcome_bill_generation(self, mock_askyesno):
        mock_askyesno.return_value = True

        with patch.object(self.bill_app, "welcome_bill") as mock_welcome_bill:
            self.bill_app.clear_data()
            mock_welcome_bill.assert_called_once()

    @patch("tkinter.messagebox.askyesno")
    def test_bill_number_generation(self, mock_askyesno):
        mock_askyesno.return_value = True

        self.bill_app.clear_data()

        bill_no = self.bill_app.bill_no.get()
        assert bill_no.isdigit()
        assert 1000 <= int(bill_no) <= 9999


class Bill_App:
    def __init__(self, root):
        # Initialize the Bill_App class with a Tkinter root window
        self.root = root
        self.sanitizer = tk.StringVar()
        self.mask = tk.StringVar()
        self.hand_gloves = tk.StringVar()
        self.dettol = tk.StringVar()
        self.newsprin = tk.StringVar()
        self.thermal_gun = tk.StringVar()
        self.rice = tk.StringVar()
        self.food_oil = tk.StringVar()
        self.wheat = tk.StringVar()
        self.daal = tk.StringVar()
        self.flour = tk.StringVar()
        self.maggi = tk.StringVar()
        self.sprite = tk.StringVar()
        self.limka = tk.StringVar()
        self.mazza = tk.StringVar()
        self.coke = tk.StringVar()
        self.fanta = tk.StringVar()
        self.mountain_duo = tk.StringVar()
        self.medical_price = tk.StringVar()
        self.grocery_price = tk.StringVar()
        self.cold_drinks_price = tk.StringVar()
        self.medical_tax = tk.StringVar()
        self.grocery_tax = tk.StringVar()
        self.cold_drinks_tax = tk.StringVar()
        self.c_name = tk.StringVar()
        self.c_phone = tk.StringVar()
        self.bill_no = tk.StringVar()
        self.search_bill = tk.StringVar()
        self.txtarea = tk.Text(self.root)

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you want to Clear Data?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.newsprin.set(0)
            self.thermal_gun.set(0)
            # ===============Grocery==============
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)
            # ============Cold Drinks=============
            self.sprite.set(0)
            self.limka.set(0)
            self.mazza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_duo.set(0)
            # ====================Total Product Price & Tax variables===============
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            # =======Cutomers===========
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")

            self.welcome_bill()

    def welcome_bill(self):
        self.txtarea.delete('1.0', tk.END)
        self.txtarea.insert(tk.END, "\tWelcome Webcode Retail")
        self.txtarea.insert(tk.END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(tk.END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(tk.END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(tk.END, f"\n================================")
        self.txtarea.insert(tk.END, f"\nProducts\t\tQTY\t\tPrice")