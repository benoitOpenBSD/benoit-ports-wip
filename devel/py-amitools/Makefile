
COMMENT =		Various tools for using AmigaOS programs on other platforms

MODPY_DISTV =		0.8.1
GH_ACCOUNT =		cnvogelg
GH_PROJECT =		amitools
GH_TAGNAME =		${MODPY_DISTV}
DISTNAME =		amitools-${MODPY_DISTV}
PKGNAME =		py-${DISTNAME}

CATEGORIES =            devel

HOMEPAGE =		https://github.com/cnvogelg/machine68k/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

#MODPY_PI =		Yes
MODPY_PYBUILD =		setuptools

BUILD_DEPENDS =		emulators/py-machine68k \
			lang/cython

.include <bsd.port.mk>
