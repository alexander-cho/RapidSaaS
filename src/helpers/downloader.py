import requests
from pathlib import Path


def download_to_local(
    url: str, 
    out_path: Path, 
    parent_mkdir: bool=True
) -> bool:
    """
    Helper function to download files from the internet into a local location.

    Parameters:
    - url (str): The URL of the file to download.
    - out_path (Path): The local path where the file should be saved.
    - parent_mkdir (bool): If True, create any necessary parent directories if they don't exist.
    
    Returns:
    - bool: True if the download is successful, False otherwise.
    """
    if parent_mkdir:
        # ensure parent dir for out_path exists, if not, create
        out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        # send a get request to the specified url and then check status code
        response = requests.get(url)
        response.raise_for_status()

        # write response content to specified local file
        # in binary to prevent newline conversions/preserve exact bytes
        out_path.write_bytes(response.content)

        # successful download and file write
        return True
    
    except requests.RequestException as e:
        # unsuccessful download
        print(f"Failed to download {url}: {e}")
        return False
    