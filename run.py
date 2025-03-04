import argparse
import logging
from recoverpy.log.logger import log  # ✅ Ensure this works
from recoverpy.ui.app import RecoverpyApp
from datetime import datetime
from os import path
from tempfile import gettempdir


def _set_logger() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Enable logging")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_file_path = path.join(gettempdir(), f"recoverpy-{timestamp}.log")

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.CRITICAL,
        format="%(asctime)s - %(levelname)s - [%(threadName)s] - %(message)s",
        handlers=[logging.FileHandler(log_file_path)] if args.debug else [logging.NullHandler()],
    )

    log.setLevel(logging.DEBUG if args.debug else logging.CRITICAL)
    log.info(f"Logging initialized. Log file: {log_file_path}")


def main() -> None:
    print("Starting application...")  # ✅ Print before initialization
    _set_logger()
    log.info("Starting Recoverpy app")

    print("RecoverpyApp imported successfully!")
    app = RecoverpyApp()
    print("App instance created.")

    app.run()
    print("Application is running!")


if __name__ == "__main__":
    main()
