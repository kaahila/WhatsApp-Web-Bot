from whatsapp import WhatsApp

whatsapp = WhatsApp(
    100,
    loginQrScreenshot="./screenshot.png",
    session="C:\\Users\\therbold\PycharmProjects\Simple-Yet-Hackable-WhatsApp-api\session",
)
print(whatsapp.send_message("Bot Log", "This is a Bot test!"))
whatsapp.quit()
