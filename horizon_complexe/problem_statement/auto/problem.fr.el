(TeX-add-style-hook
 "problem.fr"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "tikz"))
 :latex)

