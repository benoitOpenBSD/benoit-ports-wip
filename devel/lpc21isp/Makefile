
COMMENT =	portable command line ISP for LPC family and ADUC70xx

V =		1.97
DISTNAME =	lpc21isp-${V}
CATEGORIES =	devel

HOMEPAGE =	https://github.com/capiman/lpc21isp

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# LPGLv3
PERMIT_PACKAGE =	Yes

SITES =                 ${SITES_GITHUB}
GH_ACCOUNT =            capiman
GH_PROJECT =            lpc21isp
GH_COMMIT =		cf89d0b122ef02358e0f130b8f32cb804c11a54e

USE_GMAKE =		Yes

NO_TEST =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKDIST}/lpc21isp ${PREFIX}/bin

.include <bsd.port.mk>
