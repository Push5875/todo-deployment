#!/bin/bash

# Define directories
DIR1="./frontend"
DIR2="./backend"

# Define PID file
PID_FILE="/tmp/server_pids"

start_servers() {
  echo "Starting servers..."
  wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem
  # Start the HTTP server in the first directory
  echo "Starting HTTP server in $DIR1"
  (
    cd "$DIR1" || exit
    python -m http.server 8080 &
    echo $! >> "$PID_FILE"
    echo "HTTP server started on port 8080 with PID $!"
  )

  # Start the Uvicorn server in the second directory
  echo "Starting Uvicorn server in $DIR2"
  (
    cd "$DIR2" || exit
    uvicorn app:app --host 0.0.0.0 --port 8000 &
    echo $! >> "$PID_FILE"
    echo "Uvicorn server started on port 8000 with PID $!"
  )
}

stop_servers() {
  echo "Stopping servers..."

  if [ -f "$PID_FILE" ]; then
    while IFS= read -r pid; do
      if kill "$pid" > /dev/null 2>&1; then
        echo "Stopped process with PID $pid"
      else
        echo "Failed to stop process with PID $pid or process not running"
      fi
    done < "$PID_FILE"
    rm -f "$PID_FILE"
  else
    echo "No servers are running (PID file not found)"
  fi
}

case "$1" in
  start)
    start_servers
    ;;
  stop)
    stop_servers
    ;;
  restart)
    stop_servers
    start_servers
    ;;
  *)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
    ;;
esac
