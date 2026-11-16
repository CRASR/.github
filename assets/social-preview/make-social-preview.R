# Make a 1280x640 social-preview PNG for a CRASR repo.
# Usage (from this folder):
#   Rscript make-social-preview.R <repo-name> "<one-line description>" [out.png]
# Upload the result at: repo Settings > General > Social preview.

args  <- commandArgs(trailingOnly = TRUE)
title <- args[1]
desc  <- args[2]
out   <- if (length(args) > 2) args[3] else paste0(title, "-social-preview.png")

esc <- function(x) {
  x |>
    gsub("&", "&amp;", x = _, fixed = TRUE) |>
    gsub("<", "&lt;", x = _, fixed = TRUE) |>
    gsub(">", "&gt;", x = _, fixed = TRUE)
}

# Description wraps to at most three lines
desc_lines <- strwrap(desc, width = 56)
if (length(desc_lines) > 3) warning("Description is longer than three lines; extra text dropped.")
desc_lines <- c(desc_lines, "", "")[1:3]

fills <- c(TITLE = title, DESC1 = desc_lines[1], DESC2 = desc_lines[2], DESC3 = desc_lines[3])

svg <- readLines("social-preview-template.svg", warn = FALSE) |> paste(collapse = "\n")
for (k in names(fills)) svg <- sub(paste0("{{", k, "}}"), esc(fills[[k]]), svg, fixed = TRUE)

rsvg::rsvg_png(charToRaw(svg), out, width = 1280, height = 640)
message("Wrote ", out)
