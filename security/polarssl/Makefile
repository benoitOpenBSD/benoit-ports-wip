# $OpenBSD$

COMMENT =		an SSL library with an intuitive API

V =			1.3.1
DISTNAME =		polarssl-${V}-gpl
PKGNAME =		${DISTNAME:S/-gpl//}
CATEGORIES =		security
SHARED_LIBS +=		polarssl	0.0

HOMEPAGE =              https://polarssl.org/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB =		 c

MASTER_SITES =		https://polarssl.org/download/
EXTRACT_SUFX =		.tgz

USE_GMAKE =		Yes

WRKDIST =		${WRKDIR}/polarssl-${V}

PROGRAMS =		aescrypt2 benchmark cert_app cert_req crl_app crypt_and_hash \
			dh_client dh_genprime dh_server generic_sum gen_entropy gen_key \
			gen_random_havege hello key_app md5sum mpi_demo pem2der pk_decrypt \
			pk_encrypt pk_sign pk_verify rsa_decrypt rsa_encrypt rsa_genkey \
			rsa_sign rsa_verify selftest sha1sum sha2sum ssl_cert_test \
			ssl_client1 ssl_client2 ssl_fork_server ssl_mail_client \
			ssl_server ssl_server2 ssl_test strerror

pre-configure:
		${SUBST_CMD} ${WRKSRC}/library/Makefile

do-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/polarssl
		${INSTALL_DATA} ${WRKSRC}/README.rst ${WRKSRC}/ChangeLog \
			${PREFIX}/share/doc/polarssl
		${INSTALL_DATA} ${WRKSRC}/library/libpolarssl.a ${PREFIX}/lib
		${INSTALL_DATA} ${WRKSRC}/library/libpolarssl.so.${LIBpolarssl_VERSION} ${PREFIX}/lib
		${INSTALL_DATA_DIR} ${PREFIX}/include/polarssl
		${INSTALL_DATA} ${WRKSRC}/include/polarssl/* ${PREFIX}/include/polarssl
.for p in ${PROGRAMS}
		${INSTALL_PROGRAM} ${WRKBUILD}/programs/*/${p} ${PREFIX}/bin/polarssl_${p}
.endfor

do-test: fake
		cd ${WRKSRC}/tests && ${SETENV} \
			LD_PRELOAD="${WRKBUILD}/library/libpolarssl.so.${LIBpolarssl_VERSION}" \
			${GMAKE} check

.include <bsd.port.mk>
