import os
import sys


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crop_project.settings")
    argv = sys.argv if len(sys.argv) > 1 else [sys.argv[0], "runserver"]

    from django.core.management import execute_from_command_line

    execute_from_command_line(argv)


if __name__ == "__main__":
    main()
