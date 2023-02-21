import shutil
import time
from pathlib import Path
from typing import Generator
import platform
import distro

BACKUP_AND_DELETE_DOTFILES: bool = True


def get_os() -> None:
    os_name: str = platform.system()
    if os_name == "Darwin":  # Mac OS X
        os_version: str = platform.mac_ver()[0]
        print(f"Mac OS X version: {os_version}")
    elif os_name == "Linux":  # Linux
        os_version = platform.release()
        print(f"Linux version: {os_version}")
        linux_distribution: str = distro.name()
        print(f"Distribution: {linux_distribution}")


def backup_dotfile(dotfile: Path, backup_dir: Path) -> None:
    backup_path: Path = backup_dir / dotfile.name
    if dotfile.is_file():
        shutil.copy(str(dotfile), str(backup_path))
    elif dotfile.is_dir():
        shutil.copytree(str(dotfile), str(backup_path))


def remove_dotfiles(home: Path, filter: list[str]) -> None:
    dotfiles: Generator[Path, None, None] = get_dotfiles(home, filter)
    for dotfile in dotfiles:
        if dotfile.exists():
            if dotfile.is_file():
                dotfile.unlink()
            elif dotfile.is_dir():
                shutil.rmtree(str(dotfile))


def backup_dotfiles(home: Path, backup_dir: Path, filter: list[str]) -> None:
    dotfiles: Generator[Path, None, None] = get_dotfiles(home, filter)
    timestamp: str = time.strftime("%Y-%m-%d-%H-%M-%S")
    backup_sub_dir: Path = backup_dir / f"dotfiles_{timestamp}"
    backup_sub_dir.mkdir(parents=True, exist_ok=True)
    for dotfile in dotfiles:
        if dotfile.exists():
            backup_dotfile(dotfile, backup_sub_dir)


def get_dotfiles(home: Path, filter: list[str]) -> Generator[Path, None, None]:
    files: Generator[Path, None, None] = get_files(home, ".*")
    return (file for file in files if file.name not in filter)


def get_files(path: Path, filter: str) -> Generator[Path, None, None]:
    return path.glob(filter)


def get_paths() -> dict[str, dict[str, Path]]:
    script_dir: Path = Path(__file__).parent
    if Path.cwd() != script_dir:
        raise ValueError(f"Run this file from within the {script_dir} directory.")
    home_dir: Path = Path.home()
    base_dirs: dict[str, Path] = {
        "home": home_dir,
        "dotfiles": script_dir,
        "config": script_dir / "config",
        "backups": home_dir / "dotfiles_backups",
    }
    xdg_dirs: dict[str, Path] = {
        "data": home_dir / ".local" / "share",
        "cache": home_dir / ".cache",
        "config": home_dir / ".config",
    }
    return {
        "base_dirs": base_dirs,
        "xdg_dirs": xdg_dirs,
    }


def has_dotfiles(home: Path, filter: list[str]) -> bool:
    dotfiles: Generator[Path, None, None] = get_dotfiles(home, filter)
    try:
        next(dotfiles)
        return True
    except StopIteration:
        return False


def create_xdg_dirs(xdg_dirs: dict[str, Path]) -> None:
    for xdg_dir in xdg_dirs.values():
        xdg_dir.mkdir(parents=True, exist_ok=True)


def configure_zsh(home: Path, config_dir: Path, xdg_dirs: dict[str, Path]) -> None:
    zdot_dir: Path = xdg_dirs["config"] / "zsh"
    zdot_dir.mkdir(parents=True, exist_ok=True)
    zsh_config_dir: Path = config_dir / "zsh"
    zsh_files: Generator[Path, None, None] = get_files(zsh_config_dir, "*")
    for zsh_file in zsh_files:
        if zsh_file.name == "zshenv":
            dest_file: Path = home / f".{zsh_file.name}"
            dest_file.symlink_to(zsh_file)
        else:
            dest_file: Path = zdot_dir / f".{zsh_file.name}"
            dest_file.symlink_to(zsh_file)


def main() -> None:
    base_dirs: dict[str, Path] = get_paths()["base_dirs"]
    xdg_dirs: dict[str, Path] = get_paths()["xdg_dirs"]
    home: Path = base_dirs["home"]
    get_os()
    if BACKUP_AND_DELETE_DOTFILES:
        filter: list[str] = [".Trash", ".vscode", ".ssh", ".zprofile", ".gitconfig"]
        if has_dotfiles(home, filter):
            backup_dir: Path = base_dirs["backups"]
            backup_dotfiles(home, backup_dir, filter)
            remove_dotfiles(home, filter)
    create_xdg_dirs(xdg_dirs)
    config_dir: Path = base_dirs["config"]
    configure_zsh(home, config_dir, xdg_dirs)


if __name__ == "__main__":
    main()

# source_file: Path = Path("/path/to/source/file.txt")
# target_link: Path = Path("/path/to/target/link.txt")
# target_link.symlink_to(source_file)
# zcache_dir: Path = xdg_dirs["xdg_cache_home"] / "zsh"
# zcache_dir.mkdir(parents=True, exist_ok=True)
# os.makedirs(os.path.join(ZDOTDIR, 'plugins'))
# os.symlink(os.path.join(DOTFILES, 'config/zsh/zshenv'), os.path.expanduser('~/.zshenv'))
# os.symlink(os.path.join(DOTFILES, 'config/zsh/zshrc'), os.path.join(ZDOTDIR, '.zshrc'))
# os.symlink(os.path.join(DOTFILES, 'config/zsh/zshalias'), os.path.join(ZDOTDIR, '.zshalias'))
# subprocess.run(['git', 'clone', 'https://github.com/zsh-users/zsh-syntax-highlighting.git'])
# subprocess.run(['git', 'clone', 'https://github.com/zsh-users/zsh-autosuggestions.git'])
# subprocess.run(['git', 'clone', 'https://github.com/zsh-users/zsh-completions.git'])
# subprocess.run(['git', 'clone', 'https://github.com/MichaelAquilina/zsh-you-should-use.git'])
# shutil.move('zsh-*', os.path.join(ZDOTDIR, 'plugins'))
# # Set up Starship Prompt
# os.symlink(os.path.join(DOTFILES, 'config/starship'), os.path.join(XDG_CONFIG_DIR, 'starship'))


# def configure_nord_theme() -> None:
# # Set up Nord Color Iterm2
# subprocess.run(['curl', '-OL', 'https://github.com/arcticicestudio/nord-iterm2/archive/refs/tags/v0.2.0.zip'])
# subprocess.run(['unzip', 'v0.2.0.zip'])
# shutil.move('nord-iterm2-0.2.0/src/xml/Nord.itermcolors', os.path.join(XDG_CONFIG_DIR, 'Nord.itermcolors'))
# os.remove('v0.2.0.zip')
# shutil.rmtree('nord-iterm2-0.2.0')


# def configure_neovim() -> None:
# # Set up Neovim
# os.symlink(os.path.join(DOTFILES, 'config/nvim'), os.path.join(XDG_CONFIG_DIR, 'nvim'))
# subprocess.run(['python3', '-m', 'pip', 'install', '--user', '--upgrade', 'pynvim'])
# subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
# subprocess.run(['sudo', 'gem', 'install', 'neovim'])
# subprocess.run(['brew', 'install', 'node'])
# subprocess.run(['npm', 'install', '-g', 'npm'])
# subprocess.run(['npm', 'install', '-g', 'ne

# echo "Installing autojump"
# echo "Installing bat"
# echo "Installing broot"
# echo "Installing doitlive"
# echo "Installing exa"
# echo "Installing figlet"
# echo "Installing howdoi"
# echo "Installing hyperfine"
# echo "Installing lf"
# echo "Installing neofetch"
# echo "Installing neofetch"
# echo "Installing nnn"
# echo "Installing procs"
# echo "Installing speedread"
# echo "Installing starship"
# echo "Installing tealdeer"
# echo "Installing terminalizer"
# echo "Installing thefuck"
# echo "Installing timetrap"
# echo "Installing tldr"
# echo "Installing tokei"
# echo "Installing trash-cli"
# echo "Installing bat"
# echo "Installing fd-find"
# echo "Installing fzf"
# echo "Installing git"
# echo "Installing neovim"
# echo "Installing python*"
# echo "Installing ripgrep"
