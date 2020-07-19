#!/bin/env python
from app import create_app, socketio

main = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(main)
