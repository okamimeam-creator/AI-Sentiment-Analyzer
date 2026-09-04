"""Apply the modern visual enhancement layer to the sentiment analyzer UI."""

from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
HTML_PATH = PROJECT_DIR / "index.html"
CSS_PATH = PROJECT_DIR / "style.css"
START_MARKER = "/* BEGIN update_ui.py enhancements */"
END_MARKER = "/* END update_ui.py enhancements */"


ENHANCEMENT_CSS = f"""
{START_MARKER}
/* Add shared theme tokens for the glassmorphism enhancement layer. */
:root {{
  --glass-surface: rgba(255, 255, 255, 0.72);
  --glass-border: rgba(255, 255, 255, 0.8);
  --glass-shadow: 0 24px 70px rgba(44, 38, 112, 0.14);
  --purple-gradient: linear-gradient(135deg, #665dff 0%, #4437ad 52%, #282464 100%);
}}

/* Add soft ambient color behind the existing page without changing its structure. */
body {{
  background:
    radial-gradient(circle at 86% 8%, rgba(126, 117, 255, 0.18), transparent 25rem),
    radial-gradient(circle at 7% 60%, rgba(69, 169, 247, 0.12), transparent 23rem),
    var(--canvas);
}}

/* Turn existing panels and the process area into translucent glass cards. */
.panel,
.how-it-works {{
  background: var(--glass-surface);
  border-color: var(--glass-border);
  box-shadow: var(--glass-shadow);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
}}

/* Use a richer purple gradient for the hero and primary actions. */
.hero {{
  background: var(--purple-gradient);
}}

.primary-button {{
  background: linear-gradient(135deg, #756cff, #5147df);
  box-shadow: 0 10px 24px rgba(81, 71, 223, 0.22);
}}

.primary-button:hover {{
  background: linear-gradient(135deg, #8179ff, #5c51eb);
  box-shadow: 0 14px 28px rgba(81, 71, 223, 0.3);
}}

/* Add consistent motion to interactive controls while respecting reduced motion. */
.example-chip,
.member-tag,
.brand,
.primary-button {{
  transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease,
    background 180ms ease, color 180ms ease;
}}

.example-chip:hover,
.member-tag:hover {{
  transform: translateY(-2px);
  border-color: #aaa5ff;
  box-shadow: 0 8px 18px rgba(81, 71, 223, 0.12);
}}

/* Improve small-screen spacing and keep cards readable on narrow viewports. */
@media (max-width: 760px) {{
  .panel,
  .how-it-works,
  .project-details {{
    box-shadow: 0 16px 40px rgba(44, 38, 112, 0.1);
  }}
}}

@media (prefers-reduced-motion: reduce) {{
  .example-chip,
  .member-tag,
  .brand,
  .primary-button {{
    transition: none;
  }}
}}
{END_MARKER}
"""


def read_ui_files() -> tuple[str, str]:
    """Read the existing UI files before applying any enhancement."""
    html = HTML_PATH.read_text(encoding="utf-8")
    css = CSS_PATH.read_text(encoding="utf-8")
    return html, css


def update_stylesheet(css: str) -> str:
    """Replace an earlier enhancement block so repeated runs stay idempotent."""
    start = css.find(START_MARKER)
    end = css.find(END_MARKER)

    if start != -1 and end != -1 and end >= start:
        end += len(END_MARKER)
        return f"{css[:start].rstrip()}\n\n{ENHANCEMENT_CSS.strip()}\n{css[end:].lstrip()}"

    return f"{css.rstrip()}\n\n{ENHANCEMENT_CSS.strip()}\n"


def main() -> None:
    # Read both source files and fail clearly if the expected UI files are absent.
    html, css = read_ui_files()
    if "<html" not in html or ":root" not in css:
        raise ValueError("Expected existing index.html and style.css content was not found.")

    # Preserve index.html exactly; all visual enhancements are layered through CSS.
    HTML_PATH.write_text(html, encoding="utf-8")

    # Apply or refresh the marked CSS enhancement block without duplicating it.
    CSS_PATH.write_text(update_stylesheet(css), encoding="utf-8")
    print(f"Updated {HTML_PATH.name} and {CSS_PATH.name}.")


if __name__ == "__main__":
    main()
