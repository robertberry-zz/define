;; Provides integration with StumpWM. Copy & paste this into .stumpwmrc file,
;; then C-t C-d will prompt for a word and display its definition.

(defun shell-command (command) "Run a shell command and display output to
screen.  This must be used in a functional side-effects-free style! If a
program does not exit of its own accord, Stumpwm might hang!"
       (check-type command string)
       (echo-string (current-screen) (run-shell-command command t)))

;; define a word
(defcommand dictionary-def (word) ((:string "Define word: "))
  (echo-string (current-screen)
               (run-shell-command
                (concatenate 'string "define.py " word) t)))

(define-key *root-map* (kbd "C-d") "dictionary-def")
