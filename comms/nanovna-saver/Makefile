
COMMENT =		Tool for reading, displaying and saving data from the NanoVNA 
PKGNAME =		nanovna-saver-${GH_TAGNAME}
CATEGORIES =		comms

# GPLV3
PERMIT_PACKAGE =        Yes

GH_ACCOUNT =            NanoVNA-Saver
GH_PROJECT =            nanovna-saver
GH_TAGNAME =            v0.7.3

MODULES +=		lang/python

MODPY_PYBUILD =		setuptools_scm

BUILD_DEPENDS =		x11/qt6/pyside6/pyside \
			math/py-numpy \
			math/py-scipy \
			devel/py-serial

RUN_DEPENDS =		x11/qt6/pyside6/pyside \
			math/py-numpy \
			math/py-scipy \
			devel/py-serial

LIB_DEPENDS =		x11/qt6/pyside6/pyside

.include <bsd.port.mk>
