# $OpenBSD$

COMMENT =		an SSL library with an intuitive API

V =			1.3.4
DISTNAME =		polarssl-${V}-gpl
PKGNAME =		${DISTNAME:S/-gpl//}
CATEGORIES =		security
SHARED_LIBS +=		polarssl	0.0

HOMEPAGE =              https://polarssl.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		 c crypto pthread ssl

MASTER_SITES =		https://polarssl.org/download/
EXTRACT_SUFX =		.tgz

MODULES =		devel/cmake

USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/polarssl-${V}

pre-configure:
		${SUBST_CMD} ${WRKSRC}/library/Makefile

pre-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/polarssl
		${INSTALL_DATA} ${WRKSRC}/README.rst ${WRKSRC}/ChangeLog \
			${PREFIX}/share/doc/polarssl

#do-test: fake
#		cd ${WRKSRC}/tests && ${SETENV} \
#			LD_PRELOAD="${WRKINST}${PREFIX}/lib/libpolarssl.so.${LIBpolarssl_VERSION}" \
#			${GMAKE} check
#		cd ${WRKSRC}/tests && ${SETENV} \
#			LD_PRELOAD="${WRKBUILD}/library/libpolarssl.so.${LIBpolarssl_VERSION}" \
#			${GMAKE} check

.include <bsd.port.mk>
