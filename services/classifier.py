from loguru import logger

class MessageClassifier:
    def __init__(self):
        self.urgent_keywords = ["urgent", "emergency", "immediately", "asap", "critical"]
        self.payment_keywords = ["payment", "invoice", "bill", "charge", "refund"]
        self.technical_keywords = ["bug", "error", "crash", "technical", "issue", "problem"]
        
    def classify_message(self, text):
        text_lower = text.lower()
        
        # Priority detection
        priority = "normal"
        for word in self.urgent_keywords:
            if word in text_lower:
                priority = "urgent"
                break
                
        # Category detection
        category = "question"
        for word in self.payment_keywords:
            if word in text_lower:
                category = "payment"
                break
                
        for word in self.technical_keywords:
            if word in text_lower:
                category = "technical"
                break
                
        logger.info(f"Classified message: category={category}, priority={priority}")
        return category, priority