# $OpenBSD$

COMMENT =		libraries for OpenVAS security scanner

DISTNAME =		openvas-libraries-2.0.4

SHARED_LIBS +=		openvas		0.0
SHARED_LIBS +=		openvas_hg	0.0

WANTLIB =		pcap pcre util

BUILD_DEPENDS = 	::security/gnutls
RUN_DEPENDS =		::security/gnutls
LIB_DEPENDS +=		glib-2.0::devel/glib2

MODULES =		devel/gettext

MASTER_SITES =		${MASTER_SITES_OPENVAS:=600/}

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--localstatedir="/var"
CONFIGURE_ARGS +=	--sharedstatedir="/var"
CONFIGURE_ARGS +=	--enable-bpf-sharing --enable-shared

.include <bsd.port.mk>
