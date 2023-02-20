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


# def get_os() -> None:
# # Get the name of the operating system
# os_name = platform.system()
# if os_name == 'Darwin':  # Mac OS X
#     # Get the version of the operating system
#     os_version = platform.mac_ver()[0]
#     print(f"Mac OS X version: {os_version}")
# elif os_name == 'Linux':  # Linux
#     # Get the version of the operating system
#     os_version = platform.release()
#     print(f"Linux version: {os_version}")
#     # Get the distribution of the operating system
#     linux_distribution = distro.name()
#     print(f"Distribution: {linux_distribution}")
