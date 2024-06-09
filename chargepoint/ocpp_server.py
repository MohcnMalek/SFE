import logging
import asyncio
from websockets import serve
from ocpp.routing import on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call_result
from ocpp.v16 import call

logging.basicConfig(level=logging.INFO)

import requests

class ChargePoint(cp):
    @on('BootNotification')
    async def on_boot_notification(self, charge_point_model, **kwargs):
        # Notify Django server about the BootNotification
        response = requests.post('http://localhost:8000/api/chargepoints/boot_notification/', json={
            'charge_point_model': charge_point_model,
            'charge_point_vendor': kwargs.get('charge_point_vendor')
        })
        return call_result.BootNotification(
            current_time="2023-01-01T00:00:00Z",
            interval=10,
            status="Accepted"
        )

    @on('StatusNotification')
    async def on_status_notification(self, connector_id, status, **kwargs):
        # Notify Django server about the StatusNotification
        response = requests.post('http://localhost:8000/api/chargepoints/status_notification/', json={
            'connector_id': connector_id,
            'status': status
        })
        logging.info(f"Connector {connector_id} is {status}")


async def on_connect(websocket, path):
    """ For every new charge point that connects, create a ChargePoint
    instance and start listening for messages.
    """
    charge_point_id = path.strip('/')
    charge_point = ChargePoint(charge_point_id, websocket)
    await charge_point.start()

async def main():
    server = await serve(on_connect, "0.0.0.0", 9000)
    logging.info("OCPP Server started...")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
