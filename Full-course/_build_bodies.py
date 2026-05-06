"""Extract chapter bodies for the unified Fundamentals of NLP PDF."""
import os, re

REPO = r"C:/Users/aymen/Repos/FundamentalsNLP"
OUT  = os.path.join(REPO, "Full-course")

CHAPTERS = [
    ("Chapter 1 - NLP Landscape",                       "chapter1.tex", "ch1.tex"),
    ("Chapter 2 - Text Representation and Evaluation",  "chapter2.tex", "ch2.tex"),
]

def extract_body(src_path: str) -> str:
    with open(src_path, encoding="utf-8") as f:
        text = f.read()
    body = text.split(r"\begin{document}", 1)[1]
    body = body.rsplit(r"\end{document}", 1)[0]
    body = re.sub(r"\\maketitle[^\n]*\n", "", body)
    body = re.sub(r"\\setcounter\{chapter\}\{\d+\}[^\n]*\n", "", body)
    return body.strip() + "\n"

for folder, src_file, dst_file in CHAPTERS:
    src = os.path.join(REPO, "Chapters", folder, src_file)
    dst = os.path.join(OUT, dst_file)
    body = extract_body(src)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(body)
    print(f"  {dst_file}: {body.count(chr(10))} lines extracted from {src_file}")
print("OK")
