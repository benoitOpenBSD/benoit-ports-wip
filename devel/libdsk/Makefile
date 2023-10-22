
COMMENT =	a library for accessing discs and disc image files

DISTNAME =	libdsk-1.4.2

SHARED_LIBS =	dsk 0.0     # 6.13

CATEGORIES =	devel emulators

HOMEPAGE =	https://www.seasip.info/Unix/LibDsk/

MAINTAINER =	Tim Meunier <trondd@kagu-tsuchi.com>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB =	bz2 c z

SITES =		https://www.seasip.info/Unix/LibDsk/

LIB_DEPENDS =	archivers/bzip2

COMPILER =	base-clang ports-gcc base-gcc

SEPARATE_BUILD =	Yes
CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =	CPPFLAGS="-I${LOCALBASE}/include"\
		LDFLAGS="-L${LOCALBASE}/lib"

.include <bsd.port.mk>
