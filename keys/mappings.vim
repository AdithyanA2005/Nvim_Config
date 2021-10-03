" Use alt + hjkl to resize windows size
nnoremap <M-j>    :resize -2<CR>
nnoremap <M-k>    :resize +2<CR>
nnoremap <M-h>    :vertical resize +2<CR>
nnoremap <M-l>    :vertical resize -2<CR>


" Pressing the Keyboard shortcut j + k will enter <ESC>
inoremap kj <Esc>
inoremap jk <Esc>


" TAB key in normal mode will change buffer tabs(opened files) 
nnoremap <silent> <TAB> :bnext<CR>


" K to move a line up and J to move down when selected
xnoremap K :move '<-2<CR>gv-gv
xnoremap J :move '>+1<CR>gv-gv


" Terminal window navigation
tnoremap <C-h> <C-\><C-N><C-w>h
tnoremap <C-j> <C-\><C-N><C-w>j
tnoremap <C-k> <C-\><C-N><C-w>k
tnoremap <C-l> <C-\><C-N><C-w>l
inoremap <C-h> <C-\><C-N><C-w>h
inoremap <C-j> <C-\><C-N><C-w>j
inoremap <C-k> <C-\><C-N><C-w>k
inoremap <C-l> <C-\><C-N><C-w>l
tnoremap <Esc> <C-\><C-n>


" Redraw the screen and clear any search terms
noremap <silent> <c-n> :nohls<cr><c-l>


" Better window navigation
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l


" Ctrl + u will capitalise entire word
inoremap <c-u> <ESC>viwUi
nnoremap <c-u> viwU<Esc>


" Can select Blocks Of Code which was selected earler with g + v  
vnoremap < <gv
vnoremap > >gv
