FoodDeliverySystem/
├── main.py                     # Entry point for the application
├── data/
│   ├── users.json              # JSON file to store user data
│   ├── orders.json             # JSON file to store order data
│   └── restaurants.json        # JSON file to store restaurant data
├── src/
│   ├── __init__.py             # Package initializer
│   ├── gui.py                  # Main GUI interface (user and admin views)
│   ├── admin_gui.py            # Separate GUI components for admin interface
│   ├── models/
│   │   ├── __init__.py         # Package initializer
│   │   ├── user.py             # User and Admin classes
│   │   ├── restaurant.py       # Restaurant-related classes and methods
│   │   ├── order.py            # Order and ScheduledOrder classes
│   │   └── payment.py          # Payment classes and methods
│   └── utils.py                # Utility functions for JSON data handling
└── tests/
    ├── test_user.py            # Unit tests for User class
    ├── test_order.py           # Unit tests for Order class
    └── test_payment.py         # Unit tests for Payment processing
