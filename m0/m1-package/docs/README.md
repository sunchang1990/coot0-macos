# coot0 documentation

- [Cookbook](cookbook/README.md): about 85 short recipes for everyday tasks (files and maps, the view, selections,
  refinement, editing, customizing the toolbar/menus/keys, batch scripts and hooks, validation, NCS, ligands),
  each in Python and in Scheme, all tested.
- [Scripting reference](api/README.md): every Python and Scheme function of Coot 0.9.8.96 (about 1,700), with a
  concrete example on the test data and the result of trying it.
  - [All functions A-Z](api/A-Z.md)
  - [Functions in only one language](api/one-language-only.md)

In coot0 (build 28 or later): **Help > Search Menus and Docs...** finds menu entries (and runs the one you pick), cookbook recipes,
scripting functions and documentation sections (they open in your web browser); **Help > Keyboard Shortcuts...** lists Coot's keys
and your own key bindings. These pages are also in `docs/html/` of the package.

Where to type commands: Calculate > Scripting > Python... or Scheme... (both show the command, what it printed,
the result and errors). A whole file: Calculate > Run Script..., or `coot0 --script my-file.py` in a Terminal.

Coot's own documentation (user manual, tutorials) is at https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ ;
its scripting part describes Coot 0.9 as well.
