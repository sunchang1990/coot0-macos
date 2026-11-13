#include <gdk/gdkglconfig.h>
G_BEGIN_DECLS
gboolean gdk_gl_drawable_gl_begin(GdkGLDrawable *d, GdkGLContext *c);
void gdk_gl_drawable_gl_end(GdkGLDrawable *d);
void gdk_gl_drawable_swap_buffers(GdkGLDrawable *d);
gboolean gdk_gl_drawable_is_double_buffered(GdkGLDrawable *d);
G_END_DECLS
