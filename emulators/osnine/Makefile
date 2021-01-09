# $OpenBSD$

COMMENT =		OS9 level One emulator (for Motorola 6809)

DISTNAME =		osnine-1.2
CATEGORIES =		emulators

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

MASTER_SITES =		${HOMEPAGE}

HOMEPAGE =		https://www.roug.org/soren/6809/

WANTLIB +=		c ${COMPILER_LIBCXX} X11 m

AUTOCONF_VERSION =      2.69
AUTOMAKE_VERSION =      1.16

BUILD_DEPENDS +=	devel/cppunit

CONFIGURE_STYLE =       autoreconf

CONFIGURE_ENV+=		CPPFLAGS="-I${LOCALBASE}/include -I/usr/X11R6/include" \
			LDFLAGS="-L${LOCALBASE}/lib -L/usr/X11R6/lib"

NO_TEST =		Yes

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/os9l1 ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/usim ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/v6809 ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/disassemos9 ${PREFIX}/bin/
			${INSTALL_DATA_DIR} ${PREFIX}/share/osnine
			cp ${WRKSRC}/{README,NEWS,TODO} ${PREFIX}/share/osnine

.include <bsd.port.mk>
