# $OpenBSD$

COMMENT =		Drizzle Client & Protocol Library

V =			5.1.2
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

MASTER_SITES =		https://launchpad.net/libdrizzle/5.1/${V}/+download/

BUILD_DEPENDS =		textproc/py-sphinx

USE_LIBTOOL =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED}
			
NO_REGRESS =		Yes

#post-install:
#	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/libdrizzle
#	${INSTALL_PROGRAM} ${WRKSRC}/examples/.libs/* ${PREFIX}/share/examples/libdrizzle
        
.include <bsd.port.mk>
