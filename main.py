from whatsapp import WhatsApp

whatsapp = WhatsApp(
    60,
    login_qr_screenshot="./screenshot.png",
    session_name="tobi",
    headless=True,
    log_chat="Bot Log",
    keep_session_alive=True
)
try:
    print(whatsapp.send_message("Bot Test", "This is a Bot test!"))
    print(whatsapp.send_message("Bot Test", "This is another Bot test!"))
finally:
    whatsapp.quit()
