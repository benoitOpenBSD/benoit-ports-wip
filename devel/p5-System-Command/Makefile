# $OpenBSD: Makefile,v 1.3 2013/03/11 10:50:21 espie Exp $

COMMENT = 	object for running system commands

MODULES =	cpan
DISTNAME =	System-Command-1.108
CATEGORIES =	devel

# perl
PERMIT_PACKAGE_CDROM =	Yes

MAKE_ENV +=		TEST_POD=yes

BUILD_DEPENDS =	devel/p5-IPC-Run
# XXX  Failed test 'process 1778 is still alive' at t/20-zombie.t line 149.
TEST_DEPENDS =	devel/p5-Test-Output 

.include <bsd.port.mk>
