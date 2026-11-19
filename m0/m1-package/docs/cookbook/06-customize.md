# 6. Customize Coot: toolbar, menus, keys, colours, preferences

Put the lines you want every time into a startup file (recipe 6.8). In coot0 the windows, menus and toolbar
are made by Python, so buttons and menus are added with Python functions; from Scheme you call them with
`run-python-script` (the Scheme GUI library of the original Coot is not part of coot0).
`run-python-command` evaluates one Python expression and returns its value; for several lines, write them to a
`.py` file and run it with `run-python-script`, as below.

### 6.1 A toolbar button that runs your code

The function runs when the button is pressed. Here: refine the residue at the centre of the screen and its neighbours.

```python
def refine_here():
    ar = active_residue()                       # [imol, chain, resno, ins, atom, alt] of the residue in the centre
    if ar:
        imol, spec = ar[0], [ar[1], ar[2], ar[3]]
        refine_residues(imol, [spec] + residues_near_residue(imol, spec, 4.0))

coot_toolbar_button("Refine here", refine_here, tooltip="Sphere refine around the centre")
```

```scheme
(call-with-output-file "my-button.py"
  (lambda (port) (display "
def refine_here():
    ar = active_residue()
    if ar:
        imol, spec = ar[0], [ar[1], ar[2], ar[3]]
        refine_residues(imol, [spec] + residues_near_residue(imol, spec, 4.0))
coot_toolbar_button('Refine here', refine_here, tooltip='Sphere refine around the centre')
" port)))
(run-python-script "my-button.py")
```
<!-- check-py: "Refine here" in [b[0] for b in toolbar_label_list()] -->
<!-- check-scm: (if (member "Refine here" (map car (run-python-command "toolbar_label_list()"))) #t #f) -->

### 6.2 A menu of your own

A new menu "My tools" in the menu bar with two entries.

```python
menu = coot_menubar_menu("My tools")
add_simple_coot_menu_menuitem(menu, "Go to A41", lambda item: set_go_to_atom_chain_residue_atom_name("A", 41, " CA "))
add_simple_coot_menu_menuitem(menu, "White background", lambda item: set_background_colour(1, 1, 1))
```

```scheme
(call-with-output-file "my-menu.py"
  (lambda (port) (display "
menu = coot_menubar_menu('My tools')
add_simple_coot_menu_menuitem(menu, 'Go to A41', lambda item: set_go_to_atom_chain_residue_atom_name('A', 41, ' CA '))
add_simple_coot_menu_menuitem(menu, 'White background', lambda item: set_background_colour(1, 1, 1))
" port)))
(run-python-script "my-menu.py")
```
<!-- check-scm: (if (member "My tools" (run-python-command "[m.get_children()[0].get_text() for m in __import__('coot_python').main_menubar().get_children() if m.get_children()]")) #t #f) -->
<!-- check-py: len(menu.get_children()) >= 2 -->

### 6.3 A key that runs your code

Press `F5` in the graphics window to refine 3 residues on each side of the centre.
(Use `"Control_r"` for Ctrl-R. Keys that Coot already uses cannot be taken.)

```python
def refine_triple():
    ar = active_residue()
    if ar:
        refine_zone(ar[0], ar[1], ar[2] - 3, ar[2] + 3, ar[5])

add_key_binding("Refine 7 residues", "F5", refine_triple)
```

```scheme
(add-key-binding "Refine 7 residues" "F5"
  (lambda ()
    (let ((ar (active-residue)))
      (if ar (refine-zone (list-ref ar 0) (list-ref ar 1) (- (list-ref ar 2) 3) (+ (list-ref ar 2) 3) (list-ref ar 5))))))
```
<!-- check-py: "Refine 7 residues" in [k[2] for k in key_bindings] -->
<!-- check-scm: (if (assoc (key-sym-code "F5") *key-bindings*) #t #f) -->

### 6.4 Colours: map, background, symmetry

Red, green, blue from 0 to 1. The map colour can only be set while Coot has its window (it is not run in the automatic test).

```python
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_map_colour(imol_map, 0.3, 0.6, 1.0)     # light blue map
set_background_colour(1.0, 1.0, 1.0)        # white background
set_symmetry_colour(0.8, 0.8, 0.2)          # yellow symmetry copies
```

```scheme
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-map-colour imol-map 0.3 0.6 1.0)
(set-background-colour 1.0 1.0 1.0)
(set-symmetry-colour 0.8 0.8 0.2)
```
<!-- not-run: set_map_colour needs the graphics window (it stops Coot when there is none) -->

### 6.5 Thicker bonds, bigger labels, colour by chain

```python
imol = read_pdb("tutorial-modern.pdb")
set_bond_thickness(imol, 5)                 # default 3
set_font_size(3)                            # 1 small, 2 medium, 3 large
set_colour_by_chain(imol)
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(set-bond-thickness imol 5)
(set-font-size 3)
(set-colour-by-chain imol)
```

### 6.6 Messages for the user

A line in the status bar (bottom of the window), and a small window with a message.

```python
add_status_bar_text("Refinement finished")
info_dialog("Chain A: 93 residues checked, nothing found.")
```

```scheme
(add-status-bar-text "Refinement finished")
(info-dialog "Chain A: 93 residues checked, nothing found.")
```

### 6.7 Preferences you can set from a script

A few that people often change (all are remembered only for the session unless they are in a startup file):

```python
set_refinement_immediate_replacement(1)    # accept refinements without the "Accept?" window
set_map_radius(12)                          # draw maps 12 A around the centre
set_auto_recontour_map(1)                   # re-contour maps when the centre moves
set_smooth_scroll_flag(0)                   # jump instead of slide when going to an atom
set_default_bond_thickness(4)               # bond width of models read from now on
set_add_terminal_residue_do_post_refine(1)  # refine new terminal residues
```

```scheme
(set-refinement-immediate-replacement 1)
(set-map-radius 12)
(set-auto-recontour-map 1)
(set-smooth-scroll-flag 0)
(set-default-bond-thickness 4)
(set-add-terminal-residue-do-post-refine 1)
```
<!-- check-py: refinement_immediate_replacement_state() == 1 and get_auto_recontour_map() == 1 -->
<!-- check-scm: (= (refinement-immediate-replacement-state) 1) -->

### 6.8 Run your settings every time Coot starts

coot0 keeps its own home folder: `~/Library/Application Support/coot0/home/` (installed with `install.sh`; in a
folder you unpacked yourself it is `home/` inside that folder). Python and Scheme files in
`home/.coot-preferences/` are run at every start, in alphabetical order. This recipe writes such a file.

```python
import os
prefs = os.path.join(os.environ["HOME"], ".coot-preferences")
os.makedirs(prefs, exist_ok=True)
with open(os.path.join(prefs, "my-settings.py"), "w") as f:
    f.write("set_refinement_immediate_replacement(1)\n")
    f.write("set_map_radius(12)\n")
print("written to", prefs)
```

```scheme
(let ((prefs (string-append (getenv "HOME") "/.coot-preferences")))
  (if (not (file-exists? prefs)) (mkdir prefs))
  (call-with-output-file (string-append prefs "/my-settings.scm")
    (lambda (port)
      (display "(set-refinement-immediate-replacement 1)\n" port)
      (display "(set-map-radius 12)\n" port)))
  (format #t "written to ~a~%" prefs))
```
<!-- check-py: os.path.exists(os.path.join(os.environ["HOME"], ".coot-preferences", "my-settings.py")) -->
<!-- check-scm: (file-exists? (string-append (getenv "HOME") "/.coot-preferences/my-settings.scm")) -->

Inside Coot, `HOME` is coot0's own home folder (not your Mac home folder), so the file lands in the right place.
Delete the file to go back to the defaults.
