# $OpenBSD: Makefile.template,v 1.78 2018/07/09 15:00:06 jca Exp $

COMMENT =	Graphical 5-stage RISC-V pipeline simulator
CATEGORIES =	devel education

GH_ACCOUNT =	mortbopet
GH_PROJECT =	Ripes
GH_TAGNAME =	1.0.2

MAINTAINER =	Charles Daniels <charles@cdaniels.net>

# MIT
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB +=	c++ GL Qt5Core Qt5Gui Qt5Widgets c c++abi m pthread

MODULES =	devel/qmake x11/qt5

NO_TEST =	NO

# upstream Makefile does not include a 'install' directive
do-install:
	cp "$(WRKDIST)"/build-*/Ripes "$(PREFIX)/bin/ripes"

.include <bsd.port.mk>
