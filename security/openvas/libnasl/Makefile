
COMMENT =		OpenVAS security scanner libnasl
DISTNAME =		openvas-libnasl-2.0.2

SHARED_LIBS =		openvasnasl	0.0	

SITES =			${SITES_OPENVAS:=561/}

WANTLIB +=		c gcrypt glib-2.0 gpg-error pcap pcre rpcsvc
WANTLIB +=		util z

LIB_DEPENDS +=		openvas,openvas_hg::security/openvas/libraries
LIB_DEPENDS +=		gnutls::security/gnutls
LIB_DEPENDS +=		gpgme::security/gpgme

MODULES =		devel/gettext

BUILD_DEPENDS =		::devel/bison
RUN_DEPENDS =		::net/rsync

CONFIGURE_STYLE =	gnu

CONFIGURE_ENV =		LDFLAGS="-L${LOCALBASE}/lib"

.include <bsd.port.mk>
