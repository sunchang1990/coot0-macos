// Offline check of compat/gl-seam/coot-label-raster.h: rasterise labels to PGM files.  usage: label_raster_test OUTDIR
#include "coot-label-raster.h"
#include <cstdio>
int main(int argc, char **argv) {
   const char *dir = argc > 1 ? argv[1] : ".";
   const char *labels[] = { "CA", "A 123 ASP OD1", "3.12", "H-bond 2.87 \xc3\x85", "O3'" };
   double sizes[] = { 12.0 * 1.4, 12.0 * 1.4 * 2.0 };
   for (double px : sizes) for (int i = 0; i < 5; i++) {
      coot_label_bitmap b;
      if (!coot_label_rasterize(labels[i], (double)(int)(px + 0.5), b)) { printf("FAIL %s\n", labels[i]); return 1; }
      int nz = 0; for (int y = 0; y < b.h; y++) for (int x = 0; x < b.w; x++) if (b.a8[(size_t)y * b.stride + x]) nz++;
      printf("px=%d '%s' -> %dx%d baseline=%d ink_pixels=%d\n", (int)(px + 0.5), labels[i], b.w, b.h, b.baseline, nz);
      char fn[512]; snprintf(fn, sizeof fn, "%s/lab_%d_%d.pgm", dir, (int)(px + 0.5), i);
      FILE *f = fopen(fn, "wb"); fprintf(f, "P5\n%d %d\n255\n", b.w, b.h);
      for (int y = 0; y < b.h; y++) fwrite(&b.a8[(size_t)y * b.stride], 1, b.w, f);
      fclose(f);
   }
   return 0;
}
