#    from pathlib import Path
#    import os
#    import shutil
#    import subprocess
#    import time
#    import platform
#    import distro

def dotfiles_path():
	pass

def dotfiles_backup():
	pass

def dotfiles_remove():
	pass

def dotfiles_install():
	pass


#    # Create the XDG_CONFIG_DIR if it doesn't exist
#    if not os.path.exists(os.path.expanduser('~/.config')):
#        os.mkdir(os.path.expanduser('~/.config'))
#    # Set the DOTFILES and XDG_CONFIG_DIR variables
#    DOTFILES = os.getcwd()
#    XDG_CONFIG_DIR = os.path.expanduser('~/.config')
#    ZDOTDIR = os.path.join(XDG_CONFIG_DIR, 'zsh')
#    # Remove existing dotfiles
#    shutil.rmtree(os.path.expanduser('~/.config'))
#    shutil.rmtree(os.path.expanduser('~/.local'))
#    shutil.rmtree(os.path.expanduser('~/.cache'))
#    shutil.rmtree(os.path.expanduser('~/.ssh'))
#    os.remove(os.path.expanduser('~/.viminfo'))
#    for file in os.listdir(os.path.expanduser('~')):
#        if file.startswith('.zsh') or file.startswith('.bash'):
#            os.remove(os.path.join(os.path.expanduser('~'), file))
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
#    # Name of the directory to back up
#    directory_name = 'my_directory'
#    # Create a timestamp string for the backup directory name
#    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
#    # Name of the backup directory
#    backup_name = f'{directory_name}_backup_{timestamp}'
#    # Path of the original directory to back up
#    original_directory_path = os.path.join(os.getcwd(), directory_name)
#    # Path of the backup directory
#    backup_directory_path = os.path.join(os.getcwd(), backup_name)
#    # Create the backup directory
#    shutil.copytree(original_directory_path, backup_directory_path)
#    # Delete the original directory and its contents
#    shutil.rmtree(original_directory_path)
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
#    try:
#    	cwd = Path.cwd()
#    	current_file = Path(__file__)
#    	if cwd != current_file.parent:
#    		raise ValueError("Current working directory is not the parent directory of the script file.")
#    	else:
#    		print("hello")
#    except ValueError as ve:
#    	print(ve)
#    # Name of the directory to back up
#    directory_name = 'my_directory'
#    # Create a timestamp string for the backup directory name
#    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
#    # Name of the backup directory
#    backup_name = f'{directory_name}_backup_{timestamp}'
#    # Path of the original directory to back up
#    original_directory_path = os.path.join(os.getcwd(), directory_name)
#    # Path of the backup directory
#    backup_directory_path = os.path.join(os.getcwd(), backup_name)
#    # Create the backup directory
#    shutil.copytree(original_directory_path, backup_directory_path)
#    # Delete the original directory and its contents
#    shutil.rmtree(original_directory_path)
