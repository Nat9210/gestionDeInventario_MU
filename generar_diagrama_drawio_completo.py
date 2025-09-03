"""
Script completo para generar diagrama Draw.io del modelo de datos
Sistema de Inventario MVP - Maestranzas Unidas S.A.
"""

def generar_xml_drawio_completo():
    """Genera XML completo de Draw.io con el modelo de datos real"""
    
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2025-06-28T00:00:00.000Z" agent="Script Python" etag="generar_inventario_mvp" version="21.6.5">
  <diagram name="Modelo de Datos - Inventario MVP" id="modelo-inventario-mvp">
    <mxGraphModel dx="1661" dy="927" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- ==================== ENCABEZADO ==================== -->
        <mxCell id="header" value="&lt;h1 style=&quot;color:#1976D2;&quot;&gt;Sistema de Inventario MVP&lt;/h1&gt;&lt;h2 style=&quot;color:#388E3C;&quot;&gt;Modelo de Datos&lt;/h2&gt;&lt;p style=&quot;color:#666;&quot;&gt;Maestranzas Unidas S.A. - Junio 2025&lt;/p&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F8F9FA;strokeColor=none;align=left;verticalAlign=top;spacingLeft=20;spacingTop=10;" vertex="1" parent="1">
          <mxGeometry x="30" y="20" width="500" height="80" as="geometry"/>
        </mxCell>
        
        <!-- ==================== TABLA USUARIOS ==================== -->
        <mxCell id="tabla_usuarios" value="&lt;div style=&quot;font-size: 16px; font-weight: bold; color: #1976D2; padding: 8px; background-color: #E3F2FD; border-radius: 5px 5px 0 0;&quot;&gt;👥 usuarios_usuario&lt;/div&gt;
&lt;div style=&quot;font-size: 11px; text-align: left; padding: 8px; line-height: 1.4;&quot;&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #FFEB3B; border-left: 3px solid #F57F17;&quot;&gt;
&lt;b&gt;🔑 id&lt;/b&gt; (BIGINT AUTO_INCREMENT)
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📧 &lt;b&gt;username&lt;/b&gt; (VARCHAR(150)) 🔹 UNIQUE&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;🔒 password (VARCHAR(128))&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📧 email (VARCHAR(254))&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;👤 first_name (VARCHAR(150))&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;👤 last_name (VARCHAR(150))&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; color: #1976D2; font-weight: bold;&quot;&gt;🎭 &lt;b&gt;perfil&lt;/b&gt; (VARCHAR(20))&lt;/div&gt;
&lt;div style=&quot;margin-left: 15px; font-size: 10px; color: #666;&quot;&gt;• administrador, logistica, inventario&lt;br&gt;• auditor, comprador, produccion&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;✅ is_active (BOOLEAN)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;👔 is_staff (BOOLEAN)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;⭐ is_superuser (BOOLEAN)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📅 date_joined (DATETIME)&lt;/div&gt;
&lt;div&gt;⏰ last_login (DATETIME) NULL&lt;/div&gt;
&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;strokeWidth=2;verticalAlign=top;spacingTop=0;" vertex="1" parent="1">
          <mxGeometry x="50" y="130" width="300" height="280" as="geometry"/>
        </mxCell>
        
        <!-- ==================== TABLA PIEZAS ==================== -->
        <mxCell id="tabla_piezas" value="&lt;div style=&quot;font-size: 16px; font-weight: bold; color: #388E3C; padding: 8px; background-color: #E8F5E8; border-radius: 5px 5px 0 0;&quot;&gt;📦 inventario_pieza&lt;/div&gt;
&lt;div style=&quot;font-size: 11px; text-align: left; padding: 8px; line-height: 1.4;&quot;&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #FFEB3B; border-left: 3px solid #F57F17;&quot;&gt;
&lt;b&gt;🔑 id&lt;/b&gt; (BIGINT AUTO_INCREMENT)
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;🏷️ &lt;b&gt;codigo&lt;/b&gt; (VARCHAR(50)) 🔹 UNIQUE&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📄 descripcion (TEXT)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; color: #388E3C; font-weight: bold;&quot;&gt;📈 &lt;b&gt;stock_actual&lt;/b&gt; (INT UNSIGNED)&lt;/div&gt;
&lt;div style=&quot;margin-left: 15px; font-size: 10px; color: #666;&quot;&gt;DEFAULT 0, NOT NULL&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; color: #FF9800; font-weight: bold;&quot;&gt;⚠️ &lt;b&gt;stock_minimo&lt;/b&gt; (INT UNSIGNED)&lt;/div&gt;
&lt;div style=&quot;margin-left: 15px; font-size: 10px; color: #666;&quot;&gt;DEFAULT 10, NOT NULL&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📍 ubicacion (VARCHAR(100))&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;🗂️ categoria (VARCHAR(50)) NULL&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📅 fecha_creacion (DATETIME)&lt;/div&gt;
&lt;div&gt;🔄 fecha_actualizacion (DATETIME)&lt;/div&gt;
&lt;div style=&quot;margin-top: 8px; padding: 4px; background-color: #FFF9C4; border-left: 3px solid #F9A825;&quot;&gt;
&lt;b&gt;💡 Propiedades Calculadas:&lt;/b&gt;&lt;br&gt;
• stock_critico = stock_actual ≤ stock_minimo&lt;br&gt;
• estado_stock = &#39;Sin stock&#39; | &#39;Crítico&#39; | &#39;Normal&#39;
&lt;/div&gt;
&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#388E3C;strokeWidth=2;verticalAlign=top;spacingTop=0;" vertex="1" parent="1">
          <mxGeometry x="450" y="130" width="320" height="330" as="geometry"/>
        </mxCell>
        
        <!-- ==================== TABLA MOVIMIENTOS ==================== -->
        <mxCell id="tabla_movimientos" value="&lt;div style=&quot;font-size: 16px; font-weight: bold; color: #F57C00; padding: 8px; background-color: #FFF3E0; border-radius: 5px 5px 0 0;&quot;&gt;🔄 movimientos_movimientostock&lt;/div&gt;
&lt;div style=&quot;font-size: 11px; text-align: left; padding: 8px; line-height: 1.4;&quot;&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #FFEB3B; border-left: 3px solid #F57F17;&quot;&gt;
&lt;b&gt;🔑 id&lt;/b&gt; (BIGINT AUTO_INCREMENT)
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #E1F5FE; border-left: 3px solid #0288D1;&quot;&gt;
&lt;b&gt;🔗 pieza_id&lt;/b&gt; (BIGINT) FOREIGN KEY
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #E1F5FE; border-left: 3px solid #0288D1;&quot;&gt;
&lt;b&gt;🔗 usuario_id&lt;/b&gt; (BIGINT) FOREIGN KEY
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; color: #F57C00; font-weight: bold;&quot;&gt;🔄 &lt;b&gt;tipo_movimiento&lt;/b&gt; (VARCHAR(10))&lt;/div&gt;
&lt;div style=&quot;margin-left: 15px; font-size: 10px; color: #666;&quot;&gt;CHOICES: &#39;entrada&#39;, &#39;salida&#39;&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; color: #F57C00; font-weight: bold;&quot;&gt;📊 &lt;b&gt;cantidad&lt;/b&gt; (INT UNSIGNED)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;⏰ fecha_movimiento (DATETIME)&lt;/div&gt;
&lt;div style=&quot;margin-left: 15px; font-size: 10px; color: #666;&quot;&gt;AUTO_NOW_ADD&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📝 observaciones (TEXT) NULL&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; color: #795548;&quot;&gt;📈 &lt;b&gt;stock_anterior&lt;/b&gt; (INT UNSIGNED)&lt;/div&gt;
&lt;div style=&quot;color: #795548;&quot;&gt;📉 &lt;b&gt;stock_posterior&lt;/b&gt; (INT UNSIGNED)&lt;/div&gt;
&lt;div style=&quot;margin-top: 8px; padding: 4px; background-color: #FFF9C4; border-left: 3px solid #F9A825;&quot;&gt;
&lt;b&gt;⚙️ Automatización:&lt;/b&gt;&lt;br&gt;
• Actualiza stock_actual en Pieza&lt;br&gt;
• Genera AlertaStock si stock crítico&lt;br&gt;
• Registra trazabilidad completa
&lt;/div&gt;
&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#F57C00;strokeWidth=2;verticalAlign=top;spacingTop=0;" vertex="1" parent="1">
          <mxGeometry x="200" y="500" width="350" height="300" as="geometry"/>
        </mxCell>
        
        <!-- ==================== TABLA ALERTAS ==================== -->
        <mxCell id="tabla_alertas" value="&lt;div style=&quot;font-size: 16px; font-weight: bold; color: #D32F2F; padding: 8px; background-color: #FFEBEE; border-radius: 5px 5px 0 0;&quot;&gt;🚨 inventario_alertastock&lt;/div&gt;
&lt;div style=&quot;font-size: 11px; text-align: left; padding: 8px; line-height: 1.4;&quot;&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #FFEB3B; border-left: 3px solid #F57F17;&quot;&gt;
&lt;b&gt;🔑 id&lt;/b&gt; (BIGINT AUTO_INCREMENT)
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #E1F5FE; border-left: 3px solid #0288D1;&quot;&gt;
&lt;b&gt;🔗 pieza_id&lt;/b&gt; (BIGINT) FOREIGN KEY
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;📅 fecha_alerta (DATETIME)&lt;/div&gt;
&lt;div style=&quot;margin-left: 15px; font-size: 10px; color: #666;&quot;&gt;AUTO_NOW_ADD&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; color: #D32F2F; font-weight: bold;&quot;&gt;🔔 &lt;b&gt;activa&lt;/b&gt; (BOOLEAN)&lt;/div&gt;
&lt;div style=&quot;margin-left: 15px; font-size: 10px; color: #666;&quot;&gt;DEFAULT TRUE&lt;/div&gt;
&lt;div style=&quot;margin-top: 8px; padding: 4px; background-color: #FFF9C4; border-left: 3px solid #F9A825;&quot;&gt;
&lt;b&gt;🔗 Relación M2M:&lt;/b&gt;&lt;br&gt;
vista_por → usuarios_usuario&lt;br&gt;
(Tabla intermedia automática)
&lt;/div&gt;
&lt;div style=&quot;margin-top: 8px; padding: 4px; background-color: #FFCDD2; border-left: 3px solid #F44336;&quot;&gt;
&lt;b&gt;⚡ Trigger:&lt;/b&gt;&lt;br&gt;
Se crea automáticamente cuando&lt;br&gt;
stock_actual ≤ stock_minimo
&lt;/div&gt;
&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#D32F2F;strokeWidth=2;verticalAlign=top;spacingTop=0;" vertex="1" parent="1">
          <mxGeometry x="650" y="500" width="280" height="240" as="geometry"/>
        </mxCell>
        
        <!-- ==================== TABLA INTERMEDIA M2M ==================== -->
        <mxCell id="tabla_m2m" value="&lt;div style=&quot;font-size: 14px; font-weight: bold; color: #7B1FA2; padding: 6px; background-color: #F3E5F5; border-radius: 5px 5px 0 0;&quot;&gt;🔗 inventario_alertastock_vista_por&lt;/div&gt;
&lt;div style=&quot;font-size: 10px; text-align: left; padding: 6px; line-height: 1.4;&quot;&gt;
&lt;div style=&quot;margin-bottom: 6px; padding: 3px; background-color: #FFEB3B; border-left: 2px solid #F57F17;&quot;&gt;
&lt;b&gt;🔑 id&lt;/b&gt; (BIGINT AUTO_INCREMENT)
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px; padding: 3px; background-color: #E1F5FE; border-left: 2px solid #0288D1;&quot;&gt;&lt;b&gt;🔗 alertastock_id&lt;/b&gt; (BIGINT) FK&lt;/div&gt;
&lt;div style=&quot;padding: 3px; background-color: #E1F5FE; border-left: 2px solid #0288D1;&quot;&gt;&lt;b&gt;🔗 usuario_id&lt;/b&gt; (BIGINT) FK&lt;/div&gt;
&lt;div style=&quot;margin-top: 6px; font-size: 9px; color: #666; font-style: italic;&quot;&gt;
Tabla intermedia automática&lt;br&gt;
para relación Many-To-Many
&lt;/div&gt;
&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F3E5F5;strokeColor=#7B1FA2;strokeWidth=1;verticalAlign=top;spacingTop=0;" vertex="1" parent="1">
          <mxGeometry x="980" y="580" width="220" height="130" as="geometry"/>
        </mxCell>
        
        <!-- ==================== RELACIONES ==================== -->
        
        <!-- Relación Usuario -> Movimiento -->
        <mxCell id="rel_user_mov" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=3;strokeColor=#1976D2;endArrow=classic;endFill=1;" edge="1" parent="1" source="tabla_usuarios" target="tabla_movimientos">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="200" y="410" as="sourcePoint"/>
            <mxPoint x="300" y="500" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="rel_user_mov_label" value="&lt;div style=&quot;font-weight: bold; font-size: 12px; color: #1976D2; background-color: white; padding: 2px 8px; border: 2px solid #1976D2; border-radius: 8px;&quot;&gt;1:N&lt;/div&gt;&lt;div style=&quot;font-size: 10px; color: #666; margin-top: 2px;&quot;&gt;registra&lt;/div&gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="rel_user_mov">
          <mxGeometry x="-0.2" y="-2" relative="1" as="geometry">
            <mxPoint x="15" y="-15" as="offset"/>
          </mxGeometry>
        </mxCell>
        
        <!-- Relación Pieza -> Movimiento -->
        <mxCell id="rel_pieza_mov" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=3;strokeColor=#388E3C;endArrow=classic;endFill=1;" edge="1" parent="1" source="tabla_piezas" target="tabla_movimientos">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="610" y="460" as="sourcePoint"/>
            <mxPoint x="450" y="500" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="rel_pieza_mov_label" value="&lt;div style=&quot;font-weight: bold; font-size: 12px; color: #388E3C; background-color: white; padding: 2px 8px; border: 2px solid #388E3C; border-radius: 8px;&quot;&gt;1:N&lt;/div&gt;&lt;div style=&quot;font-size: 10px; color: #666; margin-top: 2px;&quot;&gt;tiene movimientos&lt;/div&gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="rel_pieza_mov">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
            <mxPoint x="25" y="-15" as="offset"/>
          </mxGeometry>
        </mxCell>
        
        <!-- Relación Pieza -> Alerta -->
        <mxCell id="rel_pieza_alerta" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=3;strokeColor=#D32F2F;endArrow=classic;endFill=1;" edge="1" parent="1" source="tabla_piezas" target="tabla_alertas">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="700" y="460" as="sourcePoint"/>
            <mxPoint x="750" y="500" as="targetPoint"/>
          </mxGeometry>
        </mxCell>
        <mxCell id="rel_pieza_alerta_label" value="&lt;div style=&quot;font-weight: bold; font-size: 12px; color: #D32F2F; background-color: white; padding: 2px 8px; border: 2px solid #D32F2F; border-radius: 8px;&quot;&gt;1:N&lt;/div&gt;&lt;div style=&quot;font-size: 10px; color: #666; margin-top: 2px;&quot;&gt;genera alertas&lt;/div&gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="rel_pieza_alerta">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry">
            <mxPoint x="15" y="-15" as="offset"/>
          </mxGeometry>
        </mxCell>
        
        <!-- Relación Alerta -> Usuario (M2M) -->
        <mxCell id="rel_alerta_user" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#7B1FA2;endArrow=classic;endFill=1;dashed=1;" edge="1" parent="1" source="tabla_alertas" target="tabla_m2m">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="rel_alerta_user_label" value="&lt;div style=&quot;font-weight: bold; font-size: 11px; color: #7B1FA2; background-color: white; padding: 2px 6px; border: 1px solid #7B1FA2; border-radius: 6px;&quot;&gt;1:N&lt;/div&gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="rel_alerta_user">
          <mxGeometry x="-0.1" y="1" relative="1" as="geometry"/>
        </mxCell>
        
        <!-- Relación Usuario -> M2M -->
        <mxCell id="rel_user_m2m" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#7B1FA2;endArrow=classic;endFill=1;dashed=1;" edge="1" parent="1" source="tabla_usuarios" target="tabla_m2m">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="200" y="450"/>
              <mxPoint x="1090" y="450"/>
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="rel_user_m2m_label" value="&lt;div style=&quot;font-weight: bold; font-size: 11px; color: #7B1FA2; background-color: white; padding: 2px 6px; border: 1px solid #7B1FA2; border-radius: 6px;&quot;&gt;M:N&lt;/div&gt;&lt;div style=&quot;font-size: 9px; color: #666; margin-top: 1px;&quot;&gt;vista_por&lt;/div&gt;" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="rel_user_m2m">
          <mxGeometry x="0.7" y="1" relative="1" as="geometry">
            <mxPoint x="-10" y="-10" as="offset"/>
          </mxGeometry>
        </mxCell>
        
        <!-- ==================== LEYENDA ==================== -->
        <mxCell id="leyenda" value="&lt;h3 style=&quot;color: #37474F; margin-bottom: 10px;&quot;&gt;📋 Leyenda del Modelo&lt;/h3&gt;
&lt;div style=&quot;font-size: 11px; line-height: 1.6;&quot;&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #FFEB3B; border-left: 3px solid #F57F17;&quot;&gt;
&lt;b&gt;🔑 Primary Key (PK)&lt;/b&gt; - Clave Primaria
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 8px; padding: 4px; background-color: #E1F5FE; border-left: 3px solid #0288D1;&quot;&gt;
&lt;b&gt;🔗 Foreign Key (FK)&lt;/b&gt; - Clave Foránea
&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 4px;&quot;&gt;&lt;b&gt;🔹 UNIQUE&lt;/b&gt; - Campo único (sin duplicados)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 4px;&quot;&gt;&lt;b&gt;📦 Campos de Negocio&lt;/b&gt; - Datos principales&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 4px;&quot;&gt;&lt;b&gt;⏰ Timestamps&lt;/b&gt; - Fechas automáticas&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 4px;&quot;&gt;&lt;b&gt;🎭 Choices&lt;/b&gt; - Valores predefinidos&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 8px;&quot;&gt;&lt;b&gt;NULL&lt;/b&gt; - Campo opcional&lt;/div&gt;

&lt;h4 style=&quot;color: #37474F; margin: 15px 0 8px 0;&quot;&gt;🔄 Tipos de Relación:&lt;/h4&gt;
&lt;div style=&quot;margin-bottom: 4px;&quot;&gt;&lt;b&gt;1:N&lt;/b&gt; - Uno a Muchos (línea sólida)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 4px;&quot;&gt;&lt;b&gt;M:N&lt;/b&gt; - Muchos a Muchos (línea punteada)&lt;/div&gt;

&lt;h4 style=&quot;color: #37474F; margin: 15px 0 8px 0;&quot;&gt;🎨 Código de Colores:&lt;/h4&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;🔵 &lt;b&gt;Azul&lt;/b&gt; - Usuarios y Autenticación&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;🟢 &lt;b&gt;Verde&lt;/b&gt; - Inventario y Piezas&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;🟠 &lt;b&gt;Naranja&lt;/b&gt; - Movimientos y Trazabilidad&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 2px;&quot;&gt;🔴 &lt;b&gt;Rojo&lt;/b&gt; - Alertas y Notificaciones&lt;/div&gt;
&lt;div&gt;🟣 &lt;b&gt;Morado&lt;/b&gt; - Relaciones Many-to-Many&lt;/div&gt;
&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8F9FA;strokeColor=#90A4AE;strokeWidth=1;verticalAlign=top;spacingTop=10;spacingLeft=15;spacingRight=15;" vertex="1" parent="1">
          <mxGeometry x="980" y="130" width="300" height="400" as="geometry"/>
        </mxCell>
        
        <!-- ==================== INFORMACIÓN TÉCNICA ==================== -->
        <mxCell id="info_tecnica" value="&lt;h3 style=&quot;color: #37474F; margin-bottom: 10px;&quot;&gt;⚙️ Información Técnica&lt;/h3&gt;
&lt;div style=&quot;font-size: 10px; line-height: 1.5;&quot;&gt;
&lt;div style=&quot;margin-bottom: 6px;&quot;&gt;&lt;b&gt;🗄️ Motor de BD:&lt;/b&gt; SQLite (desarrollo) / MySQL (producción)&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 6px;&quot;&gt;&lt;b&gt;🔧 Framework:&lt;/b&gt; Django 5.2.3 ORM&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 6px;&quot;&gt;&lt;b&gt;📅 Versión:&lt;/b&gt; 1.0 - Junio 2025&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 6px;&quot;&gt;&lt;b&gt;👥 Usuario Base:&lt;/b&gt; AbstractUser extendido&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 6px;&quot;&gt;&lt;b&gt;🔒 Seguridad:&lt;/b&gt; Perfiles y permisos por rol&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 6px;&quot;&gt;&lt;b&gt;🚀 Auto-migraciones:&lt;/b&gt; Django Migrations&lt;/div&gt;
&lt;div style=&quot;margin-bottom: 6px;&quot;&gt;&lt;b&gt;📊 Índices:&lt;/b&gt; Optimizados para consultas frecuentes&lt;/div&gt;
&lt;div&gt;&lt;b&gt;⚡ Triggers:&lt;/b&gt; Alertas automáticas por stock crítico&lt;/div&gt;
&lt;/div&gt;" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ECEFF1;strokeColor=#546E7A;strokeWidth=1;verticalAlign=top;spacingTop=10;spacingLeft=15;" vertex="1" parent="1">
          <mxGeometry x="30" y="440" width="140" height="200" as="geometry"/>
        </mxCell>
        
        <!-- ==================== PIE DE PÁGINA ==================== -->
        <mxCell id="footer" value="&lt;div style=&quot;font-size: 9px; color: #666; text-align: center; font-style: italic;&quot;&gt;
📋 Diagrama generado automáticamente desde modelos Django&lt;br&gt;
🏢 Maestranzas Unidas S.A. - Sistema de Inventario MVP&lt;br&gt;
📅 Fecha: 28 de Junio de 2025 - Versión: 1.0&lt;br&gt;
👨‍💻 Generado por: Script Python automatizado
&lt;/div&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=none;align=center;" vertex="1" parent="1">
          <mxGeometry x="30" y="830" width="1250" height="50" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return xml_content

def generar_version_simplificada():
    """Genera una versión más simple del diagrama"""
    
    xml_simple = '''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="Modelo Simple">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1169" pageHeight="827">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Usuarios -->
        <mxCell id="usuarios" value="&lt;b&gt;👥 usuarios_usuario&lt;/b&gt;&lt;hr&gt;🔑 id&lt;br&gt;📧 username (unique)&lt;br&gt;🎭 perfil&lt;br&gt;📧 email&lt;br&gt;🔒 password" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1976D2;" vertex="1" parent="1">
          <mxGeometry x="80" y="80" width="180" height="120" as="geometry"/>
        </mxCell>
        
        <!-- Piezas -->
        <mxCell id="piezas" value="&lt;b&gt;📦 inventario_pieza&lt;/b&gt;&lt;hr&gt;🔑 id&lt;br&gt;🏷️ codigo (unique)&lt;br&gt;📄 descripcion&lt;br&gt;📈 stock_actual&lt;br&gt;⚠️ stock_minimo&lt;br&gt;📍 ubicacion" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E8;strokeColor=#388E3C;" vertex="1" parent="1">
          <mxGeometry x="400" y="80" width="180" height="140" as="geometry"/>
        </mxCell>
        
        <!-- Movimientos -->
        <mxCell id="movimientos" value="&lt;b&gt;🔄 movimientos_movimientostock&lt;/b&gt;&lt;hr&gt;🔑 id&lt;br&gt;🔗 pieza_id (FK)&lt;br&gt;🔗 usuario_id (FK)&lt;br&gt;🔄 tipo_movimiento&lt;br&gt;📊 cantidad&lt;br&gt;⏰ fecha_movimiento&lt;br&gt;📈 stock_anterior&lt;br&gt;📉 stock_posterior" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF3E0;strokeColor=#F57C00;" vertex="1" parent="1">
          <mxGeometry x="200" y="280" width="220" height="160" as="geometry"/>
        </mxCell>
        
        <!-- Alertas -->
        <mxCell id="alertas" value="&lt;b&gt;🚨 inventario_alertastock&lt;/b&gt;&lt;hr&gt;🔑 id&lt;br&gt;🔗 pieza_id (FK)&lt;br&gt;📅 fecha_alerta&lt;br&gt;🔔 activa&lt;br&gt;👥 vista_por (M2M)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFEBEE;strokeColor=#D32F2F;" vertex="1" parent="1">
          <mxGeometry x="480" y="300" width="180" height="120" as="geometry"/>
        </mxCell>
        
        <!-- Relaciones -->
        <mxCell id="r1" value="1:N" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="usuarios" target="movimientos">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="r2" value="1:N" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="piezas" target="movimientos">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="r3" value="1:N" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" edge="1" parent="1" source="piezas" target="alertas">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    
    return xml_simple

def main():
    """Función principal"""
    print("🚀 GENERADOR DE DIAGRAMA DRAW.IO - SISTEMA INVENTARIO MVP")
    print("=" * 60)
    print("📋 Maestranzas Unidas S.A. - Modelo de Datos Completo")
    print()
    
    # Generar diagrama completo
    print("⚙️ Generando diagrama completo...")
    xml_completo = generar_xml_drawio_completo()
    
    # Guardar archivo completo
    with open("modelo_inventario_completo.drawio", "w", encoding="utf-8") as f:
        f.write(xml_completo)
    
    print("✅ Archivo 'modelo_inventario_completo.drawio' generado!")
    
    # Generar versión simplificada
    print("⚙️ Generando versión simplificada...")
    xml_simple = generar_version_simplificada()
    
    # Guardar archivo simple
    with open("modelo_inventario_simple.drawio", "w", encoding="utf-8") as f:
        f.write(xml_simple)
    
    print("✅ Archivo 'modelo_inventario_simple.drawio' generado!")
    
    print()
    print("📁 INSTRUCCIONES DE USO:")
    print("-" * 30)
    print("1. Ve a https://app.diagrams.net/")
    print("2. Selecciona 'File' → 'Open From' → 'Device'")
    print("3. Sube el archivo .drawio generado")
    print("4. ¡El diagrama se cargará automáticamente!")
    print()
    print("📊 ARCHIVOS GENERADOS:")
    print("• modelo_inventario_completo.drawio - Versión detallada con todos los campos")
    print("• modelo_inventario_simple.drawio - Versión simplificada para presentaciones")
    print()
    print("🎨 CARACTERÍSTICAS DEL DIAGRAMA:")
    print("• Colores diferenciados por tipo de tabla")
    print("• Iconos descriptivos para cada campo")
    print("• Relaciones claramente etiquetadas")
    print("• Leyenda completa incluida")
    print("• Información técnica detallada")
    print("• Propiedades calculadas documentadas")
    print("• Triggers y automatizaciones explicadas")
    print()
    print("🔧 PERSONALIZACIÓN:")
    print("Una vez importado en Draw.io, puedes:")
    print("• Mover y redimensionar tablas")
    print("• Cambiar colores y estilos")
    print("• Agregar notas adicionales")
    print("• Exportar como PNG, PDF, SVG")
    print()
    print("🎯 ¡Diagrama listo para usar en documentación y presentaciones!")

if __name__ == "__main__":
    main()