
COMMENT =		recognize cpu instructions in an arbitrary binary file

MODPY_EGG_VERSION =	1.1
GH_ACCOUNT =            airbus-seclab
GH_PROJECT =            cpu_rec
GH_TAGNAME =            v${MODPY_EGG_VERSION}
CATEGORIES =		security

HOMEPAGE =		https://github.com/airbus-seclab/cpu_rec

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Apache v2
PERMIT_PACKAGE =	Yes

SITES =                 ${SITES_GITHUB}

MODULES =		lang/python
#MODPY_PI =		Yes

NO_TEST =		Yes
NO_BUILD =		Yes

pre-configure:
		${SUBST_CMD} ${WRKSRC}/cpu_rec.py

do-install:
		${INSTALL_PROGRAM} ${WRKSRC}/cpu_rec.py ${PREFIX}/bin
		${INSTALL_DATA_DIR} ${PREFIX}/share/cpu_rec_corpus
		${INSTALL_DATA} ${WRKSRC}/cpu_rec_corpus/* \
			${PREFIX}/share/cpu_rec_corpus

.include <bsd.port.mk>
