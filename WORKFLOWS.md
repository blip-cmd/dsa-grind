# dsa-grind Workflow
- When the user shares a problem-solving snippet, create a new file in the appropriate folder.
- If the same problem/file already exists in dsa-grind, replace it instead of adding a duplicate.
- Keep a `times_solved` counter at the bottom of the file.

# Standard Challenge File Structure
- Start with any platform-provided definitions as comments, such as `ListNode`.
- Put the main accepted solution first using the platform style, usually `class Solution(object)`.
- Preserve the user's own solution style and variable names when they solved it themselves.
- Add optional learning helpers after the solution only when useful, but do not run them automatically.
- Add local helper classes/functions after the solution, such as `ListNode` and builders for tests.
- Add runnable test cases inside `if __name__ == "__main__":`.
- Use simple printed output plus `assert` statements for test verification.
- Keep optional simulators or walkthrough tools commented inside the `__main__` block.
- Keep metadata at the bottom of the file in this order:
  - `times_solved = N`
  - `# Difficulty: ...`
  - problem URL
  - `# key: ...`
  - `# notes: ...`

# Mentorship Style
- Be my mentor and guide.
- When I solve something myself, prioritize my version and explain only the key idea or improvement.
- Help me move fast on new challenges by applying the standard structure without asking again.
