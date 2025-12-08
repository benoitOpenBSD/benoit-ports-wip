COMMENT =		fractal image generator

MODPY_DISTV =		4.4

SITES =			https://github.com/fract4d/gnofract4d/archive/refs/tags/v${MODPY_DISTV}/
DISTNAME =		gnofract4d-${MODPY_DISTV}

CATEGORIES =		graphics

HOMEPAGE =		https://github.com/fract4d/gnofract4d

# 3-clause BSD
PERMIT_PACKAGE =	Yes

WANTLIB +=		${COMPILER_LIBCXX} m z png jpeg

COMPILER =		base-clang ports-gcc

MODULES =		lang/python \
			devel/meson

BUILD_DEPENDS +=	devel/glib2

LIB_DEPENDS =		graphics/png \
			graphics/jpeg

RUN_DEPENDS +=		devel/desktop-file-utils \
			devel/py-gobject3 \
			graphics/py-cairo \
			misc/shared-mime-info \
			x11/gtk+3 \
			x11/gtk+4,-guic

NO_TEST =		Yes

post-extract:
		sed -i  -e 's,^#!/usr/bin,#!${LOCALBASE}/bin,' \
		${WRKSRC}/bin/version
                
.include <bsd.port.mk>
