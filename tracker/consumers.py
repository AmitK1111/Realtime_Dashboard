# tracker/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CryptoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept WebSocket connection
        self.room_name = 'crypto_price'
        self.room_group_name = f'crypto_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        price_data = await self.get_current_prices()  # This function should fetch real-time prices from your API

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'price_data': price_data
        }))

    # Function to fetch current crypto prices
    async def get_current_prices(self):
        # You can fetch live prices using API here
        # Example: Bitcoin and Ethereum prices
        prices = {
            "bitcoin": 96013,
            "ethereum": 1842.24,
        }
        return prices
