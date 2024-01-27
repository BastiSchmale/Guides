(tool-bar-mode -1)
(scroll-bar-mode -1)
(tooltip-mode -1)
(menu-bar-mode -1)

(setq-default
 confirm-kill-emacs 'y-or-n-p                        ; ask before quit
 fill-column 96                                      ; Set width for automatic line breaks
 ring-bell-function 'ignore                          ; Warning Sound ausschalten
 help-window-select t                                ; Focus new help windows when opened
 inhibit-startup-screen t                            ; Disable start-up screen
 initial-scratch-message ""                          ; Empty the initial *scratch* buffer
 load-prefer-newer t                                 ; Prefers the newest version of a file
 frame-title-format '(buffer-file-name "%f" ("%b"))  ; Full path in frame title
 select-enable-primary nil                           ; Dont automatically copy selected text
 select-enable-clipboard t                           ; Merge system's and Emacs' clipboard
 ac-auto-start t                                     ; auto-complete
 view-read-only t                                    ; Always open read-only buffers in view-mode
 )
(delete-selection-mode t)                            ; overwrite selected text

(set-frame-parameter (selected-frame) 'fullscreen 'maximized)
(add-to-list 'initial-frame-alist '(fullscreen . maximized))

(load-theme 'deeper-blue)

(setq use-file-dialog nil)
(setq use-dialog-box nil)

(set-face-attribute 'default nil :font "Ubuntu Mono" :height 112)
;; (set-face-attribute 'default nil :height 112)

(setq-default cursor-type 'bar)
(set-cursor-color "#ffffff")

(set-fringe-mode 8)

(set-default 'truncate-lines t)                      ; line break/wrap
(global-visual-line-mode 1)                          ; Wrap Lines at Word Boundary
(visual-line-mode 1)                                 ; enable Wrapping Lines

(column-number-mode)
(global-display-line-numbers-mode t)

(global-set-key (kbd "<escape>") 'keyboard-escape-quit)

(global-hl-line-mode 1)

(setq display-time-format "%H:%M (%Y-%m-%d)")
(display-time-mode 1)

(setq electric-pair-pairs '((?\{ . ?\}) (?\( . ?\)) (?\[ . ?\]) (?\" . ?\")))
(electric-pair-mode t)

(fset 'yes-or-no-p 'y-or-n-p)
