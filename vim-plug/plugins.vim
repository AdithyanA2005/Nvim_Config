call plug#begin('$HOME/.config/nvim/autoload/plugged')
    Plug 'morhetz/gruvbox'
    Plug 'mhinz/vim-startify'
    Plug 'preservim/nerdtree'
    Plug 'vim-airline/vim-airline'
    Plug 'jiangmiao/auto-pairs'
    Plug 'octol/vim-cpp-enhanced-highlight'
    Plug 'mhinz/vim-signify'
    Plug 'tpope/vim-unimpaired'
    Plug 'liuchengxu/vim-which-key'
    Plug 'ryanoasis/vim-devicons'
    Plug 'tpope/vim-commentary'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'honza/vim-snippets'
    Plug 'joshdick/onedark.vim'
    Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
    Plug 'junegunn/rainbow_parentheses.vim'
call plug#end()

" Automatically install missing plugins on startup
autocmd VimEnter *
  \  if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \|   PlugInstall --sync | q
  \| endif
