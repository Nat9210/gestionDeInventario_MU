from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from datetime import datetime
import django
from django.conf import settings

# Constantes para organización
SCREENSHOTS_DIR = os.path.join(os.getcwd(), "evidencias")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def before_all(context):
    # Configurar Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_mvp.settings')
    django.setup()
    
    # Configuración de screenshots
    context.screenshot_dir = SCREENSHOTS_DIR
    today = datetime.now().strftime("%Y-%m-%d")
    context.daily_screenshot_dir = os.path.join(SCREENSHOTS_DIR, today)
    os.makedirs(context.daily_screenshot_dir, exist_ok=True)
    
    context.base_url = "http://127.0.0.1:8000"
    
    # Configuración Chrome optimizada
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--remote-debugging-port=9222")
    
    # Mejoras para rendering consistente
    chrome_options.add_argument("--force-device-scale-factor=1")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    
    # Tamaño de ventana fijo para screenshots consistentes
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    
    # Inicializar browser
    context.browser = webdriver.Chrome(options=chrome_options)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

def after_all(context):
    """Limpieza final - cerrar navegador de forma segura"""
    try:
        if hasattr(context, 'browser') and context.browser:
            context.browser.quit()
            print(" Navegador cerrado correctamente")
    except Exception as e:
        print(f" Error cerrando navegador: {e}")
    finally:
        print(f" Evidencias guardadas en: {SCREENSHOTS_DIR}")

def take_screenshot(context, name_suffix=""):
    """Función para tomar capturas de pantalla con mejoras anti-blancos"""
    try:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        # Esperar un momento para que la página se renderice completamente
        time.sleep(1)
        
        # Verificar que el navegador esté respondiendo
        try:
            # Intentar obtener el título como prueba de que la página está cargada
            title = context.browser.title
            if not title or title == "":
                time.sleep(2)  # Esperar más si no hay título
        except:
            time.sleep(2)
        
        # Asegurar que el body esté visible (evita capturas completamente blancas)
        try:
            WebDriverWait(context.browser, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except:
            pass
        
        # Scroll al inicio para captura completa
        try:
            context.browser.execute_script("window.scrollTo(0, 0);")
            time.sleep(0.5)
        except:
            pass
        
        timestamp = datetime.now().strftime("%H-%M-%S")
        
        if hasattr(context, 'scenario'):
            scenario_name = context.scenario.name.replace(" ", "_").replace("-", "_").replace(":", "")
            # Limitar longitud del nombre para evitar problemas de path
            if len(scenario_name) > 50:
                scenario_name = scenario_name[:50]
            filename = f"{scenario_name}_{timestamp}{name_suffix}.png"
        else:
            filename = f"screenshot_{timestamp}{name_suffix}.png"
        
        filepath = os.path.join(context.daily_screenshot_dir, filename)
        
        # Intentar captura múltiples veces si es necesario
        for attempt in range(3):
            try:
                success = context.browser.save_screenshot(filepath)
                if success:
                    # Verificar que el archivo no esté vacío
                    if os.path.exists(filepath) and os.path.getsize(filepath) > 1000:  # Mínimo 1KB
                        print(f" Screenshot guardado: {filepath} (Intento {attempt + 1})")
                        return filepath
                    else:
                        print(f" Screenshot muy pequeño, reintentando... (Intento {attempt + 1})")
                        time.sleep(1)
                else:
                    print(f" Fallo en save_screenshot, reintentando... (Intento {attempt + 1})")
                    time.sleep(1)
            except Exception as e:
                print(f" Error en intento {attempt + 1}: {e}")
                time.sleep(1)
        
        print(f" No se pudo tomar screenshot válido después de 3 intentos")
        return None
        
    except Exception as e:
        print(f"Error crítico tomando screenshot: {e}")
        return None

def before_scenario(context, scenario):
    """Ejecutar antes de cada escenario"""
    context.scenario = scenario  # Guardar referencia para screenshots
    
    # Limpieza de datos de pruebas anteriores - CORREGIDO para usuarios.Usuario
    try:
        from usuarios.models import Usuario
        Usuario.objects.filter(username__startswith='test_').delete()
    except Exception as e:
        print(f"Advertencia: No se pudo limpiar usuarios de prueba: {e}")
    
    # Asegurar que estemos en una página válida antes del screenshot inicial
    try:
        current_url = context.browser.current_url
        if not current_url or current_url == "data:," or "about:blank" in current_url:
            context.browser.get(context.base_url)
            time.sleep(2)  # Esperar carga inicial
    except:
        context.browser.get(context.base_url)
        time.sleep(2)
    
    # Tomar screenshot inicial del escenario
    take_screenshot(context, "_START")

def after_step(context, step):
    """Ejecutar después de cada paso - capturas en caso de fallo"""
    if step.status == "failed":
        print(f" Step FAILED: {step.name}")
        
        # Información de debug antes de la captura
        try:
            current_url = context.browser.current_url
            page_title = context.browser.title
            print(f" URL actual: {current_url}")
            print(f" Título página: {page_title}")
        except Exception as e:
            print(f" Error obteniendo info de página: {e}")
        
        # Tomar captura con retry mejorado
        screenshot_path = take_screenshot(context, "_FAILED")
        if not screenshot_path:
            print(" No se pudo capturar screenshot del fallo")
        
        # Información adicional de debug
        try:
            page_source_length = len(context.browser.page_source)
            print(f" Tamaño del HTML: {page_source_length} caracteres")
        except:
            print(" No se pudo obtener el HTML de la página")

def after_scenario(context, scenario):
    """Ejecutar después de cada escenario - Captura SIEMPRE"""
    try:
        # Crear nombre de archivo descriptivo que incluya el estado
        feature_name = scenario.feature.name.replace(" ", "_").replace("-", "_")
        scenario_name = scenario.name.replace(" ", "_").replace("-", "_")
        scenario_status = scenario.status.name if hasattr(scenario.status, 'name') else str(scenario.status)
        
        # Timestamp para evitar conflictos
        timestamp = datetime.now().strftime("%H-%M-%S")
        
        # Nombre de archivo más descriptivo
        filename = f"{feature_name}_{scenario_name}_{scenario_status}_{timestamp}.png"
        screenshot_path = os.path.join(context.daily_screenshot_dir, filename)
        
        # Tomar captura SIEMPRE
        if hasattr(context, 'browser'):
            try:
                context.browser.save_screenshot(screenshot_path)
                print(f" Captura ({scenario_status}) guardada en: {screenshot_path}")
            except Exception as e:
                print(f" Error al guardar captura: {e}")
        
        # Solo limpiar cookies en scenarios de login para evitar interferencias
        if 'login' in scenario.name.lower():
            print(" Limpiando cookies después de test de login...")
            context.browser.delete_all_cookies()
            context.browser.get(f"{context.base_url}/")
        
        # Resumen del escenario
        status_icon = "" if scenario_status == "passed" else ""
        print(f"{status_icon} Escenario {scenario.name}: {scenario_status.upper()}")
        
    except Exception as e:
        print(f" Error in after_scenario: {e}")
