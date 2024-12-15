from src.decorator.colorize_message import colorize_message  
from src.decorator.input_error import input_error
from src.constants import messages_error, messages
from src.classes import AddressBook, Record

@colorize_message
@input_error
def add_contact(args, contacts):
    """Додає контакт у словник."""
    if len(args) != 2:
        return messages_error["usage_add"]
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return messages["add_contact"]

@colorize_message
@input_error
def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) != 2:
        return messages_error["usage_change"]
    name, new_phone = args
    contact = contacts.find(name)
    if contact:
        contact.edit_phone(contact.phones[0].value, new_phone)
        return messages["change_contact"]
    return messages_error["not_found"]

@colorize_message
@input_error
def show_phone(args, contacts):
    """Повертає номер телефону за іменем."""
    if len(args) != 1:
        return messages_error["usage_phone"]
    name = args[0]
    contact = contacts.find(name)
    if contact:
        return contact.phones[0].value
    return messages_error["not_found"]

@colorize_message
@input_error
def show_all(contacts):
    """Показує всі контакти."""
    if not contacts:
        return messages_error["no_contacts"]
    return "\n".join(str(record) for record in contacts.data.values())

@colorize_message
def start_bot():
    return messages["start_message"]

@colorize_message
def exit_bot():
    return messages["exit_bot"]
