#	$OpenBSD$

ONLY_FOR_ARCHS= i386 amd64

COMMENT=	instrumented fuzzer
DISTNAME=	afl-0.54b
EXTRACT_SUFX=	.tgz
CATEGORIES=	devel

HOMEPAGE=	http://lcamtuf.coredump.cx/afl/
MASTER_SITES=	${HOMEPAGE}/releases/

# Apache 2.0
PERMIT_PACKAGE_CDROM=	Yes

USE_GMAKE=		Yes
TEST_TARGET=		test_build
WANTLIB=		c

post-install:
	${INSTALL_DATA_DIR} ${PREFIX}/share/doc/afl
	cp ${WRKDIST}/docs/{README,ChangeLog,*.txt} ${PREFIX}/share/doc/afl/

.include <bsd.port.mk>
