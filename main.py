
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# שאלות פתיחה
opening_questions = [
    "מה הדבר הראשון שקרה היום שהשפיע על המצב שלך, גם אם לרגע?",
    "על מה לא רצית לחשוב היום… אבל זה בכל זאת היה שם?",
    "אם היית יכול לשנות משהו קטן ביום הזה – מה זה היה?",
    "מה למדת על עצמך מאז אתמול, אפילו אם זה משהו ממש קטן?",
    "מה הרגשת כשקמת – ומה הרגשת באמת, לפני שהתחלת לתפקד?",
    "מה אתה לא מרשה לעצמך להרגיש עכשיו?",
    "אם הייתי רואה אותך מבחוץ – מה הייתי מפספס בך היום?",
    "מה אתה צריך לשחרר כדי להיות קצת יותר אתה היום?",
    "מתי היום הרגשת שניתקת מעצמך? ומה גרם לזה?",
    "איזו מחשבה היום גרמה לך לעצור – אפילו לשנייה? מה היה בה?"
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = random.choice(opening_questions)
    await update.message.reply_text(f"נעים לראות אותך.\n\n{question}")

if __name__ == "__main__":
    import os
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
