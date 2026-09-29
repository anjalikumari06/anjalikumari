"""
FitBuddy - Application Launcher
Runs the FastAPI Uvicorn ASGI server with live reloading.
Automatically checks for port availability to prevent conflicts with other services.
"""
import socket
import uvicorn


def find_available_port(start_port: int = 8000) -> int:
    """Finds an available port starting from start_port."""
    for port in range(start_port, start_port + 10):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    return start_port


if __name__ == "__main__":
    port = find_available_port(8000)

    print("\n" + "=" * 65)
    print("  🏋️‍♂️  FitBuddy – AI Fitness Plan Generator")
    print("  Powered by FastAPI & Google Gemini Models")
    print("=" * 65)
    if port != 8000:
        print(f"  ⚠️  Notice: Port 8000 is occupied by another app.")
        print(f"  🚀  FitBuddy started automatically on Port {port}!")
    print(f"  • Web Application:  http://127.0.0.1:{port}")
    print(f"  • Admin Dashboard:  http://127.0.0.1:{port}/view-all-users")
    print(f"  • API Swagger Docs: http://127.0.0.1:{port}/docs")
    print("=" * 65 + "\n")

    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)
