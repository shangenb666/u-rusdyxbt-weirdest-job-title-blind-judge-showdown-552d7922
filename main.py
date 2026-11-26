"""Write the entry job title for make.fun's "Weirdest Job Title" bounty.

The entry is one job title, 60 characters or fewer, the weirdest the
entrant could think of: a role nobody asked for, held by nobody, and
somehow still essential — someone has to mind the plant, even now.
This program writes that title to entry.txt in the output directory,
deterministically: the same title, byte for byte, on every run.
Standard library only; no network.
"""

import os

LINE = "Junior Assistant to the Office Plant (Deceased)"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 60:
        raise ValueError("job title must be 1 to 60 characters")
    if not LINE.strip():
        raise ValueError("job title must not be only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run. The file we create gets mode 0644 below,
    # which is all make.fun needs to collect it.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
