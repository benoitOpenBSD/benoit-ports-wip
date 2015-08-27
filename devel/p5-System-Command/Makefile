# $OpenBSD: Makefile,v 1.4 2014/05/01 06:59:28 benoit Exp $

COMMENT = 	object for running system commands

MODULES =	cpan
DISTNAME =	System-Command-1.112
CATEGORIES =	devel

# perl
PERMIT_PACKAGE_CDROM =	Yes

MAKE_ENV +=		TEST_POD=yes

BUILD_DEPENDS = devel/p5-IPC-Run

# XXX  Failed test 'process 1778 is still alive' at t/20-zombie.t line 149.
TEST_DEPENDS =	devel/p5-Test-Output

.include <bsd.port.mk>
