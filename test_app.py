from coreapi import CoreAPI
from coreapi import Request
from coreapi import JSONResponse
from coreapi import WebSocketConnection

app = CoreAPI()

@app.route(
    "/{hello}",
    methods=["GET", "POST"]
)
def hello_world(request: Request):
    hello = request.slugs["hello"]
    if request.method == "GET":
        return JSONResponse(data={"Hello": hello}, status=200)
    elif request.method == "POST":
        return JSONResponse(data={"Hello": hello}, status=201)


@app.ws("/ws")
async def foo(connection: WebSocketConnection):
    await connection.accept()
    while True:
        message = await connection.receive_message()
        if message == "close":
            await connection.close()
            return
        await connection.send_message(str(message))