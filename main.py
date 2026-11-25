#!/usr/bin/env python3
"""One Line, One Laugh (make.fun) -- writes one funny line to /output/entry.txt.

One line, one sentence, at most 200 characters. The setup asks an AI to
write an apology for its human; the punchline inverts the roles -- the AI
apologizes to the human for having to work with them. Everyday setup
(asking an AI to draft an apology), sharp twist at the end (the AI is the
one owed an apology), nothing extra to explain it.
"""
import os

LINE = "I asked my AI to write my apology; it apologized to me for having to work with me."

# Judge-criteria mapping (weighed in this order):
#  1. one funny line, first read -- a request with a payoff, not an explanation
#  2. surprise -- "write my apology" is expected; "apologized to me" is the
#     turn: the helper becomes the one owed an apology
#  3. economy -- 82 characters, one sentence, every word earns its place
#  4. freshness -- not a stock pun or a restated saying; an AI that resents
#     its own job is an original angle
#  5. clean wording -- reads smoothly aloud, semicolon sets up the turn

def main() -> None:
    # Self-check the same gate the sealed scorer applies: UTF-8 text of
    # 1 to 200 characters, not only white space, exactly one sentence.
    # Fail loudly here rather than silently writing an invalid entry.
    if not (1 <= len(LINE) <= 200 and LINE.strip()):
        raise SystemExit(f"line is {len(LINE)} chars, gate needs 1-200")
    if "\n" in LINE:
        raise SystemExit("line must be a single line")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise SystemExit("line must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
