
COMMENT =		Retro SDK for 8080,8085,8086,Z80

DISTNAME =		hcsdkretro-1.9R0
CATEGORIES =		devel

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE =	Yes

SITES =			${SITES_GITHUB}

HOMEPAGE =		https://github.com/humbertocsjr/hcsdkretro

GH_ACCOUNT =		humbertocsjr
GH_PROJECT =		hcsdkretro
GH_TAGNAME =		v1.9R0

USE_GMAKE =		Yes

WANTLIB +=		c

#NO_TEST =		Yes

do-build:
		@cd ${WRKSRC} && ${GMAKE} 

#post-install:
#	${INSTALL_DATA_DIR} ${PREFIX}/share/wla-dx/tests
#	cp -R ${WRKSRC}/tests/* ${PREFIX}/share/wla-dx/tests
#	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/wla-dx
#	cp -R ${WRKSRC}/doc/* ${PREFIX}/share/doc/wla-dx

.include <bsd.port.mk>
