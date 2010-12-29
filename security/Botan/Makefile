# $OpenBSD$

COMMENT =		a C++ crypto library

VERSION =		1.8.2
DISTNAME =		Botan-${VERSION}
SO_VERSION =		0.0
SHARED_LIBS =		botan	${SO_VERSION}

CATEGORIES =		security

HOMEPAGE =		http://botan.randombit.net/news/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# BSD
PERMIT_PACKAGE_CDROM =	Yes
PERMIT_PACKAGE_FTP =	Yes
PERMIT_DISTFILES_CDROM =Yes
PERMIT_DISTFILES_FTP =	Yes

WANTLIB =		m

MASTER_SITES =		http://files.randombit.net/botan/

EXTRACT_SUFX =		.tgz

MODULES =		perl

MAKE_FLAGS +=		LIB_OPT="${CXXFLAGS}"

CONFIGURE_STYLE =	simple
CONFIGURE_SCRIPT =	configure.pl
CONFIGURE_ARGS +=	${CONFIGURE_SHARED} \
			--prefix=${LOCALBASE} \
			--cc=gcc \
			--os=openbsd \
			--cpu=generic \
			--with-tr1=none

NO_REGRESS =		Yes

SUBST_VARS += SO_VERSION

pre-configure:
	${SUBST_CMD} ${WRKSRC}/src/build-data/makefile/unix_shr.in
#	${SUBST_CMD} ${WRKSRC}/doc/examples/GNUmakefile

do-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/Botan
	${INSTALL_DATA} ${WRKSRC}/doc/{*.txt,*.pdf} ${PREFIX}/share/doc/Botan
	${INSTALL_DATA_DIR} ${PREFIX}/share/examples/Botan
	${INSTALL_DATA} ${WRKSRC}/doc/examples/{*.cpp,*.txt,GNUmakefile} \
		${PREFIX}/share/examples/Botan
	${INSTALL_DATA_DIR} ${PREFIX}/include/botan
	${INSTALL_DATA} ${WRKSRC}/build/include/botan/* ${PREFIX}/include/botan
	${INSTALL_DATA} ${WRKSRC}/libbotan.a ${PREFIX}/lib/libbotan.a
	${INSTALL_DATA} ${WRKSRC}/libbotan.so.${SO_VERSION} \
		${PREFIX}/lib
	${INSTALL_SCRIPT} ${WRKSRC}/build/botan-config ${PREFIX}/bin

.include <bsd.port.mk>
