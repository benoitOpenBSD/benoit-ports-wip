# $OpenBSD$

COMMENT =		HTTPie is a CLI, cURL-like tool for humans

MODPY_EGG_VERSION =	0.4.1
DISTNAME =		httpie-${MODPY_EGG_VERSION}
CATEGORIES =		www

HOMEPAGE =		https://github.com/jkbr/httpie

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =		Yes
PERMIT_PACKAGE_FTP =		Yes
PERMIT_DISTFILES_CDROM =	Yes
PERMIT_DISTFILES_FTP =		Yes

MASTER_SITES =		${MASTER_SITE_PYPI:=h/httpie/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

RUN_DEPENDS =		textproc/py-pygments \
			www/py-requests
BUILD_DEPENDS =		${RUN_DEPENDS}
#REGRESS_DEPENDS =	${RUN_DEPENDS}

NO_REGRESS =            Yes
#do-regress: fake
#			cd ${WRKSRC} && ${MODPY_BIN} ./setup.py test
               
.include <bsd.port.mk>
