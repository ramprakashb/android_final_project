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
Plug 'tpope/vim-markdown'
" ------------------
Plug 'dense-analysis/ale'
" ------------------
Plug 'rmagatti/auto-session'
" ------------------
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
" ------------------
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
" ------------------
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' }
"-------------------
Plug 'p00f/nvim-ts-rainbow'
" ------------------
Plug 'sonph/onehalf', { 'rtp': 'vim' }
Plug 'vim-airline/vim-airline-themes'
let g:airline_theme='onehalfdark'
" ------------------
Plug 'vim-scripts/bash-support.vim'
"-------------------
Plug 'nathanaelkane/vim-indent-guides'
let g:indent_guides_enable_on_vim_startup = 1
let g:indent_guides_guide_size = 1
let g:indent_guides_auto_colors = 0
autocmd VimEnter,Colorscheme * :hi IndentGuidesOdd  guibg=blue   ctermbg=1
autocmd VimEnter,Colorscheme * :hi IndentGuidesEven guibg=yellow ctermbg=1

"-------------------
let g:ale_sign_error = 'E'
"-------------------
let g:ale_sign_warning = 'W'
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
call plug#end()
" Plugin section ends here
" ------------------

" Other settings go here
" ------------------
if exists('+termguicolors')
  let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
  let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"
  set termguicolors
endif

syntax on
set t_Co=256
set cursorline
colorscheme onehalfdark
let g:airline_theme='onehalfdark'

set number
retab!
set expandtab
set list
set listchars=trail:·
set tabstop=2
set shiftwidth=2
set softtabstop=2
filetype plugin on
set autoindent
setlocal spell spelllang=en_us
set textwidth=79
set syntax=whitespace
set syntax=json
set syntax=python
set syntax=java

au Syntax *.py runtime! syntax/python.vim
au Syntax *.java runtime! syntax/java.vim
au Syntax *.json runtime! syntax/json.vim

function! Preserve()
  " Preparation: save last search, and cursor position.
  let _s=@/
  let l = line(".")
  let c = col(".")
  " Do the business:
  %s/\\s\\+$//e
  %s/\s*$//g
  normal! gg=G
  " Clean up: restore previous search history, and cursor position
  let @/=_s
  call cursor(l, c)
endfunction

autocmd BufWritePre * :call Preserve()
autocmd BufWritePre *.java %google-java-format
autocmd BufWritePre *.py %yapf --style google -i
