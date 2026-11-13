# Coot bundle: runtime closure inventory (step 1)

Source: `m0/tools/bundle_inventory.py` on `coot-bin` (build 3) + canvas libraries; environment `coot-deps`. Raw data: `bundle_inventory.json`.

| Item | Result |
|---|---|
| Static dylib closure (otool, @rpath resolved) | 72 libraries (same as the M0 measurement), 3 of them the canvas libraries |
| Further libraries needed only by run-time-loaded modules | 17 more, so 89 libraries in total (119.7 MB) |
| Run-time-loaded module files (dlopen), listed separately from the 89 | 106: 12 gdk-pixbuf loaders, 17 GTK2 modules/engines/input methods, 76 Python extension modules, 1 Guile extension (their own dependencies are inside the 89) |
| Needed from outside the conda env | only the 3 canvas libraries (`canvas/prefix/lib`) |
| rpaths in `coot-bin` | the conda `lib` directory and `./canvas/prefix/lib` (relative to the build directory): both must go |
| Unresolved | 1, and harmless: the SVG pixbuf loader's own install name is a CI build path; it matters only at link time |

## Resource trees (MB)

python stdlib 53.1 (prune tests/tkinter/idle), Guile compiled modules `lib/guile` 50.0 (keep: without them Guile recompiles its core modules on first start) and `share/guile` 5.3, icons 13.0 (Adwaita + hicolor), GTK modules 1.7, pixbuf loaders 1.0, `ssl` 0.3, fontconfig data 0.1. `share/locale` is 38.1 MB of translations and is left out (English only).

## Files with the absolute conda prefix baked in (161 files)

| Category | Files | What it controls | Handled by |
|---|---|---|---|
| `lib/pkgconfig/*.pc` | 122 | build-time only | not shipped |
| `libguile-3.0.1.dylib` | 1 (23 strings) | `%load-path`, extensions path, compiled path | `GUILE_SYSTEM_PATH`, `GUILE_LOAD_PATH`, `GUILE_SYSTEM_COMPILED_PATH`, `GUILE_SYSTEM_EXTENSIONS_PATH` in the launcher; verify in the relocated copy |
| `libgtk-quartz-2.0`, 11 `gtk-2.0` immodules | 12 | data prefix, module dirs, locale dir, input-method file | `GTK_EXE_PREFIX`, `GTK_DATA_PREFIX`, `GTK_PATH`; empty `GTK_IM_MODULE_FILE` generated at first run |
| `libglib`, `libgio` | 2 | XDG fallbacks, GIO module dir | `GSETTINGS_SCHEMA_DIR`, `XDG_DATA_DIRS`, `GIO_MODULE_DIR` |
| `libpango`, `libfontconfig` | 2 | sysconf/lib dirs, fontconfig config | `PANGO_LIBDIR`, `PANGO_SYSCONFDIR`, a `fonts.conf` generated at first run |
| `gdk-pixbuf` `loaders.cache` | 1 (text) | absolute loader paths | regenerated at first run with the bundled `gdk-pixbuf-query-loaders` |
| `libcrypto`, `libcurl`, `libkrb5`, `libgssapi_krb5` | 4 | OpenSSL dir, CA bundle path, Kerberos config | Coot's own downloads disable certificate verification (`c-interface-network.cc` lines 105 and 169), so the baked CA path is unused there; Python's `urllib` needs `SSL_CERT_FILE` pointing at the shipped `cacert.pem` |
| `libpython3.11` and 3 text files in `lib/python3.11` | 4 | `sys.prefix`, build config | `PYTHONHOME`; the text files are build-time only |
| `libintl`, `libccp4c`, `libxml2` | 3 | locale dir, CCP4 dirs, XML catalog | not used at run time by Coot (English only); `CLIBD_MON` is set by the launcher |
| `libtcl`, `libncurses*`, `libtinfo*`, `libtk` | 5 | only needed by `_tkinter` and `_curses` | dropped together with those two Python modules |

## Decisions that follow

1. Bundle the 3 canvas libs, the dependency closure above minus the Tcl/Tk and curses chain, the 12 + 17 modules, the Python stdlib without tests/tkinter/idle/curses/dbm, the Guile trees, schemas, icons, `ssl/cacert.pem`.
2. Every baked path is neutralised by an environment variable set in the launcher or by a cache regenerated at first run: no binary patching of strings.
3. Keep `_ctypes` (and libffi): the Python GTK compatibility layer in phase 2 is built on it.
