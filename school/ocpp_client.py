import asyncio
import websockets
import json

async def connect_to_ocpp_server():
    uri = "ws://ocpp-server-address:9000"  # Replace with your OCPP server address and port
    
    async with websockets.connect(uri) as websocket:
        # Send a message to the server (e.g., request for charging session data)
        request_message = {
            "action": "get_charging_sessions"
        }
        await websocket.send(json.dumps(request_message))
        
        # Receive response from the server
        response = await websocket.recv()
        response_data = json.loads(response)
        
        return response_data

# Example usage
async def main():
    data = await connect_to_ocpp_server()
    print("Received data from OCPP server:", data)

if __name__ == "__main__":
    asyncio.run(main())
