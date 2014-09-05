# $OpenBSD: Makefile,v 1.15 2014/03/18 19:24:59 sthen Exp $

COMMENT =		GeoIP Python API

MODPY_EGG_VERSION =	1.3.2
DISTNAME =		GeoIP-${MODPY_EGG_VERSION}
PKGNAME =		py-GeoIP-${MODPY_EGG_VERSION}
CATEGORIES =		net

HOMEPAGE =		http://dev.maxmind.com/geoip/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# LGPL v2.1
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB += ${MODPY_WANTLIB} GeoIP>=8 pthread

MASTER_SITES =		${MASTER_SITE_PYPI:=G/GeoIP/}

MODULES =		lang/python
MODPY_ADJ_FILES =	tests/test*.py
MODPY_SETUPTOOLS =	Yes

LIB_DEPENDS =		net/GeoIP>=1.4.7

EXAMPLEDIR =		${PREFIX}/share/examples/py-GeoIP

pre-patch:
	perl -pi -e 's,/usr/local/share/GeoIP,${LOCALSTATEDIR}/db/GeoIP,g' \
	    ${WRKSRC}/*.py

pre-configure:
	@perl -pi -e 's|_LOCALBASE_|${LOCALBASE}|g' ${WRKSRC}/setup.py
        
post-install:
	${INSTALL_DATA_DIR} ${EXAMPLEDIR}
	${INSTALL_SCRIPT} ${WRKSRC}/${MODPY_ADJ_FILES} ${EXAMPLEDIR}

.include <bsd.port.mk>
