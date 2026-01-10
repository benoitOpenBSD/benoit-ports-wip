
COMMENT =		python filter design analysis tool

MODPY_EGG_VERSION = 	v0.9.5
DISTNAME =		pyfda-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME}
CATEGORIES =		cad

HOMEPAGE =		https://github.com/chipmuenk/pyfda

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes
MODPY_PI =		Yes

RUN_DEPENDS =		graphics/py-matplotlib \
			math/py-numpy \
			math/py-numexpr \ 
			math/py-scipy \
			textproc/py-markdown \
			x11/py-qt5

NO_TEST =		Yes

.include <bsd.port.mk>
