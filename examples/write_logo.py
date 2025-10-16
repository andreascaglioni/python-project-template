#!/usr/bin/env python3
"""
Generate a simple rectangular SVG logo that fits the text with symmetric padding.

This is intentionally dependency-free (writes plain SVG XML).
Tweak `text`, `font_size`, `padding`, `rx`, and `fill` as needed.
"""

text = "py-project-template"
font_family = "Segoe UI, Roboto, Arial, sans-serif"
font_size = 28  # px
padding = 16  # px on left and right
height = 64  # svg height in px
rx = 6  # corner radius
fill = "#2b6cb0"
text_color = "#ffffff"

# Simple width estimate: average character width ~ 0.6 * font_size
avg_char_width = 0.45 * font_size
text_width = int(len(text) * avg_char_width)

canvas_width = padding * 2 + text_width
# Add a little extra safety margin
canvas_width += 4

text_x = padding
# baseline: approximate vertical position so text sits nicely in the rectangle
text_y = int(height * 0.7)

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{height}" viewBox="0 0 {canvas_width} {height}" role="img" aria-label="python project template logo">
  <rect width="{canvas_width}" height="{height}" rx="{rx}" fill="{fill}" />
  <text x="{text_x}" y="{text_y}" font-family="{font_family}" font-size="{font_size}" fill="{text_color}">{text}</text>
</svg>
"""

print(svg)
