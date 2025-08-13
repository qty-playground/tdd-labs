"""Command line interface for TDD Labs."""

import argparse
import sys
import uvicorn


def run_server(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """Run the FastAPI server."""
    print(f"Starting TDD Labs API server on {host}:{port}")
    uvicorn.run(
        "tdd_labs.main:app",
        host=host,
        port=port,
        reload=reload
    )


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="TDD Labs CLI")
    parser.add_argument("--version", action="version", version="%(prog)s 0.1.0")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Server command
    server_parser = subparsers.add_parser("server", help="Run the FastAPI server")
    server_parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    server_parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    server_parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    
    args = parser.parse_args()
    
    if args.command == "server":
        run_server(host=args.host, port=args.port, reload=args.reload)
    else:
        print("TDD Labs - Welcome to Test-Driven Development!")
        print("Use 'tdd-labs server' to start the API server")
        print("Use 'tdd-labs --help' for more options")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())