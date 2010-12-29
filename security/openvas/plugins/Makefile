# $OpenBSD$

COMMENT-main =		plugins for OpenVAS security scanner
COMMENT-scripts =	plugins scripts for OpenVAS security scanner

V =			1.0.7
DISTNAME =		openvas-plugins-${V}
PKGNAME-main =		${DISTNAME}
FULLPKGNAME-scripts =	openvas-plugins-scripts-${V}

WANTLIB-main =		glib-2.0 iconv intl m pcap pcre util

MASTER_SITES =		${MASTER_SITES_OPENVAS:=539/}

BUILD_DEPENDS =		::security/openvas/server
RUN_DEPENDS-scripts = 	::security/openvas/plugins,-main
RUN_DEPENDS =		::net/rsync \
			::security/openvas/server

MODULES-main =		devel/gettext

LIB_DEPENDS-main =		openvas,openvas_hg::security/openvas/libraries


CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--localstatedir=/var
CONFIGURE_ARGS +=	--sharedstatedir=/var
CONFIGURE_ARGS +=	--enable-bpf-sharing --enable-shared

MULTI_PACKAGES = 	-main -scripts

PKG_ARCH-scripts =	*

CFLAGS +=		-I/usr/local/include

.include <bsd.port.mk>
