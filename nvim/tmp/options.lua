-----------------------------------------------
-- options.lua
-----------------------------------------------
-- vim.g.mapleader = ' '
-- local bo  = vim.bo  -- buffer local
-- local cmd = vim.cmd -- commands
-- local fn  = vim.fn  -- access vim functions
-- local g   = vim.g   -- global for let options
-- local o   = vim.o   -- global
-- local wo  = vim.wo  -- window local

local cmd = vim.cmd
local opt = vim.opt

cmd("colorscheme nord")
opt.termguicolors = true
opt.title = true
opt.spelllang = { "en" }
opt.wrap = false
opt.number= true
opt.relativenumber= true
opt.backspace = { "indent", "eol", "start" }
opt.encoding = "utf-8"
opt.fileencoding = "utf-8"
opt.cursorcolumn = true
opt.cursorline = true
cmd("au TextYankPost * lua vim.highlight.on_yank {on_visual = true}")
opt.tabstop = 4
opt.shiftwidth = 4
opt.softtabstop = 4
opt.autoindent = true
opt.breakindent = true
opt.expandtab = true
opt.shiftround = true
opt.smartindent = true
opt.smarttab = true
opt.timeout = false
opt.timeoutlen = 10
opt.updatetime = 300
opt.splitbelow = true
opt.splitright = true
opt.undofile = true
opt.swapfile = false
opt.foldenable = false
opt.foldmethod = "indent"
opt.hlsearch = true
opt.ignorecase = true
opt.incsearch = true
opt.smartcase = true
opt.scrolloff = 7
opt.sidescrolloff = 7
opt.completeopt = "menu,menuone,noselect"
opt.wildmenu = true
opt.lazyredraw = true
opt.mouse = 'a'
opt.showmatch = true
opt.clipboard = "unnamedplus"      
opt.list = true
opt.listchars = { trail = '.' }
-- opt.signcolumn = "yes:1"

