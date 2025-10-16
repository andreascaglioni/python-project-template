"""
Generate the py-project-template logo.
"""

# SETTINGS
text = "py-project-template"
font_family = "Segoe UI, Roboto, Arial, sans-serif"
font_size = 28  # in px
padding = 16  # on left and right
height = 64  # final image height in px
rx = 6  # corner radius
fill = "#2b6cb0"
text_color = "#ffffff"

# GENERATE
text_width = int(len(text) * 0.45 * font_size)  # Simple width estimate
canvas_width = padding * 2 + text_width

text_x = padding  # horizontal text position
text_y = int(height * 0.7)  # vertical text position

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{height}" viewBox="0 0 {canvas_width} {height}" role="img" aria-label="python project template logo">
  <rect width="{canvas_width}" height="{height}" rx="{rx}" fill="{fill}" />
  <text x="{text_x}" y="{text_y}" font-family="{font_family}" font-size="{font_size}" fill="{text_color}">{text}</text>
</svg>
"""

print(svg)
