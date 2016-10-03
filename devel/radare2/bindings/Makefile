# $OpenBSD: Makefile,v 1.2 2015/08/27 13:42:09 jca Exp $

COMMENT =		Vala bindings for Radare2

DISTNAME =		radare2-bindings-${V}

BUILD_DEPENDS =		devel/radare2/main>=${V}
RUN_DEPENDS =		lang/vala \
			devel/radare2/main>=${V}

PKG_ARCH =		*

# This would go if we wanted to package other bindings.
NO_BUILD =		Yes

# Only install vala bindings for now. Maybe more in the future.
INSTALL_TARGET =	install-vapi

.include <bsd.port.mk>
