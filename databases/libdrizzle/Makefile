# $OpenBSD$

COMMENT =		Drizzle Client & Protocol Library

V =			5.1.4
DISTNAME =		libdrizzle-${V}
SHARED_LIBS +=		drizzle 0.0	# .0.6
CATEGORIES =		databases

HOMEPAGE =		https://launchpad.net/libdrizzle/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# New BSD
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =		https://launchpad.net/libdrizzle/5.1/${V}/+download/

WANTLIB += 		crypto m pthread ssl stdc++ z

BUILD_DEPENDS =		textproc/py-sphinx

USE_GMAKE =		Yes

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--enable-jobserver=no \
			--enable-shared \
			--enable-static
			
NO_TEST =		Yes

#post-install:
#	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/libdrizzle
#	${INSTALL_PROGRAM} ${WRKSRC}/examples/.libs/* ${PREFIX}/share/examples/libdrizzle
        
.include <bsd.port.mk>
