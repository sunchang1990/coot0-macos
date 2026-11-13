Splash pictures of the macOS build (made by ../make_splash.py from the original share/coot/pixmaps/coot-0.9.8.96.png, 580 x 478 px)

  coot-0.9.8.96.png    580 x 478 px   same size as the original; tagline "Good to see you, Old Coot" instead of "Goodbye Old Coot".
                                      Used by Coot's own start-up window (GTK 2 draws 1 picture pixel as 1 point).
  coot-splash@2x.png  1160 x 956 px   high-resolution version shown by bin/coot-splash (compat/splash/coot-splash.m) at 580 x 478 points,
                                      i.e. one picture pixel per screen pixel on a Retina display.
  OpenSansItalic.ttf                  font of the new tagline (Open Sans, Apache License 2.0, Google / Steve Matteson)

Regenerate (the original picture is in the Coot 0.9.8.96 source tree):
  python ../make_splash.py <coot-src>/pixmaps/coot-0.9.8.96.png <outdir> "Good to see you, Old Coot" OpenSansItalic.ttf
The painting itself only has 580 x 478 pixels of detail; the 2x version is a clean enlargement with crisp text, not new detail.
A larger original of the artwork would give a sharper result with the same script.
