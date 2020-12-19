# $OpenBSD$

COMMENT =	a library for accessing discs and disc image files

DISTNAME =	lib765-0.4.2
CATEGORIES =    devel

SHARED_LIBS =	765 0.0     # 4.2

HOMEPAGE =	https://www.seasip.info/Unix/LibDsk/#765

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB =	bz2 dsk z

MASTER_SITES =	https://www.seasip.info/Unix/LibDsk/

LIB_DEPENDS =	archivers/bzip2

COMPILER =	base-clang ports-gcc base-gcc

BUILD_DEPENDS =	devel/libdsk
RUN_DEPENDS =	devel/libdsk

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV =	CPPFLAGS="-I${LOCALBASE}/include"\
		LDFLAGS="-L${LOCALBASE}/lib"

.include <bsd.port.mk>
