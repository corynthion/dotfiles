return {
    { -- LSP Configuration & Plugins
      'neovim/nvim-lspconfig',
      dependencies = {
        'williamboman/mason.nvim',
        'williamboman/mason-lspconfig.nvim',
        { 'j-hui/fidget.nvim', opts = {} },
        'folke/neodev.nvim',
      },
    },
  { -- Autocompletion
    'hrsh7th/nvim-cmp',
    dependencies = { 'hrsh7th/cmp-nvim-lsp', 'L3MON4D3/LuaSnip', 'saadparwaiz1/cmp_luasnip' },
  },
  {
	"windwp/nvim-autopairs",
  	config = function() require("nvim-autopairs").setup {} end
  }
}
