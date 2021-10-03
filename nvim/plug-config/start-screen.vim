let g:startify_custom_header = [
        \ '  _______________________________________________________________________________________________________  ' ,
        \ ' │                                                                                                       │ ' ,
        \ ' │                                                                                                       │ ' ,
        \ ' │       _____________________________________          ________________________________________         │ ' , 
        \ ' │                                                                                                       │ ' ,
        \ ' │        __   __         ______          __      ||    Hello Adithya!!                                  │ ' ,
        \ ' │       | |  / / __     / ____/___  ____/ /__    ||    Welcome back to your fully customised IDE        │ ' ,
        \ ' │       | | / / / /    / /   / __ \/ __  / _ \   ||            -------------------------                │ ' ,
        \ ' │       | |/ / / / == / /___/ /_/ / /_/ /  __/   ||    SMART-PEOPLE => SMART-IDE                        │ ' ,
        \ ' │       \___/ /_/     \____/\____/\__,_/\___/    ||    What is the wish Master ADI!!!                   │ ' ,
        \ ' │                                                                                                       │ ' ,
        \ ' │       _____________________________________          ________________________________________         │ ' , 
        \ ' │                                                                                                       │ ' , 
        \ ' │                                                                                                       │ ' , 
        \ ' │                                                                                                       │ ' , 
        \ ' │_______________________________________________________________________________________________________│ ' ,
        \ '                                                                                                           ' ,
        \]

" let g:startify_session_autoload = 1
" let g:startify_session_delete_buffers = 1
" let g:startify_session_dir = '~/OneDrive/Documents/Coding/'
let g:startify_session_dir = '~/AppData\Local/nvim/session'
let g:startify_change_to_vcs_root = 1
let g:startify_enable_special = 0
let g:webdevicons_enable_startify = 1
let g:startify_fortune_use_unicode = 1
let g:startify_session_persistence = 1
let g:startify_lists = [
          \ { 'type': 'bookmarks', 'header': ['   Bookmarks']                    },
          \ { 'type': 'sessions',  'header': ['   Sessions']                     },
          \ { 'type': 'files',     'header': ['   Files']                        },
          \ { 'type': 'dir',       'header': ['   Current Directory '. getcwd()] },
          \ ]

let g:startify_bookmarks = [
            \ { 'ss': '~/AppData/Local/nvim/plug-config/start-screen.vim' },
            \ ]
function! StartifyEntryFormat()
        return 'WebDevIconsGetFileTypeSymbol(absolute_path) ." ". entry_path'
endfunction


