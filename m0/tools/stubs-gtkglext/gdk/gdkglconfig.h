/* STUB of GtkGLExt API surface used by Coot 0.9.8.96 (inventory only) */
#ifndef STUB_GDKGLCONFIG_H
#define STUB_GDKGLCONFIG_H
#include <glib-object.h>
#include <gdk/gdk.h>
G_BEGIN_DECLS
typedef struct _GdkGLConfig GdkGLConfig;
typedef struct _GdkGLContext GdkGLContext;
typedef struct _GdkGLDrawable GdkGLDrawable;
typedef enum { GDK_GL_MODE_RGB=0, GDK_GL_MODE_RGBA=0, GDK_GL_MODE_INDEX=1<<2, GDK_GL_MODE_SINGLE=0, GDK_GL_MODE_DOUBLE=1<<1,
               GDK_GL_MODE_STEREO=1<<3, GDK_GL_MODE_ALPHA=1<<4, GDK_GL_MODE_DEPTH=1<<5, GDK_GL_MODE_STENCIL=1<<6,
               GDK_GL_MODE_ACCUM=1<<7, GDK_GL_MODE_MULTISAMPLE=1<<8 } GdkGLConfigMode;
#define GDK_GL_MODE_SAMPLES_SHIFT 9
#define GDK_GL_STEREO 0
#define GDK_GL_RGBA_TYPE 0
GdkGLConfig *gdk_gl_config_new_by_mode(GdkGLConfigMode mode);
gboolean gdk_gl_config_has_stencil_buffer(GdkGLConfig *c);
G_END_DECLS
#endif
