# The Core Concept: Reassigning a Label vs. Mutating an Object

In Python, the variable name head is not the actual node object itself. It is just a pointer, or a label, attached to that object in memory.

When you write head = head.next, you are not changing the linked list structure. You are simply sliding your local label forward to point to the next node.

Why it broke your second loop: Because you moved your local label head all the way to the end of the list, your second loop had no way to know where the front of the list was anymore.

Why it doesn't change the global state: The nodes themselves and their .next links remain completely untouched in memory.

A Concrete Analogy
Imagine a line of people holding hands.

You are standing outside the line, pointing your finger at the first person. Your finger is the variable head.

If you move your finger to point at the second person (head = head.next), the first person doesn't disappear, and they don't stop holding hands with the second person. The line hasn't changed at all. You just changed where your finger is pointing.

However, if you can no longer remember who the first person was because you stopped pointing at them, you can never get back to the start of the line.

How to protect the start of the line
To solve this, we create a second finger (curr).

Python
curr = head  # Now both 'head' and 'curr' point to the first node
Inside your loop, you move curr forward (curr = curr.next). Your curr finger slides down the line to collect the values, while your head finger stays perfectly locked onto the very first node.

When the first loop finishes, head is still pointing safely at the beginning, allowing you to reset and start your second pass.
