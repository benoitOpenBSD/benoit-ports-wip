# $OpenBSD$

COMMENT =		a Python crypto and SSL toolkit

MODPY_EGG_VERSION =	0.21.1
DISTNAME =		M2Crypto-${MODPY_EGG_VERSION}
PKGNAME =		py-${DISTNAME:L}

CATEGORIES =		security

HOMEPAGE =		http://chandlerproject.org/bin/view/Projects/MeTooCrypto

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		ssl crypto

MASTER_SITES =		${MASTER_SITE_PYPI:=M/M2Crypto/}

MODULES =		lang/python
MODPY_SETUPTOOLS =	Yes

BUILD_DEPENDS =		devel/swig

DOCSDIR =		${PREFIX}/share/doc/py-m2crypto
DEMOSDIR =		${PREFIX}/share/examples/py-m2crypto

post-install:
			${INSTALL_DATA_DIR} ${DOCSDIR}
			${INSTALL_DATA} ${WRKSRC}/doc/* ${DOCSDIR}
			${INSTALL_DATA_DIR} ${DEMOSDIR}/contrib
			${INSTALL_DATA} ${WRKSRC}/demo/*.py ${DEMOSDIR}
			${INSTALL_DATA} ${WRKSRC}/demo/*.pem ${DEMOSDIR}
			${INSTALL_DATA} ${WRKSRC}/contrib/* ${DEMOSDIR}/contrib

.include <bsd.port.mk>
