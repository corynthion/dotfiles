import shutil
import time
from pathlib import Path
from typing import Callable, Generator


def remove_dotfiles(get_dotfiles: Callable[[], Generator[Path, None, None]]) -> None:
    dotfiles: Generator[Path, None, None] = get_dotfiles()
    for dotfile in dotfiles:
        if dotfile.exists():
            if dotfile.is_file():
                dotfile.unlink()
            elif dotfile.is_dir():
                shutil.rmtree(str(dotfile))


def backup_dotfile(dotfile: Path, backup_dir: Path) -> None:
    backup_path: Path = backup_dir / dotfile.name
    if dotfile.is_file():
        shutil.copy(str(dotfile), str(backup_path))
    elif dotfile.is_dir():
        shutil.copytree(str(dotfile), str(backup_path))


def backup_dotfiles(
    backup_dir: Path, get_dotfiles: Callable[[], Generator[Path, None, None]]
) -> None:
    dotfiles: Generator[Path, None, None] = get_dotfiles()
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    backup_sub_dir: Path = backup_dir / f"dotfiles_{timestamp}"
    backup_sub_dir.mkdir(parents=True, exist_ok=True)
    for dotfile in dotfiles:
        if dotfile.exists():
            backup_dotfile(dotfile, backup_sub_dir)


def get_dotfiles() -> Generator[Path, None, None]:
    home_dir: Path = Path.home()
    dotfiles: Generator[Path, None, None] = home_dir.glob(".*")
    return (
        dotfile for dotfile in dotfiles if dotfile.name not in [".", "..", ".Trash"]
    )


def has_dotfiles(get_dotfiles: Callable[[], Generator[Path, None, None]]) -> bool:
    try:
        next(get_dotfiles())
        return True
    except StopIteration:
        return False


def get_paths() -> dict[str, Path]:
    script_dir: Path = Path(__file__).parent
    if Path.cwd() != script_dir:
        raise ValueError(f"Run this file from within the {script_dir} directory.")
    home_dir: Path = Path.home()
    return {
        "backup_dir": home_dir / "dotfiles_backup",
        "xdg_data_home": home_dir / ".local" / "share",
        "xdg_cache_home": home_dir / ".cache",
        "xdg_config_home": home_dir / ".config",
    }


def main() -> None:
    paths: dict[str, Path] = get_paths()
    if has_dotfiles(get_dotfiles):
        backup_dotfiles(paths["backup_dir"], get_dotfiles)
        remove_dotfiles(get_dotfiles)
    # else:
    # print("No dotfiles found.")


if __name__ == "__main__":
    main()

#    # ZSH
#    export ZDOTDIR="$XDG_CONFIG_HOME/zsh"
#    export STARSHIP_CONFIG="$XDG_CONFIG_HOME/starship/.starship.toml"
#
#    # Create the XDG_CONFIG_DIR if it doesn't exist
#    if not os.path.exists(os.path.expanduser('~/.config')):
#        os.mkdir(os.path.expanduser('~/.config'))

#    # Create new directories
#    os.makedirs(os.path.expanduser('~/.config'))
#    os.makedirs(os.path.expanduser('~/.local'))
#    os.makedirs(os.path.expanduser('~/.cache'))

#    # Set up Zsh
#    os.makedirs(os.path.join(ZDOTDIR, 'plugins'))
#    os.symlink(os.path.join(DOTFILES, 'config/zsh/zshenv'), os.path.expanduser('~/.zshenv'))
#    os.symlink(os.path.join(DOTFILES, 'config/zsh/zshrc'), os.path.join(ZDOTDIR, '.zshrc'))
#    os.symlink(os.path.join(DOTFILES, 'config/zsh/zshalias'), os.path.join(ZDOTDIR, '.zshalias'))
#    subprocess.run(['git', 'clone', 'https://github.com/zsh-users/zsh-syntax-highlighting.git'])
#    subprocess.run(['git', 'clone', 'https://github.com/zsh-users/zsh-autosuggestions.git'])
#    subprocess.run(['git', 'clone', 'https://github.com/zsh-users/zsh-completions.git'])
#    subprocess.run(['git', 'clone', 'https://github.com/MichaelAquilina/zsh-you-should-use.git'])
#    shutil.move('zsh-*', os.path.join(ZDOTDIR, 'plugins'))

#    # Set up Starship Prompt
#    os.symlink(os.path.join(DOTFILES, 'config/starship'), os.path.join(XDG_CONFIG_DIR, 'starship'))

#    # Set up Nord Color Iterm2
#    subprocess.run(['curl', '-OL', 'https://github.com/arcticicestudio/nord-iterm2/archive/refs/tags/v0.2.0.zip'])
#    subprocess.run(['unzip', 'v0.2.0.zip'])
#    shutil.move('nord-iterm2-0.2.0/src/xml/Nord.itermcolors', os.path.join(XDG_CONFIG_DIR, 'Nord.itermcolors'))
#    os.remove('v0.2.0.zip')
#    shutil.rmtree('nord-iterm2-0.2.0')

#    # Set up Neovim
#    os.symlink(os.path.join(DOTFILES, 'config/nvim'), os.path.join(XDG_CONFIG_DIR, 'nvim'))
#    subprocess.run(['python3', '-m', 'pip', 'install', '--user', '--upgrade', 'pynvim'])
#    subprocess.run(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
#    subprocess.run(['sudo', 'gem', 'install', 'neovim'])
#    subprocess.run(['brew', 'install', 'node'])
#    subprocess.run(['npm', 'install', '-g', 'npm'])
#    subprocess.run(['npm', 'install', '-g', 'ne

#    # Get the name of the operating system
#    os_name = platform.system()
#    if os_name == 'Darwin':  # Mac OS X
#        # Get the version of the operating system
#        os_version = platform.mac_ver()[0]
#        print(f"Mac OS X version: {os_version}")
#    elif os_name == 'Linux':  # Linux
#        # Get the version of the operating system
#        os_version = platform.release()
#        print(f"Linux version: {os_version}")
#        # Get the distribution of the operating system
#        linux_distribution = distro.name()
#        print(f"Distribution: {linux_distribution}")
