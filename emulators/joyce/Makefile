
COMMENT =	emulates the Amstrad PCW

DISTNAME =	joyce-2.2.14
CATEGORIES =	emulators

HOMEPAGE =	https://www.seasip.info/Unix/Joyce/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

SHARED_LIBS +=	link                 1.0      # 1.0

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB +=	c dsk m png xml2 z
WANTLIB +=	${COMPILER_LIBCXX} 765 SDL bz2 iconv lzma sndio usbhid

SITES =		https://www.seasip.info/Unix/Joyce/

LIB_DEPENDS =	devel/sdl \
		graphics/png \
		textproc/libxml \
		devel/libdsk \
		devel/lib765

COMPILER =	base-clang ports-gcc base-gcc

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =	CPPFLAGS="-I${LOCALBASE}/include -Wno-narrowing"\
		LDFLAGS="-L${LOCALBASE}/lib" 
CONFIGURE_ARGS =	--with-system-libdsk --with-system-lib765

USE_GMAKE =	Yes

.include <bsd.port.mk>
