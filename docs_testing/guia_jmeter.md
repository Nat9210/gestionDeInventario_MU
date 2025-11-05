# Guía para pruebas de carga con JMeter/BlazeMeter

Este documento explica cómo utilizar los endpoints especiales creados para realizar pruebas de carga en el sistema de inventario sin problemas de CSRF.

## Endpoints disponibles para pruebas

| Endpoint | Método | Descripción |
|---------|--------|-------------|
| `/test/login/` | GET | Muestra el formulario de login sin CSRF |
| `/test/login/` | POST | Autentica al usuario y devuelve JSON con resultado |
| `/test/dashboard/` | GET | Muestra el dashboard sin requerir autenticación |

## Configuración de JMeter/BlazeMeter

### Prueba de Login

1. **Crear una petición HTTP POST al endpoint** `/test/login/`
   - Body parameters: `username` y `password`
   - Content-Type: `application/x-www-form-urlencoded`

2. **Ejemplos de parámetros**:
   ```
   username=admin&password=adminpass
   ```

3. **Respuestas esperadas**:
   - Login exitoso: Status 200 con JSON `{"success": true, "message": "Login exitoso", ...}`
   - Login fallido: Status 401 con JSON `{"success": false, "message": "Credenciales inválidas"}`

4. **Captura de cookies** (opcional):
   - Si necesitas mantener la sesión, configura un Cookie Manager en JMeter

### Prueba de Dashboard

1. **Crear una petición HTTP GET al endpoint** `/test/dashboard/`
   - Sin parámetros requeridos
   - Opcional: añadir `format=json` para recibir respuesta en formato JSON

2. **Ejemplo de URL para respuesta JSON**:
   ```
   /test/dashboard/?format=json
   ```

## Creación de escenarios de prueba

### Escenario 1: Login y acceso a dashboard

1. Configurar Thread Group (número de usuarios, rampas, etc.)
2. Añadir HTTP Request para login POST
3. Añadir JSON Extractor para extraer token de éxito
4. Añadir IF Controller para verificar login exitoso
5. Añadir HTTP Request para dashboard GET
6. Añadir Assertions y Listeners para resultados

### Escenario 2: Prueba de carga en dashboard

1. Configurar Thread Group con alto número de usuarios concurrentes
2. Añadir HTTP Request para dashboard GET con `format=json`
3. Añadir Response Assertion para verificar tiempo de respuesta y datos correctos
4. Añadir Listeners (View Results Tree, Summary Report)

## Validación de pruebas

Para verificar que las pruebas funcionan correctamente:

1. Los endpoints de prueba muestran un banner amarillo indicando "ENTORNO DE PRUEBAS"
2. Las respuestas POST al login devuelven JSON con el formato indicado
3. El dashboard se muestra sin necesidad de autenticación previa
4. Las peticiones a `/test/dashboard/?format=json` devuelven datos en formato JSON

## Notas importantes

- Estos endpoints son SOLO para pruebas de carga y no deben usarse en producción
- No tienen protección CSRF a propósito para facilitar la automatización
- El dashboard de prueba muestra datos reales de la base de datos pero sin requerir login

## Ejemplo de script JMeter

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2" properties="5.0">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="Prueba Sistema Inventario">
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
        <collectionProp name="Arguments.arguments"/>
      </elementProp>
      <stringProp name="TestPlan.user_define_classpath"></stringProp>
      <boolProp name="TestPlan.functional_mode">false</boolProp>
      <boolProp name="TestPlan.serialize_threadgroups">false</boolProp>
    </TestPlan>
    <hashTree>
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Login Test">
        <intProp name="ThreadGroup.num_threads">20</intProp>
        <intProp name="ThreadGroup.ramp_time">5</intProp>
        <boolProp name="ThreadGroup.same_user_on_next_iteration">false</boolProp>
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller">
          <boolProp name="LoopController.continue_forever">false</boolProp>
          <intProp name="LoopController.loops">1</intProp>
        </elementProp>
      </ThreadGroup>
      <hashTree>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="Login Request">
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
            <collectionProp name="Arguments.arguments">
              <elementProp name="username" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">admin</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
                <boolProp name="HTTPArgument.use_equals">true</boolProp>
                <stringProp name="Argument.name">username</stringProp>
              </elementProp>
              <elementProp name="password" elementType="HTTPArgument">
                <boolProp name="HTTPArgument.always_encode">false</boolProp>
                <stringProp name="Argument.value">adminpass</stringProp>
                <stringProp name="Argument.metadata">=</stringProp>
                <boolProp name="HTTPArgument.use_equals">true</boolProp>
                <stringProp name="Argument.name">password</stringProp>
              </elementProp>
            </collectionProp>
          </elementProp>
          <stringProp name="HTTPSampler.domain">localhost</stringProp>
          <stringProp name="HTTPSampler.port">8000</stringProp>
          <stringProp name="HTTPSampler.path">/test/login/</stringProp>
          <stringProp name="HTTPSampler.method">POST</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
        </HTTPSamplerProxy>
        <hashTree>
          <JSONPostProcessor guiclass="JSONPostProcessorGui" testclass="JSONPostProcessor" testname="JSON Extractor - Success">
            <stringProp name="JSONPostProcessor.referenceNames">success</stringProp>
            <stringProp name="JSONPostProcessor.jsonPathExprs">$.success</stringProp>
            <stringProp name="JSONPostProcessor.match_numbers"></stringProp>
          </JSONPostProcessor>
          <hashTree/>
        </hashTree>
        <IfController guiclass="IfControllerPanel" testclass="IfController" testname="If Login Success">
          <stringProp name="IfController.condition">${success}==true</stringProp>
          <boolProp name="IfController.evaluateAll">false</boolProp>
        </IfController>
        <hashTree>
          <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="Dashboard JSON Request">
            <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
              <collectionProp name="Arguments.arguments">
                <elementProp name="format" elementType="HTTPArgument">
                  <boolProp name="HTTPArgument.always_encode">false</boolProp>
                  <stringProp name="Argument.value">json</stringProp>
                  <stringProp name="Argument.metadata">=</stringProp>
                  <boolProp name="HTTPArgument.use_equals">true</boolProp>
                  <stringProp name="Argument.name">format</stringProp>
                </elementProp>
              </collectionProp>
            </elementProp>
            <stringProp name="HTTPSampler.domain">localhost</stringProp>
            <stringProp name="HTTPSampler.port">8000</stringProp>
            <stringProp name="HTTPSampler.path">/test/dashboard/</stringProp>
            <stringProp name="HTTPSampler.method">GET</stringProp>
            <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
            <boolProp name="HTTPSampler.auto_redirects">false</boolProp>
            <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
            <boolProp name="HTTPSampler.DO_MULTIPART_POST">false</boolProp>
          </HTTPSamplerProxy>
          <hashTree/>
        </hashTree>
        <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="View Results Tree">
          <boolProp name="ResultCollector.error_logging">false</boolProp>
          <objProp>
            <name>saveConfig</name>
            <value class="SampleSaveConfiguration">
              <time>true</time>
              <latency>true</latency>
              <timestamp>true</timestamp>
              <success>true</success>
              <label>true</label>
              <code>true</code>
              <message>true</message>
              <threadName>true</threadName>
              <dataType>true</dataType>
              <encoding>false</encoding>
              <assertions>true</assertions>
              <subresults>true</subresults>
              <responseData>false</responseData>
              <samplerData>false</samplerData>
              <xml>false</xml>
              <fieldNames>true</fieldNames>
              <responseHeaders>false</responseHeaders>
              <requestHeaders>false</requestHeaders>
              <responseDataOnError>false</responseDataOnError>
              <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>
              <assertionsResultsToSave>0</assertionsResultsToSave>
              <bytes>true</bytes>
              <sentBytes>true</sentBytes>
              <url>true</url>
              <threadCounts>true</threadCounts>
              <idleTime>true</idleTime>
              <connectTime>true</connectTime>
            </value>
          </objProp>
          <stringProp name="filename"></stringProp>
        </ResultCollector>
        <hashTree/>
      </hashTree>
    </hashTree>
  </hashTree>
</jmeterTestPlan>
```