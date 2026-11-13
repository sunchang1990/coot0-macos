
// Headless verification of arm64 libart_lgpl / libgnomecanvas / goocanvas 1.x built for GTK2-Quartz.
// No window server in this sandbox -> exercise everything that does not need a display.
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gtk/gtk.h>
#include <libart_lgpl/libart.h>
#include <libart_lgpl/libart-features.h>
#include <libgnomecanvas/libgnomecanvas.h>
#include <goocanvas.h>

static int fails = 0;
#define CHECK(c, msg) do { int ok_ = !!(c); printf("  [%s] %s\n", ok_ ? "PASS" : "FAIL", msg); if(!ok_) fails++; } while(0)

int main(void) {
  g_type_init();
  printf("libart_lgpl: version %d.%d.%d\n", LIBART_MAJOR_VERSION, LIBART_MINOR_VERSION, LIBART_MICRO_VERSION);
  /* libart: path -> bezier -> svp -> intersection area */
  ArtVpath *sq = art_new(ArtVpath, 6);
  double xs[5] = {0,10,10,0,0}, ys[5] = {0,0,10,10,0};
  for (int i = 0; i < 5; i++) { sq[i].code = i == 0 ? ART_MOVETO : ART_LINETO; sq[i].x = xs[i]; sq[i].y = ys[i]; }
  sq[5].code = ART_END; sq[5].x = sq[5].y = 0;
  ArtSVP *svp = art_svp_from_vpath(sq);
  ArtSVP *wide = art_svp_vpath_stroke(sq, ART_PATH_STROKE_JOIN_MITER, ART_PATH_STROKE_CAP_BUTT, 2.0, 4.0, 0.25);
  ArtDRect b0; art_drect_svp(&b0, svp);
  printf("  svp n_segs=%d bbox=%.1f..%.1f x %.1f..%.1f (libart drops horizontal edges)\n", svp->n_segs, b0.x0, b0.x1, b0.y0, b0.y1);
  CHECK(svp != NULL && svp->n_segs == 2 && b0.x0 == 0 && b0.x1 == 10 && b0.y0 == 0 && b0.y1 == 10, "libart: svp_from_vpath on square keeps 2 vertical edges, bbox 0..10");
  ArtDRect bb; art_drect_svp(&bb, wide);
  CHECK(fabs(bb.x0 - -1.0) < 1e-6 && fabs(bb.x1 - 11.0) < 1e-6, "libart: stroked square (w=2) bbox spans -1..11");
  art_svp_free(svp); art_svp_free(wide); art_free(sq);

  /* libgnomecanvas: GObject types (no display needed) */
  GType gc = gnome_canvas_get_type(), gcg = gnome_canvas_group_get_type(), gcl = gnome_canvas_line_get_type(),
        gct = gnome_canvas_text_get_type(), gcr = gnome_canvas_rect_get_type(), gcp = gnome_canvas_pixbuf_get_type();
  printf("libgnomecanvas types: %s %s %s %s %s %s\n", g_type_name(gc), g_type_name(gcg), g_type_name(gcl), g_type_name(gct), g_type_name(gcr), g_type_name(gcp));
  CHECK(g_type_is_a(gc, GTK_TYPE_LAYOUT), "GnomeCanvas derives from GtkLayout");
  CHECK(g_type_is_a(gcl, GNOME_TYPE_CANVAS_ITEM), "GnomeCanvasLine derives from GnomeCanvasItem");
  GnomeCanvasPoints *pts = gnome_canvas_points_new(3);
  pts->coords[0]=0; pts->coords[1]=0; pts->coords[2]=5; pts->coords[3]=5; pts->coords[4]=9; pts->coords[5]=1;
  CHECK(pts->num_points == 3 && pts->coords[4] == 9.0, "GnomeCanvasPoints alloc/fill");
  gnome_canvas_points_free(pts);

  /* goocanvas 1.x: GObject types + display-free model objects */
  GType goo = goo_canvas_get_type();
  printf("goocanvas types: %s %s %s %s\n", g_type_name(goo), g_type_name(goo_canvas_rect_get_type()), g_type_name(goo_canvas_text_get_type()), g_type_name(goo_canvas_polyline_get_type()));
  CHECK(g_type_is_a(goo, GTK_TYPE_CONTAINER), "GooCanvas derives from GtkContainer");
  GooCanvasItemModel *root = goo_canvas_group_model_new(NULL, NULL);
  GooCanvasItemModel *r = goo_canvas_rect_model_new(root, 1.0, 2.0, 30.0, 40.0, "line-width", 3.0, "fill-color", "red", NULL);
  GooCanvasItemModel *t = goo_canvas_text_model_new(root, "Ramachandran", 5.0, 6.0, -1, GTK_ANCHOR_NW, NULL);
  GooCanvasPoints *gp = goo_canvas_points_new(2); gp->coords[0]=0; gp->coords[1]=0; gp->coords[2]=10; gp->coords[3]=10;
  GooCanvasItemModel *pl = goo_canvas_polyline_model_new(root, FALSE, 0, "points", gp, NULL);
  double x=0,y=0,w=0,h=0, lw=0; g_object_get(r, "x",&x,"y",&y,"width",&w,"height",&h,"line-width",&lw,NULL);
  CHECK(x==1.0 && y==2.0 && w==30.0 && h==40.0 && lw==3.0, "goocanvas rect model property round-trip");
  CHECK(goo_canvas_item_model_get_n_children(root) == 3, "goocanvas group model holds 3 children");
  goo_canvas_points_unref(gp); (void)t; (void)pl;
  g_object_unref(root);
  CHECK(1, "goocanvas models finalized without crash");
  printf("%s (%d failure(s))\n", fails ? "SOME CHECKS FAILED" : "ALL CHECKS PASSED", fails);
  return fails != 0;
}
