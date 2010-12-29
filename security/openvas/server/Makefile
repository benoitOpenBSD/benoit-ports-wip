# $OpenBSD$

COMMENT =		OpenVAS server security scanner
DISTNAME =		openvas-server-2.0.3

WANTLIB =		c gcrypt glib-2.0 gpg-error gpgme m pcap util

MASTER_SITES =		${MASTER_SITES_OPENVAS:=562/}

LIB_DEPENDS =		openvas,openvas_hg::security/openvas/libraries \
			openvasnasl::security/openvas/libnasl

MODULES =		devel/gettext

CONFIGURE_STYLE =	gnu
CONFIGURE_ARGS +=	--enable-shared \
			--localstatedir=/var \
			--sharedstatedir=/var

post-install:
		${INSTALL_DATA_DIR} ${PREFIX}/share/doc/openvas
		@sed -e s#!!PREFIX!!#${TRUEPREFIX}#g ${FILESDIR}/README.OpenBSD > \
				${WRKBUILD}/README.OpenBSD
		${INSTALL_DATA} ${WRKBUILD}/README.OpenBSD \
				${PREFIX}/share/doc/openvas

.include <bsd.port.mk>
