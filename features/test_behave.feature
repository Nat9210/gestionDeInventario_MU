Feature: gestion integral de la plataforma 

    como usuario de la plataforma, quiero porder acceder de forma segura y poder
    gestionar el inventario de piezas, incluyendo registro, busqueda y movimiento de stock,
    para garantitazr el correcto funcionamiento de la plataforma.

# ----------------------------------------------------------------------
# 1. ACCESO A LA PLATAFORMA (CP001 al CP004)

Scenario: CP001 - Ingresar con credenciales validas
    Given el usuario esta en la pagina de login de la plataforma
    When el usuario inicia sesion con credenciales válidas
    Then el inicio de sesión es exitoso
    And la plataforma muestra el dashboard principal

Scenario: CP002 - Ingresar sin credenciales
    Given el usuario esta en la pagina de login de la plataforma
    When el usuario inicia sesion sin proporcionar credenciales
    Then la plataforma no permite el acceso
    And la plataforma muestra un mensaje de error con el texto "rellenar este campo"

Scenario: CP003 - Ingresar con credenciales incorrectas
    Given el usuario esta en la pagina de login de la plataforma
    When el usuario inicia sesion con credenciales incorrectas <usuario: "incorrecto", contraseña: "12345">
    Then la plataforma no permite el acceso
    And la plataforma muestra un mensaje de error con el texto "credenciales incorrectas"

Scenario: CP004 - Ingresar con al menos un campo incorrecto
    Given el usuario esta en la pagina de login de la plataforma
    When el usuario inicia sesion con una combinación de credenciales parcialmente incorrecta
    Then la plataforma no permite el acceso
    And la plataforma muestra un mensaje de error con el texto "credenciales incorrectas"


# ----------------------------------------------------------------------
# 2. BÚSQUEDA DE PIEZA EN EL INVENTARIO (CP005 al CP008)


Scenario: CP005 - Buscar pieza por código o descripción
    Given el usuario está en la sección de inventario de piezas
    When el usuario realiza una búsqueda de pieza usando un criterio válido (código o descripción)
    Then el sistema muestra la lista de piezas que coinciden con el criterio de búsqueda
    And el usuario puede visualizar los detalles de las piezas encontradas

Scenario: CP006 - Buscar pieza por categoría
    Given el usuario está en la sección de inventario de piezas
    When el usuario realiza una búsqueda de pieza usando un criterio válido (categoría)
    Then el sistema muestra la lista de piezas que coinciden con el criterio de búsqueda
    And el usuario puede visualizar los detalles de las piezas encontradas

Scenario: CP007 - Buscar pieza por estado de stock
    Given el usuario está en la sección de inventario de piezas
    When el usuario realiza una búsqueda de pieza usando un criterio válido (estado de stock: bajo, medio, alto)
    Then el sistema muestra la lista de piezas que coinciden con el criterio de búsqueda
    And el usuario puede visualizar los detalles de las piezas encontradas

Scenario: CP008 - Buscar pieza inexistente
    Given el usuario está en la sección de inventario de piezas
    When el usuario realiza una búsqueda con un criterio que no coincide con ninguna pieza en el inventario
    Then el sistema notifica la ausencia de resultados con el mensaje "se encontró 0 resultados" o "no se encontraron piezas"


# ----------------------------------------------------------------------
# 3. REGISTRAR NUEVA PIEZA (CP009 al CP013)


Scenario: CP009 - Registrar pieza sin código de pieza
    Given el usuario está en el formulario de registro de nueva pieza
    When el usuario intenta registrar una pieza dejando el campo de código en blanco
    Then el sistema muestra el mensaje de validación "rellenar este campo"
    And el sistema no permite completar el registro de la pieza

Scenario: CP010 - Registrar pieza con código de pieza existente
    Given el usuario está en el formulario de registro de nueva pieza
    When el usuario intenta registrar una pieza utilizando un código ya existente en el sistema
    Then el sistema muestra el mensaje de error "ya existe una pieza con este codigo"
    And el sistema no permite completar el registro de la pieza

Scenario: CP011 - Registrar pieza sin descripción
    Given el usuario está en el formulario de registro de nueva pieza
    When el usuario intenta registrar una pieza dejando el campo de descripción vacío
    Then el sistema muestra el mensaje de validación "este campo es obligatorio"
    And el sistema no permite completar el registro de la pieza

Scenario: CP012 - Registrar pieza con stock inicial negativo
    Given el usuario está en el formulario de registro de nueva pieza
    When el usuario intenta registrar una pieza ingresando una cantidad negativa para el stock actual
    Then el sistema muestra el mensaje de error "el valor debe ser positivo"
    And el sistema no permite completar el registro de la pieza

Scenario: CP013 - Registrar pieza sin stock mínimo
    Given el usuario está en el formulario de registro de nueva pieza
    When el usuario intenta registrar una pieza dejando el campo de stock mínimo en blanco
    Then el sistema muestra el mensaje de validación "este campo es obligatorio" o "rellenar este campo"
    And el sistema no permite completar el registro de la pieza


# ----------------------------------------------------------------------
# 4. REGISTRAR ENTRADA/SALIDA DE MATERIALES (CP014 al CP017 y adiciones)

Scenario: CP014 - Registrar entrada correctamente
    Given el usuario está en la sección de registro de entrada de materiales
    When el usuario registra una entrada de materiales con datos válidos para la pieza y cantidad
    Then el sistema confirma el registro con el mensaje "entrada registrada"
    And el stock de la pieza seleccionada se actualiza correctamente

Scenario: CP015 - Registrar salida correctamente
    Given el usuario está en la sección de registro de salida de materiales
    When el usuario registra una salida de materiales con datos válidos para la pieza y cantidad
    Then el sistema confirma el registro con el mensaje "salida registrada"
    And el stock de la pieza seleccionada se actualiza correctamente

Scenario: CP016 - Registrar entrada sin seleccionar pieza
    Given el usuario está en la sección de registro de entrada de materiales
    When el usuario intenta registrar una entrada de materiales sin especificar la pieza
    Then el sistema muestra el mensaje de validación "este campo es obligatorio" o "selecciona un elemento de la lista"
    And el sistema no permite registrar la entrada de materiales

Scenario: CP017 - Registrar salida sin seleccionar pieza
    Given el usuario está en la sección de registro de salida de materiales
    When el usuario intenta registrar una salida de materiales sin especificar la pieza
    Then el sistema muestra el mensaje de validación "este campo es obligatorio" o "selecciona un elemento de la lista"
    And el sistema no permite registrar la salida de materiales

Scenario: Registrar entrada con cantidad negativa
    Given el usuario está en la sección de registro de entrada de materiales
    When el usuario intenta registrar una entrada de materiales con una cantidad negativa
    Then el sistema muestra el mensaje de error "el valor debe ser positivo"
    And el sistema no permite registrar la entrada de materiales

Scenario: Registrar salida con cantidad negativa
    Given el usuario está en la sección de registro de salida de materiales
    When el usuario intenta registrar una salida de materiales con una cantidad negativa
    Then el sistema muestra el mensaje de error "el valor debe ser positivo"
    And el sistema no permite registrar la salida de materiales

Scenario: Registrar entrada con cantidad vacía
    Given el usuario está en la sección de registro de entrada de materiales
    When el usuario intenta registrar una entrada de materiales sin especificar la cantidad
    Then el sistema muestra el mensaje de validación "este campo es obligatorio"
    And el sistema no permite registrar la entrada de materiales

Scenario: Registrar salida con cantidad vacía
    Given el usuario está en la sección de registro de salida de materiales
    When el usuario intenta registrar una salida de materiales sin especificar la cantidad
    Then el sistema muestra el mensaje de validación "este campo es obligatorio"
    And el sistema no permite registrar la salida de materiales


# ----------------------------------------------------------------------
# 5. BUSCAR MOVIMIENTOS DE STOCK (CP018 al CP021)
# El Background de login se aplica aquí.
# ----------------------------------------------------------------------

Scenario: CP018 - Buscar movimientos de pieza existente
    Given el usuario está en la página de historial de movimientos
    When el usuario busca el historial de movimientos de una pieza existente por su código
    Then el sistema muestra el historial completo de movimientos de la pieza solicitada

Scenario: CP019 - Buscar movimientos de pieza inexistente
    Given el usuario está en la página de historial de movimientos
    When el usuario busca el historial de movimientos de una pieza inexistente por su código
    Then el sistema muestra el mensaje "no se encontraron movimientos"

Scenario: CP020 - Buscar movimientos por rango de fecha correcta
    Given el usuario está en la página de historial de movimientos
    When el usuario filtra el historial de una pieza existente aplicando un rango de fechas válido
    Then el sistema muestra solo los movimientos de la pieza dentro del rango de fecha indicado

Scenario: CP021 - Buscar movimientos por fecha futura
    Given el usuario está en la página de historial de movimientos
    When el usuario intenta filtrar el historial de una pieza usando un rango de fechas que incluye fechas futuras
    Then el sistema no permite aplicar el filtro con fechas a futuro
    And el sistema muestra una notificación de error o restricción