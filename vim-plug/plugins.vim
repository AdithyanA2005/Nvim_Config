call plug#begin('$HOME/AppData/Local/nvim/autoload/plugged')
	Plug 'voldikss/vim-floaterm'
    Plug 'airblade/vim-gitgutter'                                                   " This will show specific symbols based on git in the side of the screen
    Plug 'tpope/vim-fugitive'
    Plug 'tpope/vim-rhubarb'
    Plug 'junegunn/gv.vim'   
    Plug 'morhetz/gruvbox'
    Plug 'mhinz/vim-startify'
    Plug 'preservim/nerdtree'
    Plug 'vim-airline/vim-airline'
    Plug 'jiangmiao/auto-pairs'
    Plug 'octol/vim-cpp-enhanced-highlight'
    Plug 'tpope/vim-unimpaired'
    Plug 'liuchengxu/vim-which-key'
    Plug 'ryanoasis/vim-devicons'
    Plug 'tpope/vim-commentary'                                                     " This is to comment lines 
    Plug 'dNitro/vim-pug-complete', { 'for': ['jade', 'pug'] }                      " This is for Pug autocompletion
    Plug 'digitaltoad/vim-pug',                                                     " This is pug Syntax Hyliting
    Plug 'neoclide/coc.nvim', {'branch': 'release'}                                 " This is for coc
    Plug 'honza/vim-snippets'                                                       " This is for Snippetes
    Plug 'joshdick/onedark.vim'
    Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
    Plug 'junegunn/rainbow_parentheses.vim'
call plug#end()

" Automatically install missing plugins on startup
autocmd VimEnter *
  \  if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \|   PlugInstall --sync | q
  \| endif
