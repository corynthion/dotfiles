from pathlib import Path

cwd = Path.cwd()
print(cwd)

parent_dir = Path.cwd().parent
print(parent_dir)

home = Path.home()
print(home)

current_file = Path(__file__)
print(current_file)

print(current_file.parent)

def third_func():
    return 'hello'


def second_func():
    # some code    


def first_func(string):
    x =1
    return second_func()

def main(third_func):
    greet = third_func
    first_func(greet)


# #!/bin/bash
# 
# #################################################
# # Dotfiles: Installation
# #################################################
# # [ ! -d $HOME/.config ] && mkdir $HOME/.config
# DOTFILES=$(pwd)
# XDG_CONFIG_DIR=$HOME/.config
# ZDOTDIR=$XDG_CONFIG_DIR/zsh
# 
# # XDG Directories
# rm -rf $HOME/{.config,.local,.cache,.ssh,.viminfo,.zsh*,.bash*}
# mkdir -p $HOME/{.config,.local,.cache}
# 
# # ZSH
# mkdir -p $ZDOTDIR/plugins
# ln -sf $DOTFILES/config/zsh/zshenv $HOME/.zshenv
# ln -sf $DOTFILES/config/zsh/zshrc $ZDOTDIR/.zshrc
# ln -sf $DOTFILES/config/zsh/zshalias $ZDOTDIR/.zshalias
# git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
# git clone https://github.com/zsh-users/zsh-autosuggestions.git
# git clone https://github.com/zsh-users/zsh-completions.git
# git clone https://github.com/MichaelAquilina/zsh-you-should-use.git
# mv -f zsh-* $ZDOTDIR/plugins
# 
# # # Starship Prompt
# ln -sf $DOTFILES/config/starship $XDG_CONFIG_DIR/starship
# 
# # Nord Color Iterm2
# curl -OL https://github.com/arcticicestudio/nord-iterm2/archive/refs/tags/v0.2.0.zip
# unzip v0.2.0.zip
# mv nord-iterm2-0.2.0/src/xml/Nord.itermcolors $HOME/.config
# rm -rf v0.2.0.zip
# rm -rf nord-iterm2-0.2.0
# 
# # Neovim
# ln -sf $DOTFILES/config/nvim $HOME/.config/nvim
# python3 -m pip install --user --upgrade pynvim
# python3 -m pip install --upgrade pip
# sudo gem install neovim
# brew install node
# npm install -g npm
# npm install -g neovim
# 
#  # $XDG_CONFIG_HOME/alacritty/alacritty.yml
#  
#  # Install Commands
#  brew install hyperfine
#  brew install tokei
#  brew install doitlive
#  brew install fd
#  brew install exa
#  brew install bat
#  brew install fzf
#  brew install ripgrep
#  brew install procs
#  brew install broot
#  brew install navi
#  brew install screenfetch
#  brew install neofetch
#  brew install zoxide
#  brew install thefuck
#  brew install tealdeer
#  brew install figlet
#  npm install -g terminalizer
#  pip install howdoi
#  pip install trash-cli
#  
#  # Install Fonts
#  brew tap homebrew/cask-fonts
#  brew install --cask font-inconsolata-nerd-font
############################################################
# Dotfiles Tasks
############################################################
version: '3'

includes:
  fish: ./bin/tasks/fish.yml
  neovim: ./bin/tasks/neovim.yml
  tmux: ./bin/tasks/tmux.yml

silent: true

vars:
  CONFIG: "{{.PWD}}/config"
  CACHE: "{{.PWD}}/cache"
  LOCAL: "{{.PWD}}/local"
  BIN: "{{.LOCAL}}/bin"
  XDG_CONFIG_HOME: "{{.HOME}}/.config"
  XDG_DATA_HOME: "{{.HOME}}/.local/share"
  XDG_CACHE_HOME: "{{.HOME}}/.cache"

tasks:
  default:
    cmds:
      - echo "# ward78 Dotfiles"
      - task -l              

  install:
    desc: Install Dotfiles
    cmds:
      - task: fish:install
      - task: neovim:install
      - task: tmux:install

  remove:
    desc: Remove Dotfiles
    cmds:
      - sudo apt remove bat -y
      - sudo apt remove fd-find -y
      - sudo apt remove fish -y
      - sudo apt remove fzf -y
      - sudo apt remove git -y
      - sudo apt remove neovim -y
      - sudo apt remove python* -y
      - sudo apt remove ripgrep -y
      - sudo apt remove software-properties-common -y
      - sudo apt remove perl -y
      - sudo apt remove cpan -y
      - sudo apt remove cpanm -y
      - sudo apt remove make -y

#- task: fish:remove
#- task: neovim:remove
#- task: tmux:remove
# sudo cpanm -n Neovim::Ext
# cpanm --local-lib=~/perl5 local::lib && eval (perl -I ~/perl5/lib/perl5/ -Mlocal::lib)
# sudo cpanm -n MsgPack::Raw
# sudo cpanm -n Neovim::Ext
# ls perl5/
# sudo cpanm MsgPack::Raw
# cpanm MsgPack::Raw
# cpanm Neovim::Ext
# sudo cpan App::cpanminus
# cpan App::cpanminus
# make
# sudo apt install cpanm
# perl	~/.cpan, ~/perl5	[269]	Perl5's CPAN expects ~/.cpan
##          # - echo "Installing navi command"
##          # - https://github.com/denisidoro/navi/releases/download/v2.17.0/navi-v2.17.0-x86_64-unknown-linux-musl.tar.gz

##          # - echo "Installing howdoi command"
##          # - pip install howdoi

##          # - echo "Installing tealdeer command"
#           # - https://github.com/dbrgn/tealdeer/releases/download/v1.4.1/tldr-linux-x86_64-musl

##          # - echo "Installing tldr command"
#           # - sudo apt -y install tldr

##          # - echo "Installing speedread command"
#           # - https://github.com/pasky/speedread/archive/refs/tags/v1.0.tar.gz

- echo "Installing cheat command"
- https://github.com/cheat/cheat/releases/download/4.2.3/cheat-linux-amd64.gz

 
#
##  - ln -s /usr/bin/batcat ~/.local/bin/bat
##  - Note that the binary is called fdfind as the binary name fd is already used by another package. It is recommended that after installation, you add a link to fd by executing command ln -s $(which fdfind) ~/.local/bin/fd, in order to use fd in the same way as in this documentation. Make sure that $HOME/.local/bin is in your $PATH.
- echo "Installing hyperfine command"
- echo "Installing terminalizer command"
- echo "Installing doitlive command"
- echo "Installing tokei command"

##          # - echo "Installing tokei command"
#           # - https://github.com/XAMPPRocky/tokei/releases/download/v12.1.2/tokei-x86_64-unknown-linux-musl.tar.gz
#
##          # - echo "Installing hyperfine command"
#           # - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz

##          # - echo "Installing terminalizer command"
##          # - npm install -g terminalizer
#
##          # - echo "Installing doitlive command"
##          # - pip install doitlive
#
##          # - echo "Installing timetrap command"
##          # - gem install timetrap
#
version: '3'

silent: true

tasks:
  install:
    desc: Install Fish Shell
    cmds:
      - sudo apt -y install fish 
      - sudo chsh -s $(which fish)
    status:
      - command -v fish 
      - grep fish /etc/shells
      - test "$SHELL" = "/usr/bin/fish"

  remove:
    desc: remove Fish Shell
    cmds:
      - sudo chsh -s $(which bash)
      - sudo apt -y remove fish
    status:
      - "! command -v fish"
      - test "$SHELL" = "/usr/bin/bash"
version: '3'

silent: true

tasks:
  install: 
    desc: Install Neovim
    cmds:
      - sudo apt -y install software-properties-common
      - sudo add-apt-repository ppa:neovim-ppa/unstable -y
      - sudo apt -y update
      - sudo apt -y install neovim
    vars:
        VERSION:
          sh: nvim --version | grep '^NVIM' | awk -F '.' '{print $2}'
    status:
      - test {{.VERSION}} -ge 6

  remove: 
    desc: Remove Neovim
    cmds:
      - echo {{.VERSION}}
      - sudo apt -y remove software-properties-common
      - sudo apt -y remove neovim
    status:
      - "! command -v nvim"
############################################################
# Task: Search Tools
############################################################
version: '3'
silent: true
tasks:
  install:
    desc: Install Search Tools (fd, rg, fzf, procs, autojump)
    dir: ./tmp
    cmds:
      - echo "Installing fd command"
      - curl -sOL https://github.com/sharkdp/fd/releases/download/v8.2.1/fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - tar -xf fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/fd* {{.BIN}}
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/autocomplete/fd.fish {{.BIN}}

      - echo "Installing fzf command"
      - curl -sOL https://github.com/junegunn/fzf/releases/download/0.27.3/fzf-0.27.3-linux_amd64.tar.gz
      - tar -xf fzf-0.27.3-linux_amd64.tar.gz
      - mv fzf {{.BIN}}

      - echo "Installing ripgrep command"
      - curl -sOL https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - tar -xf ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/rg {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/complete/rg.fish {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/doc/rg.1 {{.BIN}}

      - echo "Installing procs command"
      - curl -sOL https://github.com/dalance/procs/releases/download/v0.11.10/procs-v0.11.10-x86_64-lnx.zip
      - unzip -qq procs-v0.11.10-x86_64-lnx.zip
      - mv procs {{.BIN}}

      - echo "Installing thefuck command"
      - sudo apt install thefuck
      - sudo apt install python3-dev python3-pip python3-setuptools
      - sudo pip3 install thefuck

      - echo "Installing nnn command"
      - curl -sOL https://github.com/jarun/nnn/releases/download/v4.3/nnn-musl-static-4.3.x86_64.tar.gz
      - tar -xf nnn-musl-static-4.3.x86_64.tar.gz
      - mv nnn-musl-static {{.BIN}}

      - echo "Installing lf command"
      - curl -sOL https://github.com/gokcehan/lf/releases/download/r26/lf-linux-amd64.tar.gz
      - tar -xf lf-linux-amd64.tar.gz
      - mv lf {{.BIN}}

      - echo "Installing autojump command"
      - sudo apt -y install autojump
      
      - echo "Installing trash-cli command"
      - sudo apt -y install trash-cli
      
      - echo "Installing broot command"
      - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz

- echo "Installing neofetch command"
- echo "Installing starship command"
- echo "Installing exa command"
- echo "Installing bat command"
- echo "Installing figlet command"
#
#      - echo "Installing exa command"
#      - curl -sOL https://github.com/ogham/exa/releases/download/v0.10.1/exa-linux-x86_64-musl-v0.10.1.zip
#      - unzip -qq exa-linux-x86_64-musl-v0.10.1.zip
#      - mv bin/exa {{.BIN}}
#      - mv completions/exa.fish {{.BIN}}
#      - mv man/* {{.BIN}}
#
#      - echo "Installing bat command"
#      - curl -sOL https://github.com/sharkdp/bat/releases/download/v0.18.3/bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
#      - tar -xf bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
#      - mv bat-v0.18.3-x86_64-unknown-linux-musl/bat* {{.BIN}}
#      - mv bat-v0.18.3-x86_64-unknown-linux-musl/autocomplete/bat.fish {{.BIN}}
#

#
#      - echo "Installing starship command"
#      - sudo apt install figlet toilet lolcat
#
#      - echo "Installing starship command"
#      - curl -sOL https://starship.rs/install.sh
#      - chmod 744 install.sh
#      - ./install.sh --yes --bin-dir {{.BIN}} &>/dev/null
#

##    
##          # - echo "Installing neofetch command"
##          # - sudo apt -y install neofetch
#

 install:search:tools:
    desc: Install Search Tools (fd, rg, fzf, procs, autojump)
    dir: ./tmp
    cmds:
      - echo "Installing fd command"
      - curl -sOL https://github.com/sharkdp/fd/releases/download/v8.2.1/fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - tar -xf fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/fd* {{.BIN}}
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/autocomplete/fd.fish {{.BIN}}

      - echo "Installing fzf command"
      - curl -sOL https://github.com/junegunn/fzf/releases/download/0.27.3/fzf-0.27.3-linux_amd64.tar.gz
      - tar -xf fzf-0.27.3-linux_amd64.tar.gz
      - mv fzf {{.BIN}}

      - echo "Installing ripgrep command"
      - curl -sOL https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - tar -xf ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/rg {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/complete/rg.fish {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/doc/rg.1 {{.BIN}}

      - echo "Installing procs command"
      - curl -sOL https://github.com/dalance/procs/releases/download/v0.11.10/procs-v0.11.10-x86_64-lnx.zip
      - unzip -qq procs-v0.11.10-x86_64-lnx.zip
      - mv procs {{.BIN}}

      - echo "Installing exa command"
      - curl -sOL https://github.com/ogham/exa/releases/download/v0.10.1/exa-linux-x86_64-musl-v0.10.1.zip
      - unzip -qq exa-linux-x86_64-musl-v0.10.1.zip
      - mv bin/exa {{.BIN}}
      - mv completions/exa.fish {{.BIN}}
      - mv man/* {{.BIN}}

      - echo "Installing bat command"
      - curl -sOL https://github.com/sharkdp/bat/releases/download/v0.18.3/bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
      - tar -xf bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
      - mv bat-v0.18.3-x86_64-unknown-linux-musl/bat* {{.BIN}}
      - mv bat-v0.18.3-x86_64-unknown-linux-musl/autocomplete/bat.fish {{.BIN}}

      - echo "Installing nnn command"
      - curl -sOL https://github.com/jarun/nnn/releases/download/v4.3/nnn-musl-static-4.3.x86_64.tar.gz
      - tar -xf nnn-musl-static-4.3.x86_64.tar.gz
      - mv nnn-musl-static {{.BIN}}

      - echo "Installing lf command"
      - curl -sOL https://github.com/gokcehan/lf/releases/download/r26/lf-linux-amd64.tar.gz
      - tar -xf lf-linux-amd64.tar.gz
      - mv lf {{.BIN}}

      - echo "Installing starship command"
      - sudo apt install figlet toilet lolcat

      - echo "Installing starship command"
      - curl -sOL https://starship.rs/install.sh
      - chmod 744 install.sh
      - ./install.sh --yes --bin-dir {{.BIN}} &>/dev/null

#          # - echo "Installing autojump command"
#          # - sudo apt -y install autojump
#    
#          # - echo "Installing trash-cli command"
#          # - sudo apt -y install trash-cli
#    
#          # - echo "Installing neofetch command"
#          # - sudo apt -y install neofetch

#          # - echo "Installing terminalizer command"
#          # - npm install -g terminalizer

#          # - echo "Installing doitlive command"
#          # - pip install doitlive

#          # - echo "Installing timetrap command"
#          # - gem install timetrap

#          # - echo "Installing howdoi command"
#          # - pip install howdoi 

#          # - echo "Installing howdoi command"
#          # - https://github.com/cheat/cheat/releases/download/4.2.3/cheat-linux-amd64.gz

#          # - echo "Installing howdoi command"
#          # - https://github.com/denisidoro/navi/releases/download/v2.17.0/navi-v2.17.0-x86_64-unknown-linux-musl.tar.gz

#          # - echo "Installing thefuck command"
#          # - https://github.com/cheat/cheat/releases/download/4.2.3/cheat-linux-amd64.gz
           # - sudo apt install thefuck
           # - sudo apt install python3-dev python3-pip python3-setuptools
           # - sudo pip3 install thefuck

#          # - echo "Installing tealdeer command"
           # - https://github.com/dbrgn/tealdeer/releases/download/v1.4.1/tldr-linux-x86_64-musl

#          # - echo "Installing tldr command"
           # - sudo apt -y install tldr

#          # - echo "Installing tokei command"
           # - https://github.com/XAMPPRocky/tokei/releases/download/v12.1.2/tokei-x86_64-unknown-linux-musl.tar.gz


#          # - echo "Installing hyperfine command"
           # - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz


#          # - echo "Installing broot command"
           # - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz

#          # - echo "Installing speedread command"
           # - https://github.com/pasky/speedread/archive/refs/tags/v1.0.tar.gz


#  - ln -s /usr/bin/batcat ~/.local/bin/bat
#  - Note that the binary is called fdfind as the binary name fd is already used by another package. It is recommended that after installation, you add a link to fd by executing command ln -s $(which fdfind) ~/.local/bin/fd, in order to use fd in the same way as in this documentation. Make sure that $HOME/.local/bin is in your $PATH.
version: '3'

silent: true

tasks:
  install:
    desc: Install Tmux
    cmds:
      - sudo apt -y install tmux
    status:
      - command -v tmux
  remove:
    desc: Remove Tmux
    cmds:
      - sudo apt -y remove tmux
    status:
      - "! command -v tmux"
…or create a new repository on the command line
echo "# dotfiles" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:ward78/dotfiles.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin git@github.com:ward78/dotfiles.git
git branch -M main
git push -u origin main
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.




##          # - echo "Installing navi command"
##          # - https://github.com/denisidoro/navi/releases/download/v2.17.0/navi-v2.17.0-x86_64-unknown-linux-musl.tar.gz

##          # - echo "Installing howdoi command"
##          # - pip install howdoi

##          # - echo "Installing tealdeer command"
#           # - https://github.com/dbrgn/tealdeer/releases/download/v1.4.1/tldr-linux-x86_64-musl

##          # - echo "Installing tldr command"
#           # - sudo apt -y install tldr

##          # - echo "Installing speedread command"
#           # - https://github.com/pasky/speedread/archive/refs/tags/v1.0.tar.gz

- echo "Installing cheat command"
- https://github.com/cheat/cheat/releases/download/4.2.3/cheat-linux-amd64.gz

 
#
##  - ln -s /usr/bin/batcat ~/.local/bin/bat
##  - Note that the binary is called fdfind as the binary name fd is already used by another package. It is recommended that after installation, you add a link to fd by executing command ln -s $(which fdfind) ~/.local/bin/fd, in order to use fd in the same way as in this documentation. Make sure that $HOME/.local/bin is in your $PATH.
- echo "Installing hyperfine command"
- echo "Installing terminalizer command"
- echo "Installing doitlive command"
- echo "Installing tokei command"

##          # - echo "Installing tokei command"
#           # - https://github.com/XAMPPRocky/tokei/releases/download/v12.1.2/tokei-x86_64-unknown-linux-musl.tar.gz
#
##          # - echo "Installing hyperfine command"
#           # - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz

##          # - echo "Installing terminalizer command"
##          # - npm install -g terminalizer
#
##          # - echo "Installing doitlive command"
##          # - pip install doitlive
#
##          # - echo "Installing timetrap command"
##          # - gem install timetrap
#
############################################################
# Task: Search Tools
############################################################
version: '3'
silent: true
tasks:
  install:
    desc: Install Search Tools (fd, rg, fzf, procs, autojump)
    dir: ./tmp
    cmds:
      - echo "Installing fd command"
      - curl -sOL https://github.com/sharkdp/fd/releases/download/v8.2.1/fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - tar -xf fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/fd* {{.BIN}}
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/autocomplete/fd.fish {{.BIN}}

      - echo "Installing fzf command"
      - curl -sOL https://github.com/junegunn/fzf/releases/download/0.27.3/fzf-0.27.3-linux_amd64.tar.gz
      - tar -xf fzf-0.27.3-linux_amd64.tar.gz
      - mv fzf {{.BIN}}

      - echo "Installing ripgrep command"
      - curl -sOL https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - tar -xf ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/rg {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/complete/rg.fish {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/doc/rg.1 {{.BIN}}

      - echo "Installing procs command"
      - curl -sOL https://github.com/dalance/procs/releases/download/v0.11.10/procs-v0.11.10-x86_64-lnx.zip
      - unzip -qq procs-v0.11.10-x86_64-lnx.zip
      - mv procs {{.BIN}}

      - echo "Installing thefuck command"
      - sudo apt install thefuck
      - sudo apt install python3-dev python3-pip python3-setuptools
      - sudo pip3 install thefuck

      - echo "Installing nnn command"
      - curl -sOL https://github.com/jarun/nnn/releases/download/v4.3/nnn-musl-static-4.3.x86_64.tar.gz
      - tar -xf nnn-musl-static-4.3.x86_64.tar.gz
      - mv nnn-musl-static {{.BIN}}

      - echo "Installing lf command"
      - curl -sOL https://github.com/gokcehan/lf/releases/download/r26/lf-linux-amd64.tar.gz
      - tar -xf lf-linux-amd64.tar.gz
      - mv lf {{.BIN}}

      - echo "Installing autojump command"
      - sudo apt -y install autojump
      
      - echo "Installing trash-cli command"
      - sudo apt -y install trash-cli
      
      - echo "Installing broot command"
      - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz

- echo "Installing neofetch command"
- echo "Installing starship command"
- echo "Installing exa command"
- echo "Installing bat command"
- echo "Installing figlet command"
#
#      - echo "Installing exa command"
#      - curl -sOL https://github.com/ogham/exa/releases/download/v0.10.1/exa-linux-x86_64-musl-v0.10.1.zip
#      - unzip -qq exa-linux-x86_64-musl-v0.10.1.zip
#      - mv bin/exa {{.BIN}}
#      - mv completions/exa.fish {{.BIN}}
#      - mv man/* {{.BIN}}
#
#      - echo "Installing bat command"
#      - curl -sOL https://github.com/sharkdp/bat/releases/download/v0.18.3/bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
#      - tar -xf bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
#      - mv bat-v0.18.3-x86_64-unknown-linux-musl/bat* {{.BIN}}
#      - mv bat-v0.18.3-x86_64-unknown-linux-musl/autocomplete/bat.fish {{.BIN}}
#

#
#      - echo "Installing starship command"
#      - sudo apt install figlet toilet lolcat
#
#      - echo "Installing starship command"
#      - curl -sOL https://starship.rs/install.sh
#      - chmod 744 install.sh
#      - ./install.sh --yes --bin-dir {{.BIN}} &>/dev/null
#

##    
##          # - echo "Installing neofetch command"
##          # - sudo apt -y install neofetch
#

 install:search:tools:
    desc: Install Search Tools (fd, rg, fzf, procs, autojump)
    dir: ./tmp
    cmds:
      - echo "Installing fd command"
      - curl -sOL https://github.com/sharkdp/fd/releases/download/v8.2.1/fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - tar -xf fd-v8.2.1-x86_64-unknown-linux-musl.tar.gz
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/fd* {{.BIN}}
      - mv fd-v8.2.1-x86_64-unknown-linux-musl/autocomplete/fd.fish {{.BIN}}

      - echo "Installing fzf command"
      - curl -sOL https://github.com/junegunn/fzf/releases/download/0.27.3/fzf-0.27.3-linux_amd64.tar.gz
      - tar -xf fzf-0.27.3-linux_amd64.tar.gz
      - mv fzf {{.BIN}}

      - echo "Installing ripgrep command"
      - curl -sOL https://github.com/BurntSushi/ripgrep/releases/download/13.0.0/ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - tar -xf ripgrep-13.0.0-x86_64-unknown-linux-musl.tar.gz
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/rg {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/complete/rg.fish {{.BIN}}
      - mv ripgrep-13.0.0-x86_64-unknown-linux-musl/doc/rg.1 {{.BIN}}

      - echo "Installing procs command"
      - curl -sOL https://github.com/dalance/procs/releases/download/v0.11.10/procs-v0.11.10-x86_64-lnx.zip
      - unzip -qq procs-v0.11.10-x86_64-lnx.zip
      - mv procs {{.BIN}}

      - echo "Installing exa command"
      - curl -sOL https://github.com/ogham/exa/releases/download/v0.10.1/exa-linux-x86_64-musl-v0.10.1.zip
      - unzip -qq exa-linux-x86_64-musl-v0.10.1.zip
      - mv bin/exa {{.BIN}}
      - mv completions/exa.fish {{.BIN}}
      - mv man/* {{.BIN}}

      - echo "Installing bat command"
      - curl -sOL https://github.com/sharkdp/bat/releases/download/v0.18.3/bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
      - tar -xf bat-v0.18.3-x86_64-unknown-linux-musl.tar.gz
      - mv bat-v0.18.3-x86_64-unknown-linux-musl/bat* {{.BIN}}
      - mv bat-v0.18.3-x86_64-unknown-linux-musl/autocomplete/bat.fish {{.BIN}}

      - echo "Installing nnn command"
      - curl -sOL https://github.com/jarun/nnn/releases/download/v4.3/nnn-musl-static-4.3.x86_64.tar.gz
      - tar -xf nnn-musl-static-4.3.x86_64.tar.gz
      - mv nnn-musl-static {{.BIN}}

      - echo "Installing lf command"
      - curl -sOL https://github.com/gokcehan/lf/releases/download/r26/lf-linux-amd64.tar.gz
      - tar -xf lf-linux-amd64.tar.gz
      - mv lf {{.BIN}}

      - echo "Installing starship command"
      - sudo apt install figlet toilet lolcat

      - echo "Installing starship command"
      - curl -sOL https://starship.rs/install.sh
      - chmod 744 install.sh
      - ./install.sh --yes --bin-dir {{.BIN}} &>/dev/null

#          # - echo "Installing autojump command"
#          # - sudo apt -y install autojump
#    
#          # - echo "Installing trash-cli command"
#          # - sudo apt -y install trash-cli
#    
#          # - echo "Installing neofetch command"
#          # - sudo apt -y install neofetch

#          # - echo "Installing terminalizer command"
#          # - npm install -g terminalizer

#          # - echo "Installing doitlive command"
#          # - pip install doitlive

#          # - echo "Installing timetrap command"
#          # - gem install timetrap

#          # - echo "Installing howdoi command"
#          # - pip install howdoi 

#          # - echo "Installing howdoi command"
#          # - https://github.com/cheat/cheat/releases/download/4.2.3/cheat-linux-amd64.gz

#          # - echo "Installing howdoi command"
#          # - https://github.com/denisidoro/navi/releases/download/v2.17.0/navi-v2.17.0-x86_64-unknown-linux-musl.tar.gz

#          # - echo "Installing thefuck command"
#          # - https://github.com/cheat/cheat/releases/download/4.2.3/cheat-linux-amd64.gz
           # - sudo apt install thefuck
           # - sudo apt install python3-dev python3-pip python3-setuptools
           # - sudo pip3 install thefuck

#          # - echo "Installing tealdeer command"
           # - https://github.com/dbrgn/tealdeer/releases/download/v1.4.1/tldr-linux-x86_64-musl

#          # - echo "Installing tldr command"
           # - sudo apt -y install tldr

#          # - echo "Installing tokei command"
           # - https://github.com/XAMPPRocky/tokei/releases/download/v12.1.2/tokei-x86_64-unknown-linux-musl.tar.gz


#          # - echo "Installing hyperfine command"
           # - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz


#          # - echo "Installing broot command"
           # - https://github.com/sharkdp/hyperfine/releases/download/v1.12.0/hyperfine-v1.12.0-x86_64-unknown-linux-musl.tar.gz

#          # - echo "Installing speedread command"
           # - https://github.com/pasky/speedread/archive/refs/tags/v1.0.tar.gz


#  - ln -s /usr/bin/batcat ~/.local/bin/bat
#  - Note that the binary is called fdfind as the binary name fd is already used by another package. It is recommended that after installation, you add a link to fd by executing command ln -s $(which fdfind) ~/.local/bin/fd, in order to use fd in the same way as in this documentation. Make sure that $HOME/.local/bin is in your $PATH.
