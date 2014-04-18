# $OpenBSD$

COMMENT =		an SSL library with an intuitive API

DISTNAME =		polarssl-1.3.6
CATEGORIES =		security
SHARED_LIBS +=		polarssl	0.0

HOMEPAGE =              https://polarssl.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# Dual licensed: GPLv2+/Commercial
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		 c crypto pthread ssl

MASTER_SITES =		https://polarssl.org/download/
EXTRACT_SUFX =		-gpl.tgz

MODULES =		devel/cmake

pre-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/polarssl
		${INSTALL_DATA} ${WRKSRC}/README.rst ${WRKSRC}/ChangeLog \
			${PREFIX}/share/doc/polarssl

# XXX
#do-test: fake
#		cd ${WRKSRC}/tests && ${SETENV} \
#			LD_PRELOAD="${WRKINST}${PREFIX}/lib/libpolarssl.so.${LIBpolarssl_VERSION}" \
#			${GMAKE} check
#		cd ${WRKSRC}/tests && ${SETENV} \
#			LD_PRELOAD="${WRKBUILD}/library/libpolarssl.so.${LIBpolarssl_VERSION}" \
#			${GMAKE} check

.include <bsd.port.mk>
