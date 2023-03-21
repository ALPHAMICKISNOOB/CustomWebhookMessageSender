from discord_webhook import DiscordWebhook
while True:
    content = input("The message to send from your webhook : ")
    webhook_url = 'Webhook_url'
    #executes the Webhook
    webhook = DiscordWebhook(url=webhook_url, content=content)
    response = webhook.execute()
