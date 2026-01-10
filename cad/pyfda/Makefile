
COMMENT =		python filter design analysis tool

#MODPY_EGG_VERSION =     0.9.5
DISTNAME =		pyfda-260109
GH_ACCOUNT =    	chipmuenk
GH_PROJECT =    	pyfda
#GH_TAGNAME =		v${MODPY_EGG_VERSION}
GH_COMMIT =		1b4e8b46beec64da388704838567e27d81882556

CATEGORIES =		cad

HOMEPAGE =		https://github.com/chipmuenk/pyfda

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv3
PERMIT_PACKAGE =	Yes

MODULES =		lang/python

MODPY_PYBUILD =		setuptools

RUN_DEPENDS =		graphics/py-matplotlib \
			math/py-numpy \
			math/py-numexpr \
			math/py-scipy \
			textproc/py-markdown \
			x11/py-qt5 \
			devel/mplcursors \
			textproc/py-docutils

NO_TEST =		Yes

.include <bsd.port.mk>
