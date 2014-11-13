# $OpenBSD: Makefile,v 1.23 2010/09/03 12:34:55 sthen Exp $

SHARED_ONLY=		Yes

COMMENT-main=		LDAP client API for Python
COMMENT-examples=	example programs for the LDAP client API for Python

MODPY_EGG_VERSION =	2.3.12
DISTNAME=		python-ldap-${MODPY_EGG_VERSION}
PKGNAME-main=		py-ldap-${MODPY_EGG_VERSION}
FULLPKGNAME-examples=	py-ldap-examples-${MODPY_EGG_VERSION}
FULLPKGPATH-examples=	databases/py-ldap,-examples

CATEGORIES=		databases

HOMEPAGE=		http://python-ldap.sourceforge.net/

# Python
PERMIT_PACKAGE_CDROM =	Yes

WANTLIB-main=		crypto ssl lber-2.3 ldap_r-2.3 sasl2

MASTER_SITES=		${MASTER_SITE_PYPI:=p/python-ldap/}

MODULES=		lang/python
MODPY_VERSION=		${FLAVOR:S/python//}

LIB_DEPENDS-main=	::databases/openldap \
			::security/cyrus-sasl2

FLAVORS=		python2.4 python2.7
FLAVOR?=		python2.7

.if ${FLAVOR:L:Mpython2.4} && !${FLAVOR:L:Npython2.4}
MULTI_PACKAGES= -main
.elif ${FLAVOR:L:Mpython2.7} && !${FLAVOR:L:Npython2.7}
MULTI_PACKAGES= -main -examples
.else
ERRORS+=	"Fatal: You must select one version: ${FLAVORS}"
.endif

EXAMPLESDIR=		${PREFIX}/share/examples/py-ldap

pre-configure:
	${SUBST_CMD} ${WRKSRC}/setup.cfg
 
post-install:
	${INSTALL_DATA_DIR} ${EXAMPLESDIR}
	cd ${WRKSRC}; tar cf - Demo | tar xf - -C ${EXAMPLESDIR}
	find ${WRKINST} -name \*.egg-info -exec rm {} \;

do-test: fake
	@cd ${WRKSRC}/Tests/Lib && ${MAKE_ENV} \
		PYTHONPATH=${WRKINST}${MODPY_SITEPKG} \
		${MODPY_BIN} ./test_ldapurl.py 

.include <bsd.port.mk>
