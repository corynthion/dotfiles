# from builtins import print
# import shutil
# import time
from pathlib import Path

# from typing import Callable, Generator, Any, Literal

# BACKUP_AND_DELETE_DOTFILES: Literal[False] = False


# def filter_dotfiles() -> None:
#     ...


# def remove_dotfiles(dotfiles: Callable[[], Generator[Path, None, None]]) -> None:
#     dotfiles_gen: Generator[Path, None, None] = dotfiles()
#     for dotfile in dotfiles_gen:
#         if dotfile.exists():
#             if dotfile.is_file():
#                 dotfile.unlink()
#             elif dotfile.is_dir():
#                 shutil.rmtree(str(dotfile))


# def backup_dotfile(dotfile: Path, backup_dir: Path) -> None:
#     backup_path: Path = backup_dir / dotfile.name
#     if dotfile.is_file():
#         shutil.copy(str(dotfile), str(backup_path))
#     elif dotfile.is_dir():
#         shutil.copytree(str(dotfile), str(backup_path))


# def backup_dotfiles(
#     backup_dir: Path, files: Callable[[Path, str], Generator[Path, None, None]]
# ) -> None:
#     home: Path = Path.home()
#     find: Literal[".*"] = ".*"
#     dotfiles_gen: Generator[Path, None, None] = files(home, find)
#     timestamp: str = time.strftime("%Y-%m-%d-%H-%M-%S")
#     backup_sub_dir: Path = backup_dir / f"dotfiles_{timestamp}"
#     backup_sub_dir.mkdir(parents=True, exist_ok=True)
#     for dotfile in dotfiles_gen:
#         if dotfile.exists():
#             backup_dotfile(dotfile, backup_sub_dir)


# def create_xdg_dirs() -> None:
#     path: dict[str, Any] = get_paths()
#     xdg_dirs: dict[str, Path] = path["xdg_dirs"]
#     for xdg_dir in xdg_dirs.values():
#         xdg_dir.mkdir(parents=True, exist_ok=True)


# def configure_zsh() -> None:
#     path: dict[str, Any] = get_paths()
#     xdg_dirs: dict[str, Path] = path["xdg_dirs"]
#     zdot_dir: Path = xdg_dirs["xdg_config_home"] / "zsh"
#     zdot_dir.mkdir(parents=True, exist_ok=True)
#     config_dir: Path = path["config"]
#     zsh_config_dir: Path = config_dir / "zsh"
#     zsh_config_files: Generator[Path, None, None] = get_files(zsh_config_dir, "*")
#     for zsh_config_file in zsh_config_files:
#         if zsh_config_file.name == "zshenv":
#             dest_file: Path = path["home"] / f".{zsh_config_file.name}"
#             dest_file.symlink_to(zsh_config_file)
#         else:
#             dest_file: Path = zdot_dir / f".{zsh_config_file.name}"
#             dest_file.symlink_to(zsh_config_file)


# def get_files(path: Path, find: str) -> Generator[Path, None, None]:
#     return path.glob(find)


def get_paths() -> dict[str, dict[str, Path]]:
    script_dir: Path = Path(__file__).parent
    if Path.cwd() != script_dir:
        raise ValueError(f"Run this file from within the {script_dir} directory.")
    home_dir: Path = Path.home()
    dotfiles_dirs: dict[str, Path] = {
        "dotfiles": script_dir,
        "configs": script_dir / "configs",
        "backups": home_dir / "dotfiles_backups",
    }
    xdg_dirs: dict[str, Path] = {
        "data": home_dir / ".local" / "share",
        "cache": home_dir / ".cache",
        "config": home_dir / ".config",
    }
    return {
        "dotfiles": dotfiles_dirs,
        "xdg": xdg_dirs,
    }


# def get_dotfiles() -> Generator[Path, None, None]:
#     dotfiles_gen: Generator[Path, None, None] = Path.home().glob(".*")
#     return (
#         dotfile for dotfile in dotfiles_gen if dotfile.name not in [".", "..", ".Trash"]
#     )


# def get_files(path: Path, find: str) -> Generator[Path, None, None]:
#     return path.glob(find)


# def has_dotfiles(files: Callable[[Path, str], Generator[Path, None, None]]) -> bool:
#     try:
#         home: Path = Path.home()
#         find: Literal[".*"] = ".*"
#         next(files(home, find))
#         return True
#     except StopIteration:
#         return False


def main() -> None:
    paths: dict[str, dict[str, Path]] = get_paths()
    print(paths)


#     if BACKUP_AND_DELETE_DOTFILES:
#         if has_dotfiles(get_files):
#             backup_dotfiles(paths["backup_dir"], get_dotfiles)
#             remove_dotfiles(get_dotfiles)
#     create_xdg_dirs()
#     configure_zsh()


if __name__ == "__main__":
    main()
