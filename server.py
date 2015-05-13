from autobahn.asyncio.websocket import WebSocketServerProtocol

class MyServerProtocol(WebSocketServerProtocol):
	def onMessage(self, payload, isBinary):
		self.sendMessage(payload, isBinary)

if __name__ == '__main__':
	try:
		import asyncio
	except ImportError:
		import trollius as asyncio
	from autobahn.asyncio.websocket import WebSocketServerFactory
	factory = WebSocketServerFactory()
	factory.protocol = MyServerProtocol

	loop = asyncio.get_event_loop()
	coro = loop.create_server(factory, '127.0.0.1', 9000)
	server = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass
	finally:
		server.close()
		loop.close()
