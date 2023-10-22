
COMMENT =		GNU PIC assembler and utilities

VERSION =		1.5.2
DISTNAME =		gputils-${VERSION}
CATEGORIES =		devel

HOMEPAGE =		http://gputils.sourceforge.net/

MAINTAINER =		Benoit Lecocq <benoit@openbsd.org>

# GPLv2
PERMIT_PACKAGE =	Yes

WANTLIB =		c

#SITES =		${SITE_SOURCEFORGE:=gputils/}
#SITES0 =		http://www.arcane-labs.net/download/OpenBSD/
SITES =			http://www.arcane-labs.net/download/OpenBSD/

#DISTFILES =		${DISTNAME}${EXTRACT_SUFX} gputils-testsuite-${VERSION}${EXTRACT_SUFX}:0
DIST_SUBDIR =		gputils

CONFIGURE_STYLE =	autoconf
CONFIGURE_ENV =		"CC=${CC}" "CPP=${CPP}" "CFLAGS=${CFLAGS}" "CPPFLAGS=${CPPFLAGS}" "LDFLAGS=${LDFLAGS}"
CONFIGURE_ARGS +=	--disable-html-doc

USE_GMAKE =		Yes

AUTOCONF_VERSION =	2.69

do-test:
	cd ${WRKSRC}/gpasm/testsuite && sh ./test all


#DOCFILES =	gputils.lyx gputils.pdf gputils.ps
DOCFILES =	gputils.lyx

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/gputils
.for FILE in ${DOCFILES}
	${INSTALL_DATA} ${WRKSRC}/doc/${FILE} ${PREFIX}/share/doc/gputils
.endfor

.include <bsd.port.mk>
