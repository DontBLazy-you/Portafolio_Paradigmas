+++
date = '2026-02-20T22:43:19-08:00'
draft = false
title = 'Practica 0: Manejo de Repositorios'
tags = []
+++

## Introducción

En la **Práctica 0: Manejo de Repositorios** aprendí el uso de herramientas básicas para la documentación, control de versiones y publicación de proyectos. Durante esta práctica trabajé con **Markdown, Git, GitHub, Hugo y GitHub Actions**, combinando estos conocimientos para crear y publicar una página web estática.

Este reporte corresponde a la **primera entrada de mi portafolio**, e incluye el enlace a mi repositorio en GitHub y a la página estática publicada.

---

## Desarrollo

- Utilicé **Markdown** para redactar un reporte donde describo qué es, cómo se usa y su sintaxis básica.
- Aprendí a usar **Git** y **GitHub** para crear repositorios, manejar versiones y subir el proyecto a la nube utilizando comandos esenciales.
- Añadí esa información al reporte.
- Integré estos conocimientos para generar un sitio estático con **Hugo**, automatizar su publicación mediante **GitHub Actions** y desplegarlo en **GitHub Pages**.
- Añadí cómo hacer lo anterior al reporte.

---

## Markdown: Definición, Uso y Sintaxis

### ¿Qué es Markdown?

**Markdown** es un lenguaje de marcado ligero creado en 2004 por **John Gruber** con la colaboración de **Aaron Swartz**. Su objetivo principal es lograr la máxima legibilidad y facilidad de publicación tanto en su forma de entrada como de salida, inspirándose en convenciones ya existentes para dar formato a mensajes de correo electrónico mediante texto plano.

A diferencia de los procesadores de texto tradicionales como Microsoft Word, **Markdown** permite añadir formatos como: **negritas**, *cursivas* o [enlaces](https://www.markdownguide.org/) utilizando únicamente texto plano, sin necesidad de botones ni menús visuales. Esto convierte la escritura en algo más simple, eficiente y portable.

El texto marcado con **Markdown** se convierte automáticamente en documentos HTML o XHTML válidos mediante un intérprete o procesador. Gruber implementó originalmente dicho procesador en el lenguaje de programación Perl, aunque desde entonces ha sido portado a PHP, Python, Ruby, Java y muchos otros lenguajes.

#### Características principales

- Basado en texto plano, compatible con cualquier dispositivo o sistema operativo.
- Sintaxis sencilla que puede aprenderse en minutos.
- Altamente legible aun sin procesar.
- Convertible a HTML, PDF, ePub y otros formatos mediante herramientas como Pandoc.
- Ampliamente adoptado en plataformas como GitHub, Reddit, Stack Overflow, Slack, WordPress y Trello.

### Sintaxis de Markdown

La sintaxis de Markdown se divide en elementos de bloque (que afectan secciones completas de texto) y elementos en línea (que afectan palabras o frases individuales). A continuación se presenta una guía completa de los elementos más importantes.

#### Encabezados

Los encabezados se crean usando el símbolo de almohadilla (#) al inicio de la línea, seguido de un espacio. Se pueden crear hasta seis niveles de encabezado, equivalentes a las etiquetas HTML `<h1>` a `<h6>`.

| **Sintaxis Markdown** | **Resultado**     | **Nivel HTML** |
|-----------------------|-------------------|----------------|
| `# Título principal`  | Encabezado nivel 1 | `<h1>`        |
| `## Subtítulo`        | Encabezado nivel 2 | `<h2>`        |
| `### Sección`         | Encabezado nivel 3 | `<h3>`        |
| `#### Subsección`     | Encabezado nivel 4 | `<h4>`        |
| `##### Apartado`      | Encabezado nivel 5 | `<h5>`        |
| `###### Nota`         | Encabezado nivel 6 | `<h6>`        |

#### Énfasis: negritas, cursivas y tachado

Para aplicar énfasis al texto se utilizan asteriscos (*) o guiones bajos (_). La cantidad de caracteres determina el tipo de énfasis.

| Sintaxis | Resultado |
|----------|-----------|
| `*texto en cursiva* o _texto en cursiva_` | *Texto en cursiva* |
| `**texto en negrita** o __texto en negrita__` | **Texto en negrita** |
| `***texto en negrita y cursiva***` | ***Texto en negrita y cursiva*** |
| `~~texto tachado~~` | ~~Texto tachado~~ |

#### Párrafos y saltos de línea

Un párrafo nuevo se genera dejando una línea en blanco entre dos bloques de texto. Para un salto de línea simple dentro del mismo párrafo, se deben agregar dos espacios al final de la línea antes de presionar Enter.

#### Listas

Markdown soporta listas ordenadas (numeradas) y no ordenadas (con viñetas).

##### Lista no ordenada

Se utiliza un asterisco (*), guion (-) o símbolo de suma (+) seguido de un espacio:

```markdown
- Elemento 1
- Elemento 2
- Elemento 3
```

- Elemento 1
- Elemento 2
- Elemento 3

##### Lista ordenada

Se utiliza un número seguido de un punto y un espacio:

```markdown
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
```

1. Primer elemento
2. Segundo elemento
3. Tercer elemento

#### Citas en bloque (Blockquotes)

Las citas se crean usando el signo mayor que (>) al inicio de cada línea del bloque citado. Pueden combinarse con otros elementos de Markdown como negritas o cursivas.

##### Sintaxis

```markdown
> Esta es una cita en bloque.
> El texto puede continuar en la siguiente línea.
>
> Y puede tener múltiples párrafos.
```

##### Resultado

> Esta es una cita en bloque.
> El texto puede continuar en la siguiente línea.
>
> Y puede tener múltiples párrafos.

#### Código

Markdown permite mostrar código tanto en línea como en bloques independientes.

##### Código en línea

Se utilizan acentos graves para marcar código dentro de un párrafo:

```markdown
Usa el comando `git push` para subir cambios.
```

Resultado: Usa el comando `git push` para subir cambios.

##### Bloque de código

Se utilizan tres acentos graves (```) para delimitar un bloque. Se puede especificar el lenguaje para resaltado de sintaxis:

````markdown
```python
print("Hola mundo")
```
````

#### Enlaces e imágenes

```markdown
[Texto del enlace](https://url.com)
![Texto alternativo](ruta/imagen.png)
```

#### Línea horizontal

Se crea con tres o más guiones, asteriscos o guiones bajos en una línea:

```markdown
---
```

---

## Git y GitHub: Control de Versiones y Repositorios en la Nube

### ¿Qué es Git?

**Git** es un sistema de control de versiones distribuido, de código abierto y gratuito, creado en 2005 por **Linus Torvalds** — el mismo creador del kernel de Linux. Fue diseñado para manejar desde proyectos pequeños hasta proyectos muy grandes con rapidez y eficiencia.

Un sistema de control de versiones permite registrar los cambios realizados en uno o más archivos a lo largo del tiempo, de modo que se puedan recuperar versiones específicas más adelante. Git almacena una "fotografía" del estado de todos los archivos del proyecto cada vez que se confirma un cambio, lo que permite volver a cualquier estado anterior en cualquier momento.

A diferencia de los sistemas centralizados, Git es distribuido: cada desarrollador tiene una copia completa del historial del proyecto en su propia computadora. Esto significa que se puede trabajar sin conexión a internet y que no existe un único punto de fallo.

#### Características principales de Git

- **Distribuido:** cada copia del repositorio contiene el historial completo.
- **Velocidad:** las operaciones locales son casi instantáneas.
- **Integridad:** cada archivo y commit se verifica mediante un hash SHA-1.
- **Ramas (branches):** permite trabajar en múltiples líneas de desarrollo en paralelo.
- **Gratuito y de código abierto:** disponible para Windows, macOS y Linux.

### ¿Qué es GitHub?

**GitHub** es una plataforma web de alojamiento de repositorios Git en la nube, fundada en 2008 y adquirida por Microsoft en 2018. Permite a los desarrolladores almacenar, gestionar y colaborar en proyectos de software de forma remota.

Mientras que Git es la herramienta de control de versiones que funciona localmente en tu computadora, GitHub es el servicio en línea que actúa como servidor remoto para almacenar y compartir esos repositorios.

#### Diferencia entre Git y GitHub

| Característica | Git | GitHub |
|----------------|-----|--------|
| Tipo | Herramienta de software | Plataforma web |
| Función | Control de versiones local | Alojamiento remoto de repos |
| Instalación | Se instala en tu computadora | Se usa desde el navegador |
| Conexión | Funciona sin internet | Requiere internet |
| Creado por | Linus Torvalds (2005) | Tom Preston-Werner (2008) |

### Instalación y Configuración Inicial

Git puede descargarse desde su sitio oficial: [https://git-scm.com/downloads](https://git-scm.com/downloads)

Una vez instalado, se debe configurar el nombre y correo electrónico que aparecerán en cada commit:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@email.com"
```

Para verificar la configuración:

```bash
git config --list
```

### Comandos Esenciales de Git

#### Inicializar y clonar repositorios

| Comando | Descripción |
|---------|-------------|
| `git init` | Crea un nuevo repositorio Git en la carpeta actual |
| `git clone <url>` | Clona un repositorio remoto en tu computadora |

#### Registrar cambios

| Comando | Descripción |
|---------|-------------|
| `git status` | Muestra el estado de los archivos |
| `git add <archivo>` | Agrega un archivo al staging area |
| `git add .` | Agrega todos los archivos modificados |
| `git commit -m "mensaje"` | Confirma los cambios con un mensaje |
| `git log` | Muestra el historial de commits |

#### Sincronizar con repositorio remoto

| Comando | Descripción |
|---------|-------------|
| `git remote add origin <url>` | Vincula el repositorio local con uno remoto |
| `git push` | Sube los commits locales al repositorio remoto |
| `git pull` | Descarga y fusiona los cambios remotos |

### Crear un Repositorio en GitHub y Subir Información

#### Crear el repositorio en GitHub

1. Iniciar sesión en [github.com](https://github.com)
2. Hacer clic en el botón **'+'** y seleccionar **'New repository'**
3. Asignar un nombre al repositorio
4. Elegir si será público o privado
5. Hacer clic en **'Create repository'**

#### Flujo completo para subir un proyecto

```bash
# 1. Inicializar el repositorio local
git init

# 2. Agregar los archivos
git add .

# 3. Hacer el primer commit
git commit -m "chore: primer commit"

# 4. Vincular con GitHub
git remote add origin git@github.com:usuario/repositorio.git

# 5. Subir el código
git push -u origin master
```

#### Flujo de trabajo diario

```bash
# 1. Ver qué cambió
git status

# 2. Agregar los cambios
git add .

# 3. Confirmar con un mensaje
git commit -m "descripción del cambio"

# 4. Subir a GitHub
git push
```

### Mensajes de Commit: Conventional Commits

Una buena práctica es usar prefijos descriptivos en los mensajes de commit:

| Prefijo | Uso |
|---------|-----|
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección de un error |
| `chore:` | Configuración o mantenimiento |
| `docs:` | Cambios en documentación |

---

## Hugo y GitHub Actions: Sitios Estáticos y Publicación Automatizada

### ¿Qué es Hugo?

**Hugo** es un generador de sitios estáticos de código abierto, creado en 2013 por **Steve Francia**. Está escrito en el lenguaje de programación **Go** y es conocido por ser uno de los generadores más rápidos del mundo, capaz de construir un sitio completo en milisegundos.

A diferencia de los gestores de contenido dinámicos como WordPress, Hugo no requiere base de datos ni servidor con procesamiento en tiempo real. En su lugar, genera archivos **HTML, CSS y JavaScript** estáticos a partir de archivos Markdown y plantillas, los cuales pueden alojarse en cualquier servidor o servicio de hosting estático como GitHub Pages.

#### Características principales

- Velocidad de construcción extremadamente rápida.
- No requiere base de datos ni servidor de aplicaciones.
- Contenido escrito en Markdown.
- Gran variedad de temas disponibles en [themes.gohugo.io](https://themes.gohugo.io/).
- Compatible con GitHub Pages, Netlify y otros servicios de hosting estático.

### Crear un sitio estático con Hugo

#### Instalación

Hugo puede descargarse desde su sitio oficial: [https://gohugo.io/installation/](https://gohugo.io/installation/)

En Windows se descarga el binario `hugo.exe` y se agrega al PATH del sistema para poder usarlo desde cualquier terminal.

Para verificar la instalación:

```bash
hugo version
```

#### Comandos esenciales de Hugo

| Comando | Descripción |
|---------|-------------|
| `hugo new site nombre` | Crea un nuevo proyecto Hugo |
| `hugo server` | Inicia un servidor local en `localhost:1313` |
| `hugo` | Construye el sitio y genera los archivos en `/public` |

#### Estructura de un proyecto Hugo

```
mi-sitio/
├── hugo.yaml         # Configuración del sitio
├── content/          # Archivos Markdown con el contenido
├── themes/           # Temas instalados
├── static/           # Imágenes y archivos estáticos
├── layouts/          # Plantillas HTML personalizadas
└── public/           # Sitio generado (no se sube a Git)
```

#### Configuración básica

El archivo `hugo.yaml` controla toda la configuración del sitio:

```yaml
baseURL: "https://usuario.github.io/repositorio/"
languageCode: "es-mx"
title: "Mi Portafolio"
theme: nombre-del-tema
```

#### Instalar un tema

Los temas se instalan como submódulos de Git:

```bash
git submodule add https://github.com/autor/tema themes/nombre-tema
```

Luego se referencia en `hugo.yaml`:

```yaml
theme: nombre-tema
```

#### Subir el proyecto a GitHub

El proceso es igual que con cualquier proyecto de Git. El archivo `.gitignore` debe excluir la carpeta `public/` ya que GitHub Actions la generará automáticamente:

```
public/
*.lock
```

```bash
git add .
git commit -m "feat: sitio Hugo configurado"
git push
```

### ¿Qué es GitHub Actions?

**GitHub Actions** es una plataforma de integración y entrega continua (CI/CD) integrada directamente en GitHub. Permite automatizar flujos de trabajo como compilación y despliegue de proyectos cada vez que ocurre un evento en el repositorio, como un `git push`.

En el contexto de Hugo, GitHub Actions se utiliza para **compilar automáticamente el sitio y publicarlo en GitHub Pages** cada vez que se sube un cambio, sin necesidad de hacerlo manualmente.

#### Conceptos clave

| Término | Descripción |
|---------|-------------|
| **Workflow** | Proceso automatizado definido en un archivo YAML |
| **Job** | Conjunto de pasos que se ejecutan en una máquina virtual |
| **Step** | Acción individual dentro de un job |
| **Trigger** | Evento que dispara el workflow (ej. `push`) |

### Configurar GitHub Actions para publicar en GitHub Pages

#### Estructura del archivo de workflow

Los workflows se definen en archivos `.yaml` dentro de la carpeta `.github/workflows/`:

```
.github/
└── workflows/
    └── hugo.yaml
```

#### Archivo de workflow para Hugo

```yaml
name: Deploy Hugo site to GitHub Pages

on:
  push:
    branches: [master]
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          submodules: true

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build site
        run: hugo --minify

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

#### Proceso completo de publicación automatizada

1. Se realizan cambios en los archivos del proyecto de forma local.
2. Se suben los cambios a GitHub con `git push`.
3. GitHub Actions detecta el `push` y ejecuta el workflow automáticamente.
4. Hugo construye el sitio y genera los archivos estáticos.
5. Los archivos generados se publican en GitHub Pages.
6. El sitio queda disponible públicamente en la URL configurada.

---

## Referencias

- Gruber, J. (2004). *Markdown*. Daring Fireball. https://daringfireball.net/projects/markdown/
- Atlassian. (s.f.). *¿Qué es Git?* Atlassian Git Tutorial. https://www.atlassian.com/es/git/tutorials/what-is-git
- Chacon, S., & Straub, B. (2023). *Pro Git* (2.a ed.). Apress. https://git-scm.com/book/es/v2
- GitHub. (2024). *Crear un repositorio*. GitHub Docs. https://docs.github.com/es/repositories/creating-and-managing-repositories/creating-a-new-repository
- GitHub. (2024). *Introducción a GitHub Actions*. GitHub Docs. https://docs.github.com/es/actions/learn-github-actions/understanding-github-actions
- GitHub. (2024). *Acerca de GitHub Pages*. GitHub Docs. https://docs.github.com/es/pages/getting-started-with-github-pages/about-github-pages
- Hugo Authors. (2024). *Hugo Documentation*. https://gohugo.io/documentation/

## Portafolio y Página estatica

[Portafolio Paradigmas de la Programación](https://github.com/DontBLazy-you/Portafolio_Paradigmas)

[Página Estatica]([google.com](http://localhost:1313/Portafolio_Paradigmas/))