
COMMENT =		a port-knocking server

DISTNAME =		knock-0.5
CATEGORIES =		security

HOMEPAGE =		http://www.zeroflux.org/proj/knock/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

SITES =			http://www.zeroflux.org/proj/knock/files/

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--prefix=${LOCALBASE} 
CONFIGURE_ENV =		CFLAGS="-I${LOCALBASE}/include"

.include <bsd.port.mk>
