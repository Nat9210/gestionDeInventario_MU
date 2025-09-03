/**
 * SISTEMA DE INVENTARIO - JAVASCRIPT PRINCIPAL
 * Funcionalidades comunes del sistema
 */

// ===== CONFIGURACIÓN GLOBAL =====
const InventarioApp = {
    // URLs de la API
    urls: {
        stockPieza: document.querySelector('[data-stock-url]')?.dataset.stockUrl || '/movimientos/api/stock-pieza/',
    },
    
    // Configuración
    config: {
        animationDuration: 300,
        debounceDelay: 300,
    }
};

// ===== UTILIDADES GENERALES =====
const Utils = {
    /**
     * Debounce function para optimizar búsquedas
     */
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    /**
     * Mostrar toast notification
     */
    showToast(message, type = 'info') {
        const toastContainer = document.getElementById('toast-container') || this.createToastContainer();
        const toast = this.createToast(message, type);
        toastContainer.appendChild(toast);
        
        // Mostrar toast
        setTimeout(() => toast.classList.add('show'), 100);
        
        // Ocultar después de 3 segundos
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    },

    createToastContainer() {
        const container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'position-fixed top-0 end-0 p-3';
        container.style.zIndex = '1070';
        document.body.appendChild(container);
        return container;
    },

    createToast(message, type) {
        const colors = {
            success: 'bg-success',
            error: 'bg-danger', 
            warning: 'bg-warning',
            info: 'bg-info'
        };

        const toast = document.createElement('div');
        toast.className = `toast align-items-center text-white ${colors[type] || colors.info}`;
        toast.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">${message}</div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" onclick="this.parentElement.parentElement.remove()"></button>
            </div>
        `;
        return toast;
    },

    /**
     * Formatear números
     */
    formatNumber(num) {
        return new Intl.NumberFormat('es-CL').format(num);
    },

    /**
     * Formatear fecha
     */
    formatDate(date) {
        return new Intl.DateTimeFormat('es-CL', {
            day: '2-digit',
            month: '2-digit', 
            year: 'numeric'
        }).format(new Date(date));
    }
};

// ===== GESTIÓN DE STOCK =====
const StockManager = {
    /**
     * Obtener stock actual de una pieza
     */
    async obtenerStock(piezaId) {
        try {
            const response = await fetch(`${InventarioApp.urls.stockPieza}?pieza_id=${piezaId}`);
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'Error al obtener stock');
            }
            
            return data;
        } catch (error) {
            console.error('Error:', error);
            Utils.showToast('Error al obtener información de stock', 'error');
            return null;
        }
    },

    /**
     * Actualizar indicador visual de stock
     */
    actualizarIndicadorStock(elemento, stockData) {
        if (!stockData) {
            elemento.textContent = 'Error al obtener stock';
            elemento.className = 'form-control bg-danger text-white';
            return;
        }

        elemento.textContent = `${Utils.formatNumber(stockData.stock_actual)} unidades`;
        elemento.className = 'form-control bg-light';
        
        // Añadir clase según estado de stock
        if (stockData.stock_actual === 0) {
            elemento.classList.add('text-danger');
        } else if (stockData.stock_actual <= stockData.stock_minimo) {
            elemento.classList.add('text-warning');
        } else {
            elemento.classList.add('text-success');
        }
    }
};

// ===== FILTROS DINÁMICOS =====
const FiltrosManager = {
    init() {
        this.setupBuscadorInstantaneo();
        this.setupFiltrosAvanzados();
    },

    setupBuscadorInstantaneo() {
        const buscador = document.querySelector('input[name="busqueda"]');
        if (!buscador) return;

        const debouncedSearch = Utils.debounce(() => {
            this.filtrarTabla(buscador.value);
        }, InventarioApp.config.debounceDelay);

        buscador.addEventListener('input', debouncedSearch);
    },

    filtrarTabla(termino) {
        const tabla = document.querySelector('table tbody');
        if (!tabla) return;

        const filas = tabla.querySelectorAll('tr');
        let visibles = 0;

        filas.forEach(fila => {
            const texto = fila.textContent.toLowerCase();
            const coincide = texto.includes(termino.toLowerCase());
            
            fila.style.display = coincide ? '' : 'none';
            if (coincide) visibles++;
        });

        this.actualizarContadorResultados(visibles);
    },

    actualizarContadorResultados(cantidad) {
        let contador = document.querySelector('.resultado-contador');
        if (!contador) {
            contador = document.createElement('p');
            contador.className = 'text-muted resultado-contador';
            document.querySelector('.card-body')?.appendChild(contador);
        }
        contador.innerHTML = `<i class="bi bi-info-circle"></i> Se encontraron ${cantidad} resultado(s).`;
    },

    setupFiltrosAvanzados() {
        const filtros = document.querySelectorAll('select[name^="filtro_"]');
        filtros.forEach(filtro => {
            filtro.addEventListener('change', () => {
                // Aquí se puede implementar filtrado más avanzado
                console.log(`Filtro ${filtro.name} cambiado a:`, filtro.value);
            });
        });
    }
};

// ===== FORMULARIOS INTELIGENTES =====
const FormManager = {
    init() {
        this.setupValidacionEnTiempoReal();
        this.setupAutocompletado();
        this.setupMovimientos();
    },

    setupValidacionEnTiempoReal() {
        const formularios = document.querySelectorAll('form');
        formularios.forEach(form => {
            const campos = form.querySelectorAll('input, select, textarea');
            campos.forEach(campo => {
                campo.addEventListener('blur', () => this.validarCampo(campo));
            });
        });
    },

    validarCampo(campo) {
        // Limpiar validaciones previas
        campo.classList.remove('is-valid', 'is-invalid');
        
        // Validaciones específicas
        if (campo.required && !campo.value.trim()) {
            this.mostrarError(campo, 'Este campo es obligatorio');
            return false;
        }

        if (campo.type === 'number' && campo.value < 0) {
            this.mostrarError(campo, 'El valor debe ser positivo');
            return false;
        }

        // Campo válido
        campo.classList.add('is-valid');
        this.limpiarError(campo);
        return true;
    },

    mostrarError(campo, mensaje) {
        campo.classList.add('is-invalid');
        
        let feedbackDiv = campo.parentNode.querySelector('.invalid-feedback');
        if (!feedbackDiv) {
            feedbackDiv = document.createElement('div');
            feedbackDiv.className = 'invalid-feedback';
            campo.parentNode.appendChild(feedbackDiv);
        }
        feedbackDiv.textContent = mensaje;
    },

    limpiarError(campo) {
        const feedbackDiv = campo.parentNode.querySelector('.invalid-feedback');
        if (feedbackDiv) {
            feedbackDiv.remove();
        }
    },

    setupMovimientos() {
        const piezaSelect = document.getElementById('pieza-select');
        const stockDisplay = document.getElementById('stock-actual');
        
        if (piezaSelect && stockDisplay) {
            piezaSelect.addEventListener('change', async () => {
                const piezaId = piezaSelect.value;
                
                if (!piezaId) {
                    stockDisplay.textContent = 'Seleccione una pieza para ver el stock';
                    stockDisplay.className = 'form-control bg-light';
                    return;
                }

                // Mostrar loading
                stockDisplay.textContent = 'Cargando...';
                stockDisplay.className = 'form-control bg-light loading';

                // Obtener stock
                const stockData = await StockManager.obtenerStock(piezaId);
                StockManager.actualizarIndicadorStock(stockDisplay, stockData);
                
                // Remover loading
                stockDisplay.classList.remove('loading');
            });
        }
    }
};

// ===== DASHBOARD DINÁMICO =====
const DashboardManager = {
    init() {
        this.setupRefreshButton();
        this.setupAutoRefresh();
        this.animateCards();
    },

    setupRefreshButton() {
        const refreshBtn = document.getElementById('refresh-dashboard');
        if (refreshBtn) {
            refreshBtn.addEventListener('click', () => {
                this.refreshData();
            });
        }
    },

    async refreshData() {
        Utils.showToast('Actualizando datos...', 'info');
        
        // Simular actualización (en producción sería una llamada AJAX)
        setTimeout(() => {
            Utils.showToast('Datos actualizados', 'success');
            this.animateCards();
        }, 1000);
    },

    setupAutoRefresh() {
        // Actualizar cada 5 minutos
        setInterval(() => {
            this.refreshData();
        }, 300000);
    },

    animateCards() {
        const cards = document.querySelectorAll('.stat-card');
        cards.forEach((card, index) => {
            setTimeout(() => {
                card.classList.add('fade-in');
            }, index * 100);
        });
    }
};

// ===== INICIALIZACIÓN =====
document.addEventListener('DOMContentLoaded', function() {
    // Inicializar módulos
    FiltrosManager.init();
    FormManager.init();
    DashboardManager.init();
    
    // Configurar tooltips de Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    console.log('💼 Sistema de Inventario iniciado correctamente');
});
