"""Gera as imagens PNG (1080x1350) dos posts do LigFlow e da Calutec.

Uso:
    python3 kit/render.py <pasta-do-post>

Renderiza cada arquivo .html da pasta (em ordem alfabetica) para um .png
de mesmo nome. Os HTML seguem os modelos de kit/modelos/ e usam os
marcadores {{LOGO}} (LigFlow) e {{LOGO_CALUTEC}} no lugar do caminho
das logos. A fonte Saira e injetada a partir de kit/fontes/, sem
depender do Google Fonts.

Requer: pip install playwright (e um Chrome/Chromium instalado).
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

KIT = Path(__file__).resolve().parent
LOGO = KIT / "logo-ligflow.png"
LOGO_CALUTEC = KIT / "logo-calutec.png"
FONTES = KIT / "fontes"
CHROME_CANDIDATOS = ["/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]


def font_css() -> str:
    css = ""
    for peso in (500, 600, 700, 800, 900):
        for estilo in ("normal", "italic"):
            f = FONTES / f"saira-latin-{peso}-{estilo}.woff2"
            css += (f"@font-face{{font-family:Saira;font-weight:{peso};font-style:{estilo};"
                    f"src:url('file://{f}') format('woff2')}}\n")
    return css


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    pasta = Path(sys.argv[1]).resolve()
    paginas = sorted(pasta.glob("*.html"))
    if not paginas:
        sys.exit(f"Nenhum .html em {pasta}")

    chrome = next((c for c in CHROME_CANDIDATOS if Path(c).exists()), None)
    css = font_css()
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome, args=["--allow-file-access-from-files"])
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        for html in paginas:
            fonte = html.read_text(encoding="utf-8")
            if "{{" in fonte.replace("{{LOGO}}", "").replace("{{LOGO_CALUTEC}}", ""):
                sys.exit(f"{html.name}: ainda tem marcador {{{{...}}}} sem preencher")
            fonte = fonte.replace("{{LOGO_CALUTEC}}", f"file://{LOGO_CALUTEC}")
            fonte = fonte.replace("{{LOGO}}", f"file://{LOGO}")
            fonte = fonte.replace("</head>", f"<style>{css}</style></head>", 1)
            tmp = html.with_suffix(".render.tmp.html")
            tmp.write_text(fonte, encoding="utf-8")
            page.goto(f"file://{tmp}")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(300)
            if not page.evaluate("document.fonts.check('italic 900 40px Saira')"):
                sys.exit(f"{html.name}: fonte Saira nao carregou")
            png = html.with_suffix(".png")
            page.screenshot(path=str(png), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            tmp.unlink()
            print(f"ok  {png}")
        browser.close()


if __name__ == "__main__":
    main()
