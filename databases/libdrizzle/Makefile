# $OpenBSD$

COMMENT =		Drizzle Client & Protocol Library

V =			0.8
DISTNAME =		libdrizzle-${V}

SHARED_LIBS +=		drizzle 0.0	# .0.6

CATEGORIES =		databases

HOMEPAGE =		https://launchpad.net/libdrizzle/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# New BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

MASTER_SITES =		http://launchpad.net/libdrizzle/trunk/${V}/+download/

LIB_DEPENDS =		databases/sqlite3

USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--disable-mtmalloc
			
NO_REGRESS =		Yes

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/libdrizzle
	${INSTALL_PROGRAM} ${WRKSRC}/examples/.libs/* ${PREFIX}/share/examples/libdrizzle
        
.include <bsd.port.mk>
