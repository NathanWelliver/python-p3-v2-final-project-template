# Phase 3 Project

## Overview

The Bucket List  CLI is a command-line interface application that allows users to manage buckets and items within those buckets. Users can create, read, update, and delete both buckets and items, as well as navigate through them using a user-friendly CLI. This README provides an overview of the project's structure, key files, and functions.

## CLI Script

### `cli.py`

The `cli.py` script is the main entry point for the CLI application. It contains the primary loop that presents the user with menus and handles their input to perform various actions within the application.

- **`main()`**: The main function that initiates the CLI and presents the user with the main menu. It handles user input to navigate to different sections of the application.
- **`main_menu()`**: Displays the main menu with options to manage buckets or exit the program.
- **`manage_buckets_menu()`**: Allows the user to manage buckets by listing them, creating new ones, or navigating to specific buckets.
- **`selected_bucket_menu(bucket)`**: Provides options to manage a selected bucket, including creating items, updating the bucket name, deleting the bucket, or managing items within the bucket.
- **`manage_items_menu(bucket)`**: Allows the user to manage items within a selected bucket, including creating new items or selecting existing ones to update or delete.
- **`item_menu(item, bucket)`**: Provides options to manage a selected item, including updating its details or deleting it.

## Helper Functions

### `helpers.py`

The `helpers.py` file contains utility functions to support the CLI application, including displaying lists, handling user input, and interacting with buckets and items.

- **`display_list_with_index(items)`**: Displays a list of items with numerical indices, making it easier for users to select an item by number.
- **`get_item_from_list(items)`**: Prompts the user to select an item from a list by number and returns the selected item.
- **`exit_program()`**: Prints a goodbye message and exits the program.
- **`buckets()`**: Retrieves and displays all buckets from the database.
- **`select_bucket(bucket)`**: Displays the items within a selected bucket.
- **`bucket_by_name(name)`**: Finds and returns a bucket by its name.
- **`create_bucket()`**: Prompts the user to enter a name for a new bucket and creates it in the database.
- **`delete_bucket(bucket)`**: Deletes a specified bucket and all items associated with it after user confirmation.
- **`update_bucket(bucket)`**: Updates the name of a specified bucket.
- **`create_item(bucket)`**: Prompts the user to enter details for a new item and adds it to a specified bucket.
- **`delete_item(item)`**: Deletes a specified item after user confirmation.
- **`update_item(item)`**: Updates the details of a specified item.
- **`select_item(bucket)`**: Allows the user to select an item from a bucket and displays its details.

## Models

### `bucket.py`

The `bucket.py` file defines the `Bucket` class, which represents a bucket in the database.

- **`__init__(self, name, id=None)`**: Initializes a new bucket instance with a name and an optional ID.
- **`create_table(cls)`**: Creates the `buckets` table in the database if it does not already exist.
- **`drop_table(cls)`**: Drops the `buckets` table from the database.
- **`save(self)`**: Saves the bucket instance to the database.
- **`update(self)`**: Updates the bucket's name in the database.
- **`delete(self)`**: Deletes the bucket from the database.
- **`instance_from_db(cls, row)`**: Creates a bucket instance from a database row.
- **`get_all(cls)`**: Retrieves all buckets from the database.
- **`find_by_id(cls, id)`**: Finds a bucket by its ID.
- **`find_by_name(cls, name)`**: Finds a bucket by its name.
- **`items(self)`**: Retrieves all items associated with this bucket.

### `item.py`

The `item.py` file defines the `Item` class, which represents an item in the database.

- **`__init__(self, title, description, bucket_id, id=None)`**: Initializes a new item instance with a title, description, bucket ID, and an optional ID.
- **`create_table(cls)`**: Creates the `items` table in the database if it does not already exist.
- **`drop_table(cls)`**: Drops the `items` table from the database.
- **`save(self)`**: Saves the item instance to the database.
- **`update(self)`**: Updates the item’s details in the database.
- **`delete(self)`**: Deletes the item from the database.
- **`instance_from_db(cls, row)`**: Creates an item instance from a database row.
- **`get_all(cls)`**: Retrieves all items from the database.
- **`find_by_id(cls, id)`**: Finds an item by its ID.
- **`find_by_title(cls, title)`**: Finds an item by its title.

## Getting Started

1. **Setup**: Ensure you have Python and the required dependencies installed. Use `pipenv` to install dependencies listed in the `Pipfile`.
2. **Database Initialization**: Run the `create_table` methods in `bucket.py` and `item.py` to initialize the database schema.
3. **Running the CLI**: Execute the `cli.py` script to start the CLI application and follow the prompts to manage buckets and items.

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Pipenv Documentation](https://pipenv.pypa.io/en/latest/)

