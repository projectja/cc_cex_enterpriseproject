# Here you cand find,
# all the constants used
# in the backend.
# This constants are fixes values
# that not be editable.


# Sector de actividad
PRODUCTOS_SERVICIOS = (
   ('', '----------'),
   ('CE', 'Carnes y embutidos'), ('FV', 'Frutas y verduras'), 
   ('PC', 'Pescados y conservas'), ('OA', 'Otros porudctos de alimentacion'), 
   ('BA', 'Bebidas y alcoholes'), ('CP', 'Calzado y piel'),
   ('T', 'Textiles'), ('C', 'Corcho'), ('CM', 'Construcción y mobiliario'),
   ('SI', 'Suministros industriales'), ('PQ', 'Productos químicos y básicos'), 
   ('SC', 'Servicios de consultoría'), ('SM', 'Servicios de montaje/mantenimiento/técnico'), 
   ('SGR', 'Servicios de gestión de residuos'), ('SIE', 'Servicios de ingeniería/energía/renovables y economía circular'), 
   ('TIC', 'Servicios TIC'), 
   ('OTHER', 'Otros'),
)


PYME = (
   (0, 'Si'),
   (1, 'No'),
)

EMP_FIJOS = (
   ('CC', '0-5'),
   ('SD', '6-10'),
   ('OV', '11-20'),
   ('VT', '21-30'),
   ('TC', '31-50'),
   ('CD', '51-250'),
   ('GD', '>250'),
)

EMP_EVENT = (
   ('CCE', '0-5'),
   ('SDE', '6-10'),
   ('OVE', '11-20'),
   ('VTE', '21-30'),
   ('TCE', '31-50'),
   ('CDE', '51-250'),
   ('GDE', '>250'),
) 


VOL_FACT = (
   ('MM', '<100.000 euros'),
   ('MQ', '100.000-500.000 euros'),
   ('QMM', '500.001-1.000.000 euros'),
   ('MQM', '1.000.000-5.000.000 euros'),
   ('QQD', '5.000.001-10.000.000 euros'),
   ('GTM', '>10.000.000 euros'),
)

FREQ_EXPORT = (
   ('EH', 'Exportadora habitual'),
   ('EO', 'Exportadora ocasional'),
   ('EP', 'Empresa con potencial exportador'),
)


STATUS_SOLICITUD = (
   (0, 'Por confirmar'),
   (1, 'Enviada'),
)