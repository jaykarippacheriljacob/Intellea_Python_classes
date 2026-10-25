""" 
    Notification Types
    Easy
    Inheritance and Method Overriding
    Implement the Notification classes.

    Notification(message) stores the message.
    send() returns Notification: <message>.
    info() returns Message length: <length>.
    EmailNotification and SmsNotification inherit from Notification and only override send() to return Email: <message> and SMS: <message>.
    The function send_all is already written. It uses your classes.

    Parameters

    items: list of (kind, message) pairs; kind is email, sms or anything else
    Returns

    A list of strings: for each item, the result of send() and then the result of info(). email makes an EmailNotification, sms an SmsNotification, anything else a plain Notification.

    Examples

    Arguments: [('email', 'Welcome to Intellea'), ('sms', 'OTP 4821'), ('push', 'Hi')]
    Returns: ['Email: Welcome to Intellea', 'Message length: 19', 'SMS: OTP 4821', 'Message length: 8', 'Notification: Hi', 'Message length: 2']
    Explanation: push is neither email nor sms, so it is a plain Notification. All three use the inherited info().
    Constraints

    1 <= number of items <= 20
    Each message has 1 to 100 characters and may contain spaces and symbols
    The kind is compared exactly, so only email and sms in small letters pick a child class
    Use inheritance. Do not copy __init__ or info() into the child classes
 """

class Notification:
    def __init__(self, message):
        # Store the message text in this object
        self.message = message

    def send(self):
        # Default send for a general notification
        return "Notification: " + self.message

    def info(self):
        # Shared by all notification types; child classes inherit it unchanged
        return "Message length: " + str(len(self.message))


class EmailNotification(Notification):
    def send(self):
        # Overrides the parent's send() with an Email prefix
        return "Email: " + self.message


class SmsNotification(Notification):
    def send(self):
        # Overrides the parent's send() with an SMS prefix
        return "SMS: " + self.message


# Do not change the code below
def send_all(items):
    lines = []
    for kind, message in items:
        if kind == "email":
            item = EmailNotification(message)
        elif kind == "sms":
            item = SmsNotification(message)
        else:
            item = Notification(message)
        lines.append(item.send())
        lines.append(item.info())
    return lines


# Test cases
print(send_all([("email", "Hello"), ("sms", "Hi there"), ("push", "Update")]))
# Output: ['Email: Hello', 'Message length: 5', 'SMS: Hi there', 'Message length: 8',
#          'Notification: Update', 'Message length: 6']
print(send_all([("sms", "")]))
# Output: ['SMS: ', 'Message length: 0']   (empty message)
print(send_all([("Email", "Test")]))
# Output: ['Notification: Test', 'Message length: 4']   ("Email" ≠ "email", so it falls back to the parent)
print(send_all([]))
# Output: []

