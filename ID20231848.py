class Ticket:
    ticket_counter = 2000

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.ticket_counter
        Ticket.ticket_counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.generate_password()
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"

    def reopen(self):
        if self.status == "Closed":
            self.status = "Reopened"

    def display(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}")

    def generate_password(self):
        # Reset password logic based on staff ID and creator name
        new_password = self.staff_id[:2] + self.creator_name[:3]
        return new_password


class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def submit_ticket(self, staff_id, creator_name, contact_email, description):
        ticket = Ticket(staff_id, creator_name, contact_email, description)
        self.tickets.append(ticket)

    def resolve_tickets(self):
        for ticket in self.tickets:
            ticket.resolve_password_change()

    def reopen_tickets(self):
        for ticket in self.tickets:
            ticket.reopen()

    def display_tickets(self):
        for ticket in self.tickets:
            ticket.display()

    def display_ticket_stats(self):
        tickets_created = len(self.tickets)
        tickets_resolved = sum(1 for ticket in self.tickets if ticket.status == "Closed")
        tickets_to_solve = sum(1 for ticket in self.tickets if ticket.status == "Open")

        print("\nDisplaying Ticket Statistics")
        print(f"Tickets Created: {tickets_created}")
        print(f"Tickets Resolved: {tickets_resolved}")
        print(f"Tickets To Solve: {tickets_to_solve}")


def main():
    ticketing_system = TicketingSystem()

    # Submit some tickets
    ticketing_system.submit_ticket("INNAM", "Inna", "inna@example.com", "My monitor stopped working")
    ticketing_system.submit_ticket("MARIAH", "Maria", "maria@example.com", "Request for a videocamera to conduct webinars")
    ticketing_system.submit_ticket("JOHNS", "John", "john@example.com", "Password Change")

    # Resolve some tickets
    ticketing_system.resolve_tickets()

    # Print ticket information
    print("\nPrinting Tickets:")
    ticketing_system.display_tickets()

    # Display ticket statistics
    ticketing_system.display_ticket_stats()

    # Reopen some resolved tickets
    ticketing_system.reopen_tickets()

    # Display ticket information and statistics again
    print("\nPrinting Tickets After Reopening:")
    ticketing_system.display_tickets()
    ticketing_system.display_ticket_stats()


if __name__ == "__main__":
    main()