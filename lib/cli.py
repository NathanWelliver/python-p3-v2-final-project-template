from helpers import (
    exit_program,
    buckets,
    display_list_with_index,
    create_bucket,
    delete_bucket,
    update_bucket,
    select_bucket,
    create_item,
    delete_item,
    update_item,
    select_item
)

def main():
    while True:
        main_menu()
        choice = input("Choose an option: ").strip()
        if choice == "0":
            exit_program()
        elif choice == "1":
            manage_buckets_menu()
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    print("\n=== MAIN MENU ===")
    print("1. Manage Buckets")
    print("0. Exit")
    print("=================")

def manage_buckets_menu():
    while True:
        print("\n=== MANAGE BUCKETS ===")
        all_buckets = buckets()
        
        print("\nChoose a bucket by number, or select an option:")
        print("c. Create a new bucket")
        print("0. Back to Main Menu")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "0":
            break
        elif choice.lower() == "c":
            create_bucket()
        else:
            try:
                bucket_index = int(choice) - 1
                if 0 <= bucket_index < len(all_buckets):
                    selected_bucket_menu(all_buckets[bucket_index])
                else:
                    print("Invalid bucket number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number or 'c' to create a bucket.")

def selected_bucket_menu(bucket):
    while True:
        print(f"\n=== BUCKET: {bucket.name} ===")
        select_bucket(bucket)  # Display items in the bucket
        
        print("\nChoose an option:")
        print("c. Add a new item")
        print("u. Update bucket name")
        print("d. Delete this bucket")
        print("m. Manage items")
        print("0. Back to Manage Buckets")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "0":
            break
        elif choice.lower() == "c":
            create_item(bucket)
        elif choice.lower() == "u":
            update_bucket(bucket)
        elif choice.lower() == "d":
            delete_bucket(bucket)
            break
        elif choice.lower() == "m":
            manage_items_menu(bucket)
        else:
            print("Invalid choice. Please try again.")

def manage_items_menu(bucket):
    while True:
        print(f"\n=== ITEMS IN BUCKET: {bucket.name} ===")
        items = bucket.items()
        
        if items:
            display_list_with_index(items)
        else:
            print("This bucket is empty.")
        
        print("\nChoose an option:")
        print("c. Create a new item")
        print("0. Back to Bucket Menu")
        print("Select an item by number")

        choice = input("Choose an option: ").strip()
        
        if choice == "0":
            break
        elif choice.lower() == "c":
            create_item(bucket)
        else:
            try:
                item_index = int(choice) - 1
                if 0 <= item_index < len(items):
                    item_menu(items[item_index], bucket)
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number or '1' to create an item.")

def item_menu(item, bucket):
    while True:
        print(f"\n=== ITEM: {item.title} ===")
        print(f"Bucket: {bucket.name}")
        print(f"Description: {item.description}")
        
        print("\nChoose an option:")
        print("1. Update item")
        print("2. Delete item")
        print("0. Back to Items Menu")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            update_item(item)
        elif choice == "2":
            delete_item(item)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
