-----------------------------------------------
-- plugins.bak.lua
-----------------------------------------------
vim.cmd([[
  augroup packer_user_config
    autocmd!
    autocmd BufWritePost plugins.lua source <afile> | PackerCompile
  augroup end
]])

use({ "nathom/filetype.nvim", config = get_setup("filetype") })

use({
  "folke/zen-mode.nvim",
  config = get_setup("zen-mode"),
})

use({
  "norcalli/nvim-colorizer.lua",
  event = "BufReadPre",
  config = get_setup("colorizer"),
})

use({
  "nvim-treesitter/nvim-treesitter",
  config = get_setup("treesitter"),
  run = ":TSUpdate",
})

use("nvim-treesitter/nvim-treesitter-textobjects")

use({
  "hrsh7th/nvim-cmp",
  requires = {
    { "hrsh7th/cmp-nvim-lsp" },
    { "hrsh7th/cmp-nvim-lua" },
    { "hrsh7th/cmp-buffer" },
    { "hrsh7th/cmp-path" },
    { "hrsh7th/cmp-cmdline" },
    { "hrsh7th/vim-vsnip" },
    { "hrsh7th/cmp-vsnip" },
    { "hrsh7th/vim-vsnip-integ" },
    { "f3fora/cmp-spell" },
    { "octaltree/cmp-look" },
    { "hrsh7th/cmp-calc" },
    { "hrsh7th/cmp-emoji" },
  },
  config = get_setup("cmp"),
})

use({ "kyazdani42/nvim-tree.lua", config = get_setup("tree") })

use({
  "lewis6991/gitsigns.nvim",
  requires = { "nvim-lua/plenary.nvim" },
  event = "BufReadPre",
  config = get_setup("gitsigns"),
})

use("p00f/nvim-ts-rainbow")

use({ "jose-elias-alvarez/null-ls.nvim", config = get_setup("null-ls") })

use({ "neovim/nvim-lspconfig", config = get_setup("lsp") })

use({
  "numToStr/Comment.nvim",
  opt = true,
  keys = { "gc", "gcc" },
  config = get_setup("comment"),
})

use({
  "nvim-telescope/telescope.nvim",
  module = "telescope",
  cmd = "Telescope",
  requires = {
    { "nvim-lua/popup.nvim" },
    { "nvim-lua/plenary.nvim" },
    { "nvim-telescope/telescope-fzf-native.nvim", run = "make" },
  },
  config = get_setup("telescope"),
})
use({ "nvim-telescope/telescope-file-browser.nvim" })

use({ "onsails/lspkind-nvim", requires = { { "famiu/bufdelete.nvim" } } })

use({ "tpope/vim-repeat" })

use({ "tpope/vim-surround" })

use({ "wellle/targets.vim" })

use({
  "phaazon/hop.nvim",
  event = "BufReadPre",
  config = get_setup("hop"),
})

use({
  "rmagatti/session-lens",
  requires = { "rmagatti/auto-session", "nvim-telescope/telescope.nvim" },
  config = get_setup("session"),
})

use({ "windwp/nvim-ts-autotag" })

use({
  "winston0410/range-highlight.nvim",
  requires = { { "winston0410/cmd-parser.nvim" } },
  config = get_setup("range-highlight"),
})

use({ "filipdutescu/renamer.nvim", config = get_setup("renamer") })

use({ "goolord/alpha-nvim", config = get_setup("alpha") })

use({ "luukvbaal/stabilize.nvim", config = get_setup("stabilize") })

use({
  "simrat39/symbols-outline.nvim",
  cmd = { "SymbolsOutline" },
  setup = get_setup("outline"),
})
