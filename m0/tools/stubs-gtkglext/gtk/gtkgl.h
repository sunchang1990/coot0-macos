#include <gtk/gtk.h>
#include <gdk/gdkglconfig.h>
#include <gdk/gdkgldrawable.h>
G_BEGIN_DECLS
gboolean gtk_widget_set_gl_capability(GtkWidget *w, GdkGLConfig *c, GdkGLContext *share, gboolean direct, int render_type);
GdkGLContext  *gtk_widget_get_gl_context(GtkWidget *w);
GdkGLDrawable *gtk_widget_get_gl_drawable(GtkWidget *w);
GdkGLConfig   *gtk_widget_get_gl_config(GtkWidget *w);
G_END_DECLS
