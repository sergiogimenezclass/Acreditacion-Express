# 🎨 Guía de Rediseño: Ecosistema Acreditación Express (Light Theme Edition)

Este documento define la identidad visual para la Noche de los Oficios. Buscamos un diseño minimalista, limpio y extremadamente profesional, optimizado para la claridad y la rapidez de carga.

## 🌈 Paleta de Colores (Clean & Minimal)
- **Primary (Corporate Blue):** `#2563EB` (Blue 600)
- **Secondary (Soft Slate):** `#64748B` (Slate 500 para textos secundarios)
- **Background:** `#F8FAFC` (Slate 50 - Un blanco grisáceo muy suave)
- **Cards/Surface:** `#FFFFFF` (Blanco puro con sombras suaves `shadow-sm`)
- **Accent (Success):** `#10B981` (Emerald 500 para el botón de exportar)

## 📱 Pantalla 1: Formulario Móvil (User Experience)
**Objetivo:** Claridad total y facilidad de uso bajo luz ambiente.
- **Header:** Fondo blanco con un borde inferior muy fino. Título en `Slate 900` con iconos modernos.
- **Campos del Formulario:** 
    - Inputs con fondo blanco, bordes finos en `Slate 200`.
    - Al hacer foco (focus), el borde cambia a `Blue 600` con un anillo de luz suave.
- **Botón:** Sólido en `Blue 600` con texto blanco en negrita.
- **UX:** El filtrado de cursos debe ser instantáneo. Los cursos aparecen en una lista limpia con radio-buttons o un select estilizado.

## 📺 Pantalla 2: Stand / Monitor (Impacto Visual)
**Objetivo:** Un monitor que se sienta como una ventana de bienvenida brillante.
- **Estado Inactivo:** 
    - Fondo blanco puro o con un gradiente muy sutil hacia el azul claro.
    - Código QR maquetado con bordes redondeados y una sombra suave para que "flote".
    - Texto: "Escaneá el código para registrarte" en `Slate 800`.
- **Efecto Bienvenida:** 
    - El fondo hace una transición rápida a un azul muy suave (`Blue 50`).
    - El mensaje de bienvenida aparece en el centro: "¡Hola [Nombre]! 👋 Bienvenido/a a la Noche de los Oficios".
    - **Confeti:** Colores vibrantes pero pasteles para mantener la estética limpia.

## 📊 Pantalla 3: Admin Dashboard (Efficiency Mode)
**Objetivo:** Un panel de control tipo "SaaS" moderno.
- **Seguridad:** Prompt de password al inicio.
- **Layout:** Fondo `Slate 50`, tarjetas de métricas en blanco puro con bordes redondeados.
- **Tabla:** Encabezados en gris claro, filas con líneas divisorias finas. Hover en las filas que cambie a un azul muy tenue.
- **Exportación:** Botón verde esmeralda con icono de descarga.

## 🛠️ Stack Sugerido para Stitch
- **Framework:** Tailwind CSS (sin modo dark activado).
- **Animaciones:** Transiciones de opacidad y escala suaves.
- **Icons:** Lucide Icons (stroke de 2px, color `Slate 700`).
