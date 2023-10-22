
COMMENT =	interface to bzip2 compression library

DISTNAME =	Compress-Bzip2-2.28
CATEGORIES =	archivers

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl
PERMIT_PACKAGE =	Yes

MODULES =	cpan
LIB_DEPENDS =	archivers/bzip2
WANTLIB =	bz2>=10 perl

MAKE_ENV =	TEST_POD=Yes

pre-configure:
	${SUBST_CMD} ${WRKSRC}/config.in

.include <bsd.port.mk>
