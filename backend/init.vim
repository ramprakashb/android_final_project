" ~/neovim/plugged is where the plugins are
" getting installed
" Plugin section starts
" -------------------------------------------
call plug#begin('~/neovim/plugged')
" On-demand loading
" plugin provides mappings to easily delete, change
" and add such surroundings in pairs.
" --------------------
Plug 'tpope/vim-surround'
" ------------------
Plug '~/projects/vim-python-magic'
" ------------------
Plug 'tomasiser/vim-code-dark'
" ------------------
Plug 'tpope/vim-markdown'
" ------------------
Plug 'dense-analysis/ale'
" ------------------
Plug 'rmagatti/auto-session'
" ------------------
Plug 'luochen1990/rainbow'
" ------------------
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
" ------------------
Plug 'norcalli/nvim-colorizer.lua'
" ------------------
Plug 'google/vim-maktaba'
" ------------------
Plug 'google/vim-codefmt'
" ------------------
Plug 'google/vim-glaive'
" ------------------
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
" ------------------
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
" ------------------
Plug 'google/yapf'
"-------------------
Plug 'google/vim-maktaba'
"-------------------
Plug 'google/vim-codefmt'
"-------------------
Plug 'p00f/nvim-ts-rainbow'
"-------------------
Plug 'vim-airline/vim-airline'
"-------------------
Plug 'vim-airline/vim-airline-themes'
"-------------------
Plug 'google/google-java-format'
"-------------------
Plug 'eclipse/eclipse.jdt.ls'
"-------------------
let g:ale_sign_error = '!!'
"-------------------
let g:ale_sign_warning = '??'
"-------------------
let g:ale_floating_window_border = ['│', '─', '╭', '╮', '╯', '╰']
"-------------------
let g:auto_save = 1
"-------------------
let g:rainbow_active = 1 "set to 0 if you want to enable it later via :RainbowToggle
"-------------------
let g:ale_set_highlights = 1
"-------------------
let g:ale_echo_msg_format = '%linter%: %s'
"-------------------
let g:ale_linters = {
            \   'python': ['flake8', 'pyflakes'],
            \}
let g:ale_completion_autoimport = 1
"-------------------
let g:ale_javascript_prettier_use_global = 1
"-------------------
let g:ale_fixers = {
            \   'python': ['isort', 'black'],
            \}
let g:ale_fix_on_save = 1
"-------------------
let g:ale_lint_on_text_changed = 1
"-------------------
let g:ale_echo_msg_error_str = 'E'
"-------------------
let g:ale_echo_msg_warning_str = 'W'
"-------------------
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'
"-------------------
let g:airline#extensions#ale#enabled = 1
"-------------------
let g:airline_theme='simple'
"-------------------

call plug#end()
" Plugin section ends here
" ------------------

" Other settings go here
" ------------------
set termguicolors t_Co=256
syntax enable
set number
set expandtab
set tabstop=4
set shiftwidth=2
set softtabstop=2
setlocal cursorline
filetype plugin on
set textwidth=79
augroup fmt
    autocmd!
    autocmd BufWritePre *.java AutoFormatBuffer google-java-format
    autocmd BufWritePre *.py AutoFormatBuffer black
    autocmd BufWritePre * %s/\s\+$//e

augroup END
