---
title: "nvim配置总结"
excerpt: "本文总结了常用的nvim配置，持续更新中。。。"
mathjax: false
tags: "新文章在写"
---

## 什么是Nvim
Neovim是一个社区驱动的开源项目，是Vim文本编辑器的一个分叉版本，它的构建使Vim更容易为核心开发人员维护。 它是Vim文本编辑器的一个增强的开箱即用版本，或者您可以说，它是一个更简化的Vim，它使得集成比使用Vim容易得多。 Vim已经是最受欢迎的文本编辑器，也是程序员选择的文本编辑器。

### 安装和卸载
参加官方的安装教程：安装。在使用vim相关的内容时，可以参考博客，但博客的水平参差不齐，最终应该以官方的指导为标准。
卸载：

```bash
sudo apt remove neovim
sudo apt remove neovim-runtime
```
升级的话，可以先卸载再安装新版本。。。。。（目前还没找到其他方法）

### 配置

**预备**
不预备也可以看下面的内容，看不懂了，可以回来看看预备内容。
- Ctrl 键对应 <c>
- 空格 键对应 <space>
- alt 键对应 <a> 或者 <m>
- esc 键对应 <esc>
- 退格键对应 <bs>
- 回车键对应 <cr>
- shift 键对应 <shift>
- f1 到 f12 对应 <f1> 到 <f12>
- <leader>表示前缀建。可以通过：let mapleader=''进行设置
这些功能键与普通字母做配合时，将字母键放入到 <> 中，并以 - 和 功能键做分割，比如说 :map <c-d> dd 来将 <Ctrl +d> 映射为 dd。当然有时候为了可读性，我们可以将这些功能键以大写字母来表示，例如 <C-d> 就表示 <Ctrl +d>

### init.vim
基本的配置写在这个文件里面。位置在`~/.config/nvim/init.vim`，如果没有这个文件的话，可以创建一个。
下面的是我的init.vim的配置：
```bash
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" write plug you want to install here
"    content in #begin() i.e. '~/.vim/plugged' is position of you plugin
"    Plug 'github_username/repo_name'  use this format to install plug
"    The detail about plug can be found in github repo. read! read! read!
"    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

call plug#begin('~/.vim/plugged')
let g:plug_url_format = 'git@github.com:%s.git'  " high speed clone when you install plug

Plug 'crusoexia/vim-monokai'    " theme
Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'honza/vim-snippets'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'octol/vim-cpp-enhanced-highlight'
Plug 'tomasr/molokai'
Plug 'joshdick/onedark.vim'

call plug#end()


""""""""""""""""""""""""""""""""""""""""
" basic config
""""""""""""""""""""""""""""""""""""""""
syntax on
colo monokai " onedark molokai 
set nu
set rnu
set ts=4
" set tw=4  " which lead to auto change line in complete
inoremap ' ''<ESC>i
inoremap " ""<ESC>i
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {<CR>}<ESC>O


""""""""""""""""""""""""""""""""""""""""
" nerdtree config
""""""""""""""""""""""""""""""""""""""""

" autocmd vimenter * NERDTree  "自动开启Nerdtree
let g:NERDTreeWinSize = 25 "设定 NERDTree 视窗大小
let NERDTreeShowBookmarks=1  " 开启Nerdtree时自动显示Bookmarks
"打开vim时如果没有文件自动打开NERDTree
" autocmd vimenter * if !argc()|NERDTree|endif

"当NERDTree为剩下的唯一窗口时自动关闭
" autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" 设置树的显示图标
let g:NERDTreeDirArrowExpandable = '+'
let g:NERDTreeDirArrowCollapsible = '-'
let NERDTreeIgnore = ['\.pyc$']  " 过滤所有.pyc文件不显示
let g:NERDTreeShowLineNumbers=0 " 是否显示行号
let g:NERDTreeHidden=1     "不显示隐藏文件
""Making it prettier
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1
nnoremap <t+t> :NERDTreeToggle<CR> " 开启/关闭nerdtree快捷键



""""""""""""""""""""""""""""""""""""""""
" coc config
""""""""""""""""""""""""""""""""""""""""

" if hidden is not set, TextEdit might fail.
set hidden
" Some servers have issues with backup files, see #649
set nobackup
set nowritebackup

" You will have bad experience for diagnostic messages when it's default 4000.
set updatetime=200

" don't give |ins-completion-menu| messages.
set shortmess+=c

" always show signcolumns
set signcolumn=yes

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
inoremap <silent><expr> <TAB>
\ pumvisible() ? "\<C-n>" :
\ <SID>check_back_space() ? "\<TAB>" :
\ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
let col = col('.') - 1
return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
inoremap <silent><expr> <c-space> coc#refresh()

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current position.
" Coc only does snippet and additional edit on confirm.
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
" Or use `complete_info` if your vim support it, like:
" inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"

" Use `[g` and `]g` to navigate diagnostics
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)
" Remap keys for gotos
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" Use K to show documentation in preview window
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
if (index(['vim','help'], &filetype) >= 0)
execute 'h '.expand('<cword>')
else
call CocAction('doHover')
endif
endfunction

" Highlight symbol under cursor on CursorHold
" autocmd CursorHold * silent call CocActionAsync('highlight')

" Remap for rename current word
nmap <leader>rn <Plug>(coc-rename)

" Remap for format selected region
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

augroup mygroup
autocmd!
" Setup formatexpr specified filetype(s).
" autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
" Update signature help on jump placeholder
" autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
augroup end

" Remap for do codeAction of selected region, ex: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)

" Remap for do codeAction of current line
nmap <leader>ac  <Plug>(coc-codeaction)
" Fix autofix problem of current line
nmap <leader>qf  <Plug>(coc-fix-current)

" Create mappings for function text object, requires document symbols feature of languageserver.
xmap if <Plug>(coc-funcobj-i)
xmap af <Plug>(coc-funcobj-a)
omap if <Plug>(coc-funcobj-i)
omap af <Plug>(coc-funcobj-a)

" Use `:Format` to format current buffer
command! -nargs=0 Format :call CocAction('format')

" Use `:Fold` to fold current buffer
command! -nargs=? Fold :call     CocAction('fold', <f-args>)

" use `:OR` for organize import of current buffer
command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')
```

### Coc
coc. nvim 是一个补全插件，它可以补全很多东西，比如：函数、变量、关键字、文件名、路径、标签、颜色、emoji 等等。 来禁用掉切换时的插入，或者禁用插件监听CompleteDone 事件的行为。 copilot.vim 提供选项时，无法使用tab 切换。
对于python的支持，要现在虚拟环境中安装pynvim：`pip install pynvim`
常用的coc补全：
```bash
:CocInstall coc-clangd  # C++环境插件
:CocInstall coc-cmake  # Cmake 支持
:CocInstall coc-git    # git 支持
:CocInstall coc-highlight  # 高亮支持
:CocInstall coc-jedi   # jedi python系列使用
:CocInstall coc-json   # json 文件支持
:CocInstall coc-sh     # bash 环境支持
:CocInstall coc-snippets # python提供 snippets
:CocInstall coc-vimlsp # lsp
:CocInstall coc-yaml   # yaml
:CocInstall coc-syntax
```

## 参考
- <a href='https://www.cnblogs.com/cniwoq/p/13272746.html#3-cocnvim-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE'>Neovim+Coc.nvim配置 目前个人最舒服终端编辑环境(Python&C++)</a>
- <a href='https://phoenixnap.com/kb/update-node-js-version'>Nodejs更新的方法</a>
- <a href='https://blog.csdn.net/SteveForever/article/details/124896792'>升级nvim的一种方法</a>