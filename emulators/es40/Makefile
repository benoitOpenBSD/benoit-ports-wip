
COMMENT =		es40 emulator

DISTNAME =		es40-20230707
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

HOMEPAGE =		https://github.com/gdwnldsKSC/es40

GH_ACCOUNT =		gdwnldsKSC
GH_PROJECT =		es40
GH_COMMIT =		9d4ac0193b7fefca7ce2575f63cc786e05787e13

WANTLIB +=		c util X11

AUTOCONF_VERSION =	2.69
AUTOMAKE_VERSION =	1.16

CONFIGURE_STYLE =	autoreconf

LIB_DEPEND =		devel/sdl

#CFLAGS +=		-I${X11BASE}/include
#CXXFLAGS +=		-I${X11BASE}/include
CONFIGURE_ENV +=	CPPFLAGS="-I${X11BASE}/include -I${LOCALBASE}/include/SDL" \
			LDFLAGS="-L${X11BASE}/lib" \
			CFLAGS=="-I${X11BASE}/include -I${LOCALBASE}/include/SDL"

USE_GMAKE =		Yes

# DEBUG_PACKAGES =	${BUILD_PACKAGES}

#do-install:
#			${INSTALL_PROGRAM} ${WRKSRC}/emu/sim6809 ${PREFIX}/bin/
#			${INSTALL_DATA_DIR} ${PREFIX}/share/sim6809
#			${INSTALL_DATA} ${WRKSRC}/doc/* ${PREFIX}/share/sim6809
#			${INSTALL_DATA} ${WRKSRC}/README ${PREFIX}/share/sim6809

NO_TEST =		Yes

.include <bsd.port.mk>
