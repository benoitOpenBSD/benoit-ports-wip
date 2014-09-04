# $OpenBSD: Makefile,v 1.9 2013/10/25 16:16:57 benoit Exp $

COMMENT =	perl binding for Redis database

DISTNAME =	Redis-1.975
CATEGORIES =	databases

EPOCH =		0

MAINTAINER =	Benoit Lecocq <benoit@openbsd.org>

# Perl
PERMIT_PACKAGE_CDROM =	Yes

MODULES =		cpan

RUN_DEPENDS =		devel/p5-Try-Tiny

BUILD_DEPENDS =		devel/p5-Test-CPAN-Meta

TEST_DEPENDS =	devel/p5-Test-Deep \
			devel/p5-Test-Fatal \
			devel/p5-Test-SharedFork \
			devel/p5-PerlIO-via-Timeout \
			net/p5-Test-TCP \
			net/p5-IO-Socket-Timeout \
			devel/p5-Try-Tiny \
			devel/p5-IO-String \
			databases/redis

.include <bsd.port.mk>
