# lib/helpers.py
from models.bucket import Bucket
from models.item import Item

# Utility function to display a list with numbering
def display_list_with_index(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.name if isinstance(item, Bucket) else item.title}")

def get_item_from_list(items):
    while True:
        try:
            choice = int(input("Select an item by number: "))
            return items[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please select a valid number.")

def exit_program():
    print("Goodbye!")
    exit()

def buckets():
    all_buckets = Bucket.get_all()
    if not all_buckets:
        print("No buckets found.")
    else:
        display_list_with_index(all_buckets)
    return all_buckets

def select_bucket(bucket):
    print(f"\nBucket: {bucket.name}")
    items = bucket.items()
    if items:
        print("Items in this bucket:")
        display_list_with_index(items)
    else:
        print("This bucket is currently empty.")

def bucket_by_name(name):
    bucket = Bucket.find_by_name(name)
    if bucket:
        return bucket
    else:
        print(f"Bucket '{name}' does not exist yet.")

def create_bucket():
    name = input("Enter the bucket's name: ")
    try:
        bucket = Bucket.create(name)
        print(f'Success! {bucket.name} has been created!')
    except Exception as exc:
        print("Error creating bucket: ", exc)

def delete_bucket(bucket):
    confirm = input(f"Are you sure you want to delete the Bucket '{bucket.name}' and all its items? This action cannot be undone. (yes/no): ").lower()
    if confirm == 'yes':
        try:
            items = bucket.items()
            for item in items:
                item.delete()
                print(f"Item '{item.title}' has been deleted.")
            bucket.delete()
            print(f"Bucket '{bucket.name}' has been deleted along with all its items.")
        except Exception as exc:
            print("Error deleting bucket or its items:", exc)
    else:
        print("Deletion canceled.")

def update_bucket(bucket):
    new_name = input(f"Enter the new name for '{bucket.name}': ")
    try:
        bucket.name = new_name
        bucket.update()
        print(f"Bucket renamed to '{bucket.name}'.")
    except Exception as exc:
        print("Error updating bucket:", exc)

def create_item(bucket):
    title = input("Enter the item's title: ")
    description = input("Enter the item's description: ")
    try:
        item = Item.create(title=title, description=description, bucket_id=bucket.id)
        print(f"Success! Item '{item.title}' has been added to Bucket '{bucket.name}'")
    except Exception as exc:
        print("Error creating item: ", exc)

def delete_item(item):
    confirm = input(f"Are you sure you want to delete the Item '{item.title}'? This action cannot be undone. (yes/no): ").lower()
    if confirm == 'yes':
        try:
            item.delete()
            print(f"Item '{item.title}' has been deleted.")
        except Exception as exc:
            print("Error deleting item:", exc)
    else:
        print("Deletion canceled.")

def update_item(item):
    new_title = input(f"Enter the new title for the Item '{item.title}': ")
    new_description = input(f"Enter the new description for Item '{item.title}': ")
    try:
        item.title = new_title
        item.description = new_description
        item.update()
        print(f"Item '{item.title}' has been updated.")
    except Exception as exc:
        print("Error updating item:", exc)

def select_item(bucket):
    items = bucket.items()
    if not items:
        print("No items found in this bucket.")
        return None

    while True:
        display_list_with_index(items)
        try:
            choice = int(input("Select an item by number: "))
            if 1 <= choice <= len(items):
                selected_item = items[choice - 1]  # Adjusting for 0-based index
                print(f'\nItem: {selected_item.title}')
                print(f'Description: {selected_item.description}')
                return selected_item
            else:
                print(f"Please select a number between 1 and {len(items)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")