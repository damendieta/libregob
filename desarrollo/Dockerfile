FROM fabricadesoftwarelibre/libregob:18.1
MAINTAINER Fábrica de Software Libre <libregob@fslibre.com>

# Vamos al usuario root
USER root

# Instalamos las librerias de desarrollo.
RUN set -x; \
        pip3 install watchdog
# Agregamos libregob-addons a los volumens.
VOLUME ["/mnt/libregob-addons"]
 
# Retornamos al al usuario odoo 
USER odoo
