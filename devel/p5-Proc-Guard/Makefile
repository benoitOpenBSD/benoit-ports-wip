# $OpenBSD: Makefile,v 1.1.1.1 2014/12/28 09:20:30 benoit Exp $

COMMENT =	process runner with RAII pattern

DISTNAME =	Proc-Guard-0.07
CATEGORIES =	devel

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		cpan

CONFIGURE_STYLE =	modbuild

RUN_DEPENDS =		devel/p5-Class-Accessor-Lite
TEST_DEPENDS +=		sysutils/p5-File-Which \
			net/p5-Test-TCP \
			devel/p5-Test-Requires

.include <bsd.port.mk>
