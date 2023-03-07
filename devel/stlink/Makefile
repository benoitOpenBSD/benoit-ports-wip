# $OpenBSD:$ 

COMMENT =	toolset to program and debug STM32 devices

GH_ACCOUNT =	stlink-org
GH_PROJECT =	stlink
GH_TAGNAME =	v1.7.0

SHARED_LIBS =	stlink	1.0 # 1.7.0
CATEGORIES =	devel

# BSD
PERMIT_PACKAGE =	Yes

WANTLIB += atk-1.0 c cairo cairo-gobject gdk-3 gdk_pixbuf-2.0
WANTLIB += gio-2.0 glib-2.0 gobject-2.0 gtk-3 harfbuzz intl pango-1.0
WANTLIB += pangocairo-1.0 usb usb-1.0

COMPILER =		base-clang ports-gcc base-gcc
MODULES =		devel/cmake

LIB_DEPENDS =		x11/gtk+3 \
			devel/libusb-compat
#			devel/libusb1

CONFIGURE_ARGS =	-DCMAKE_INSTALL_MANDIR=${PREFIX}/man/man1

# Fix dos line-endings in files needing patches
pre-patch:
	@cd ${WRKSRC} && perl -i -pe 's/\r$$//' src/libusb_settings.h

.include <bsd.port.mk>
