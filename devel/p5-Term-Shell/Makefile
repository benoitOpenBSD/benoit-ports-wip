# $OpenBSD: Makefile,v 1.10 2015/09/04 07:01:30 benoit Exp $
# Original from: Neil Watkiss <nwatkiss@ttul.org>

COMMENT =	simple command-line shell framework

MODULES =	cpan
DISTNAME =	Term-Shell-0.07
CATEGORIES =	devel

# Perl
PERMIT_PACKAGE_CDROM =	Yes

CONFIGURE_STYLE =	modbuild

TEST_DEPENDS =		devel/p5-Test-TrailingSpace

MAKE_ENV +=		TEST_POD=1

.include <bsd.port.mk>
