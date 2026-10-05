from pathlib import Path
import socket, sys
Path("inside.txt").write_text("synthetic sandbox probe")
try:
    Path(sys.argv[1]).write_text("synthetic sandbox probe")
except OSError:
    pass
else:
    raise SystemExit("Outside write was not denied")
try:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
except OSError:
    pass
else:
    raise SystemExit("Network access was not denied")
