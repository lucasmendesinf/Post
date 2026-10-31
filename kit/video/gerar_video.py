"""Gera o video vertical (1080x1920, 30 fps, MP4) de domingo a partir de um roteiro JSON.

Uso:
    python3 kit/video/gerar_video.py <roteiro.json> <saida.mp4> [--musica arquivo.mp3]

O roteiro descreve as cenas (ver kit/video/exemplo-roteiro.json). A pagina
kit/video/video.html anima as cenas em funcao do tempo; este script grava
quadro a quadro com o Chrome (Playwright) e monta o MP4 com o ffmpeg.

A musica padrao e kit/video/musica.m4a (faixa do video de referencia do Lucas),
embutida no proprio arquivo para sair igual no Reels e nos stories. Se o video
for mais longo que a faixa, ela repete; no fim entra um fade-out. Use
--musica para outra faixa ou --sem-musica para gerar sem audio.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

VIDEO_DIR = Path(__file__).resolve().parent
KIT = VIDEO_DIR.parent
FPS = 30
CHROME_CANDIDATOS = ["/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]
TEMAS = {
    "ligflow": {"cor": "#EE3124", "logo": KIT / "logo-ligflow-transparente.png"},
    "calutec": {"cor": "#FD5002", "logo": KIT / "logo-calutec-transparente.png"},
}


def font_css() -> str:
    css = ""
    for peso in (500, 600, 700, 800, 900):
        for estilo in ("normal", "italic"):
            f = KIT / "fontes" / f"saira-latin-{peso}-{estilo}.woff2"
            css += (f"@font-face{{font-family:Saira;font-weight:{peso};font-style:{estilo};"
                    f"src:url('file://{f}') format('woff2')}}\n")
    return css


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roteiro")
    ap.add_argument("saida")
    ap.add_argument("--musica", default=str(VIDEO_DIR / "musica.m4a"))
    ap.add_argument("--sem-musica", action="store_true")
    args = ap.parse_args()

    roteiro = json.loads(Path(args.roteiro).read_text(encoding="utf-8"))
    tema = TEMAS[roteiro.get("tema", "ligflow")]
    roteiro["cor"] = tema["cor"]
    roteiro["logo"] = f"file://{tema['logo']}"
    total = sum(c["duracao"] for c in roteiro["cenas"])
    if not 10 <= total <= 60:
        sys.exit(f"Duracao total {total}s fora do intervalo 10-60s")

    html = (VIDEO_DIR / "video.html").read_text(encoding="utf-8")
    html = html.replace("</head>", f"<style>{font_css()}</style></head>", 1)
    html = html.replace("<script>", "<script>window.ROTEIRO = " + json.dumps(roteiro, ensure_ascii=False) + ";</script>\n<script>", 1)
    tmp = Path(args.saida).with_suffix(".render.tmp.html")
    tmp.write_text(html, encoding="utf-8")

    saida = Path(args.saida)
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "image2pipe", "-vcodec", "mjpeg", "-framerate", str(FPS), "-i", "-"]
    if not args.sem_musica:
        if not Path(args.musica).exists():
            sys.exit(f"Musica nao encontrada: {args.musica}")
        cmd += ["-stream_loop", "-1", "-i", args.musica, "-map", "0:v", "-map", "1:a",
                "-c:a", "aac", "-b:a", "160k", "-t", f"{total}",
                "-af", f"afade=t=in:st=0:d=0.3,afade=t=out:st={max(total - 1.5, 0)}:d=1.5"]
    cmd += ["-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart", str(saida)]

    chrome = next((c for c in CHROME_CANDIDATOS if Path(c).exists()), None)
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=chrome, args=["--allow-file-access-from-files"])
            page = browser.new_page(viewport={"width": 1080, "height": 1920})
            page.goto(f"file://{tmp.resolve()}")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(400)
            if not page.evaluate("document.fonts.check('800 40px Saira')"):
                sys.exit("Fonte Saira nao carregou")
            frames = int(round(total * FPS))
            for i in range(frames):
                page.evaluate(f"renderAt({i / FPS})")
                ff.stdin.write(page.screenshot(type="jpeg", quality=92))
                if i % (FPS * 5) == 0:
                    print(f"  {i / FPS:4.1f}s / {total}s", flush=True)
            browser.close()
    finally:
        ff.stdin.close()
        ff.wait()
        tmp.unlink(missing_ok=True)
    if ff.returncode != 0:
        sys.exit("ffmpeg falhou")
    print(f"ok  {saida}  ({total}s)")


if __name__ == "__main__":
    main()
