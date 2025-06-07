from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters
)
from services.classifier import MessageClassifier
from services.gpt_client import GPTClient
from services.db_service import DatabaseService
from config import OFFLINE_WEEK_END_DATE, SUPPORT_EMAIL
from loguru import logger
import os

class TelegramHandler:
    def __init__(self):
        self.classifier = MessageClassifier()
        self.gpt_client = GPTClient()
        self.db_service = DatabaseService()
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_message = (
            "🦖 *Welcome to Dino Support!* 🦖\n\n"
            "I'm here to help with your questions during our offline week. "
            "Just send me your message and I'll do my best to assist!\n\n"
            f"*Note:* Our team is offline until {OFFLINE_WEEK_END_DATE}. "
            "Urgent matters will be prioritized when we return."
        )
        
        await update.message.reply_text(
            welcome_message,
            parse_mode="Markdown"
        )
        
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.message.from_user
        message_text = update.message.text
        
        logger.info(f"New message from {user.username}: {message_text}")
        
        # Classify the message
        category, priority = self.classifier.classify_message(message_text)
        
        # Generate response based on priority
        if priority == "normal":
            # Try to answer with GPT
            response = self.gpt_client.generate_response(message_text)
            
            if response:
                await update.message.reply_text(
                    response,
                    parse_mode="Markdown"
                )
                # Store as resolved
                self.db_service.create_ticket(
                    user_id=user.id,
                    username=user.username,
                    message=message_text,
                    category=category,
                    priority=priority,
                    response=response
                )
                return
                
        # For urgent or if GPT couldn't answer
        response = (
            f"Hi {user.first_name} 👋,\n\n"
            f"Dino received your *{category}* message and classified it as *{priority}* priority. "
            f"A team member will review it after {OFFLINE_WEEK_END_DATE}.\n\n"
            f"For urgent matters, you can email us at {SUPPORT_EMAIL}."
        )
        
        await update.message.reply_text(
            response,
            parse_mode="Markdown"
        )
        
        # Store as unresolved
        self.db_service.create_ticket(
            user_id=user.id,
            username=user.username,
            message=message_text,
            category=category,
            priority=priority
        )
        
    def run(self):
        from config import TELEGRAM_TOKEN
        
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
        
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        logger.info("Starting Telegram bot...")
        application.run_polling()