# $OpenBSD$

COMMENT =		recognize cpu instructions in an arbitrary binary file

MODPY_EGG_VERSION =	1.0
GH_ACCOUNT =            airbus-seclab
GH_PROJECT =            cpu_rec
GH_TAGNAME =            v${MODPY_EGG_VERSION}
CATEGORIES =		security

HOMEPAGE =		https://github.com/airbus-seclab/cpu_rec

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Apache v2
PERMIT_PACKAGE_CDROM =	Yes

MASTER_SITES =          ${MASTER_SITES_GITHUB}

MODULES =		lang/python
MODPY_VERSION =		${MODPY_DEFAULT_VERSION_3}

NO_TEST =		Yes
NO_BUILD =		Yes

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/cpu_rec.py ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/cpu_rec_corpus
		${INSTALL_DATA} ${WRKSRC}/cpu_rec_corpus/* \
			${PREFIX}/share/cpu_rec_corpus

.include <bsd.port.mk>
