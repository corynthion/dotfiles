local fn = vim.fn
local cmd = vim.cmd
local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'

if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({
    "git",
    "clone",
    "--depth",
    "1",
    "https://github.com/wbthomason/packer.nvim",
    install_path,
  })
end

cmd("packadd packer.nvim")

function get_config(name)
  return string.format('require("config/%s")', name)
end

return require("packer").startup({
  function(use)
    use("wbthomason/packer.nvim")
    use({ "arcticicestudio/nord-vim" })
    use({ "kyazdani42/nvim-web-devicons" })
    use({
      "nvim-lualine/lualine.nvim",
      config = get_config("lualine"),
      event = "VimEnter",
      requires = { "kyazdani42/nvim-web-devicons", opt = true },
    })
    use({
      "windwp/nvim-autopairs",
      -- after = "nvim-cmp",
      config = get_config("autopairs"),
    })
    if packer_bootstrap then
      require("packer").sync()
    end
  end
})
