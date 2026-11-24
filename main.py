"""One Line of Earned Pride — make.fun bounty u-mang-one-line-of-earned-pride-a0138557.

Entry line (167 chars):
After 214 rejections, the librarian finally shelved her own novel at eye level — and the boy who'd laughed at her drafts last winter asked if he could borrow it first.

Writes exactly that line, with no trailing newline, to /output/entry.txt.
Gate: the line must be 1-240 characters long (it is 167).
"""

LINE = "After 214 rejections, the librarian finally shelved her own novel at eye level \u2014 and the boy who'd laughed at her drafts last winter asked if he could borrow it first."

assert 1 <= len(LINE) <= 240, f"line length {len(LINE)} outside 1-240 gate"
assert len(LINE) == 167, f"line length {len(LINE)} != 167"

if __name__ == "__main__":
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
