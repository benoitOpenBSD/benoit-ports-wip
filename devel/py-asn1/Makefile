# $OpenBSD: Makefile,v 1.27 2017/01/03 19:19:48 landry Exp $

COMMENT =	ASN.1 library for Python

MODPY_EGG_VERSION =	0.3.7
DISTNAME =		pyasn1-${MODPY_EGG_VERSION}
PKGNAME =		${DISTNAME:S/py/py-/}
CATEGORIES =		devel
PKG_ARCH =		*
EPOCH =			0

HOMEPAGE =		https://github.com/etingof/pyasn1

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD 2-Clause
PERMIT_PACKAGE_CDROM =	Yes

MODPY_PI =		Yes
MODPY_SETUPTOOLS =	Yes

MODULES =		lang/python
FLAVORS =		python3
FLAVOR ?=

BUILD_DEPENDS =		textproc/py-sphinx${MODPY_FLAVOR}

DOCSRC =		${WRKSRC}/doc/source

post-build:
	cd ${DOCSRC} && PYTHONPATH=${WRKSRC} \
		${LOCALBASE}/bin/sphinx-build${MODPY_BIN_SUFFIX} -N . _build/html

#DOCSDIR =	${PREFIX}/share/doc/${MODPY_PY_PREFIX}asn1

#post-install:
#	${INSTALL_DATA_DIR} ${DOCSDIR}
#	${INSTALL_DATA} ${WRKSRC}/doc/*.html ${DOCSDIR}

TEST_DEPENDS =		devel/py-test${MODPY_FLAVOR}

do-test: fake
	@cd ${WRKSRC} && env PYTHONPATH=${WRKINST}/${MODPY_SITEPKG} \
		${MODPY_BIN} -m pytest

.include <bsd.port.mk>
