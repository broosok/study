import time
from typing import Annotated
from pydantic import PositiveFloat, Field, EmailStr, validate_call



@validate_call
def send_invoice(
    client_name: Annotated[str, Field(min_length=1)],
    client_email: EmailStr,
    items_purchased: list[str],
    amount_owed: PositiveFloat,
) -> str:
    email_str = f"""
    Dear {client_name}, \n
    Thank you for choosing xyz inc! You
    owe ${amount_owed:,.2f} for the following items: \n
    {items_purchased}
    """
    print(f"Sending email to {client_email}...")
    time.sleep(2)
    return email_str

send_invoice(client_name="dsadsada", client_email="dassdadsa@ss.ru", items_purchased=[], amount_owed=123_000)