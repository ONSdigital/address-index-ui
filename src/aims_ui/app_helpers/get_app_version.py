import logging
import os


def get_app_version() -> str:
  """
    Get the application version from version.txt file.

    Returns:
        str: Application version string, or "Unknown" if reading fails.
    """
  version_path = os.path.abspath(
      os.path.join(os.path.dirname(__file__), '..', '..', '..', 'version.txt'))

  try:
    with open(version_path, 'r', encoding='utf-8') as version_file:
      return version_file.read().strip()
  except FileNotFoundError:
    logging.error(f'version.txt not found at {version_path}')
  except PermissionError:
    logging.error(f'Permission denied when accessing {version_path}')
  except Exception as e:
    logging.exception(
        f'Unexpected error while reading version from {version_path}: {e}')

  # If any error occurs, return "Unknown"
  return 'Unknown'
