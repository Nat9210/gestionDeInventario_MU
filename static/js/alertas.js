/**
 * MÓDULO DE ALERTAS - JavaScript específico
 */

class AlertasManager {
    constructor() {
        this.init();
    }

    init() {
        this.setupMarcarComoVista();
        this.setupFiltroAlerta();
        this.setupRefreshAlerts();
    }

    setupMarcarComoVista() {
        const botonesVista = document.querySelectorAll('.btn-marcar-vista');
        botonesVista.forEach(btn => {
            btn.addEventListener('click', async (e) => {
                e.preventDefault();
                const alertaId = btn.dataset.alertaId;
                await this.marcarAlertaVista(alertaId, btn);
            });
        });
    }

    async marcarAlertaVista(alertaId, boton) {
        try {
            const formData = new FormData();
            formData.append('alerta_id', alertaId);
            formData.append('csrfmiddlewaretoken', document.querySelector('[name=csrfmiddlewaretoken]').value);

            const response = await fetch(window.location.href, {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                boton.textContent = 'Visto';
                boton.classList.remove('btn-outline-info');
                boton.classList.add('btn-success');
                boton.disabled = true;
                
                Utils.showToast('Alerta marcada como vista', 'success');
            }
        } catch (error) {
            console.error('Error:', error);
            Utils.showToast('Error al marcar alerta', 'error');
        }
    }

    setupFiltroAlerta() {
        const filtroEstado = document.getElementById('filtro-estado-alerta');
        if (filtroEstado) {
            filtroEstado.addEventListener('change', () => {
                this.filtrarAlertasPorEstado(filtroEstado.value);
            });
        }
    }

    filtrarAlertasPorEstado(estado) {
        const alertas = document.querySelectorAll('.alerta-card');
        alertas.forEach(alerta => {
            const esVista = alerta.classList.contains('vista');
            const mostrar = estado === 'todas' || 
                          (estado === 'activas' && !esVista) ||
                          (estado === 'vistas' && esVista);
            
            alerta.style.display = mostrar ? 'block' : 'none';
        });
    }

    setupRefreshAlerts() {
        // Auto-refresh cada 2 minutos para alertas críticas
        setInterval(() => {
            this.checkNuevasAlertas();
        }, 120000);
    }

    async checkNuevasAlertas() {
        // En una implementación real, esto haría una llamada AJAX
        // para verificar nuevas alertas sin recargar la página
        console.log('Verificando nuevas alertas...');
    }
}

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    if (document.querySelector('.alerta-card')) {
        new AlertasManager();
    }
});
