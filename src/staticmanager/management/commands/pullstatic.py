import helpers

from typing import Any

from django.core.management.base import BaseCommand
from django.conf import settings


# directory where vendor static files will be saved, as specified in settings
STATICFILES_VENDOR_DIRS = getattr(settings, 'STATICFILES_VENDOR_DIR')

# map static file names to external URL
VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js",
    "flowbite.min.js.map": "https://cdn.jsdelivr.net/npm/flowbite@2.5.1/dist/flowbite.min.js",
}


class Command(BaseCommand):
    """
    Custom management command to download external static files from URLs
    and save them to a specified directory within the Django project

    Usage:
        $ cd src
        $ python manage.py pullstatic
    """
    def handle(self, *args: Any, **kwargs: Any) -> None:
        """
        Handle the command execution by downloading the specified static files
        This method iterates through the pre-defined static files, downloads
        them and saves it to the specified directory.
        """
        self.stdout.write("Downloading vendor static files...")
        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            # output path for each file
            out_path = STATICFILES_VENDOR_DIRS / name

            # check if download was successful- if it was, add it to completed_urls
            # list, if not log error message
            download_success = helpers.download_to_local(url=url, out_path=out_path)
            if download_success:
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {url}")
                )
        
        # check if all the expected files were successfully downloaded
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("Successfully updated all vendor static files.")
            )
        else:
            self.stdout.write(
                self.style.WARNING("Some files were not updated.")
            )
