
COMMENT =	Simulator for Z80 and GBZ80

DISTNAME =	sdcc-extra-src-20210107
PKGNAME =	${DISTNAME:S/-src//}
CATEGORIES =	devel

HOMEPAGE =	http://sdcc.sourceforge.net/

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB += 		${COMPILER_LIBCXX} c m

SITES =			https://www.arcane-labs.net/download/OpenBSD/ \
			${SITE_SOURCEFORGE:=sdcc/}

EXTRACT_SUFX =	.tar.bz2

# c++11
COMPILER =		base-clang ports-gcc

CONFIGURE_STYLE =	gnu
CONFIGURE_ENV +=	CPPFLAGS="${CPPFLAGS} -I${LOCALBASE}/include" \
			LDFLAGS="${LDFLAGS} -L${LOCALBASE}/lib"

USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/sdcc-extra

do-install:
			${INSTALL_PROGRAM} ${WRKSRC}/emu/rrgb/rrgb  ${PREFIX}/bin/
			${INSTALL_PROGRAM} ${WRKSRC}/emu/rrz80/rrz80 ${PREFIX}/bin/

NO_TEST =		Yes

.include <bsd.port.mk>
