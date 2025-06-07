from models.ticket_model import Session, Ticket
from loguru import logger

class DatabaseService:
    def __init__(self):
        self.session = Session()
        
    def create_ticket(self, user_id, username, message, category, priority, response=None):
        try:
            ticket = Ticket(
                user_id=user_id,
                username=username,
                message=message,
                category=category,
                priority=priority,
                response=response
            )
            self.session.add(ticket)
            self.session.commit()
            logger.success(f"Ticket created for user {username}")
            return ticket
        except Exception as e:
            self.session.rollback()
            logger.error(f"Failed to create ticket: {e}")
            raise
            
    def get_pending_tickets(self):
        try:
            return self.session.query(Ticket).filter_by(resolved=False).all()
        except Exception as e:
            logger.error(f"Failed to fetch pending tickets: {e}")
            raise
            
    def close_ticket(self, ticket_id):
        try:
            ticket = self.session.query(Ticket).filter_by(id=ticket_id).first()
            if ticket:
                ticket.resolved = True
                self.session.commit()
                logger.success(f"Ticket {ticket_id} closed")
                return True
            return False
        except Exception as e:
            self.session.rollback()
            logger.error(f"Failed to close ticket {ticket_id}: {e}")
            raise