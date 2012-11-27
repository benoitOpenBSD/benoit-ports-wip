# $OpenBSD$

COMMENT =		HTTPie is a CLI, cURL-like tool for humans

MODPY_EGG_VERSION =	0.3.0
DISTNAME =		${MODPY_EGG_VERSION}
PKGNAME =		httpie-${MODPY_EGG_VERSION}

CATEGORIES =		www

HOMEPAGE =		https://github.com/jkbr/httpie

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =		Yes
PERMIT_PACKAGE_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes
PERMIT_DISTFILES_FTP =		Yes

MASTER_SITES =		https://github.com/jkbr/httpie/archive/

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

WRKDIST =		${WRKDIR}/${PKGNAME}/

RUN_DEPENDS =		textproc/py-pygments \
			www/py-requests
BUILD_DEPENDS =		${RUN_DEPENDS}
REGRESS_DEPENDS = 	${RUN_DEPENDS}

do-regress:
			cd ${WRKSRC}/tests && ${MODPY_BIN} tests.py

.include <bsd.port.mk>
