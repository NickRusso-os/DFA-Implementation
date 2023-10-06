# Email Format Checker (DFA Implementation)

A Deterministic Finite Automaton (DFA) that checks if the provided string conforms to NJIT's email format.

## Functionality

The DFA checks the format of emails based on the following rules:
1. The email starts with alphabets.
2. It can contain numbers and alphabets before '@'.
3. It should contain a '@' followed by alphabets, numbers, or '.'.
4. If the email contains '.edu' as the domain, it is accepted.

## How to Use

1. Run the program.
2. When prompted, decide whether you want to enter a string with `y` or `n`.
    - If `n` is chosen, the program will exit.
    - If `y` is chosen, the user will be prompted to enter a string over Σ (the alphabet).
3. Enter the string and the program will provide immediate feedback for each letter processed.
4. At the end, the program will indicate whether the string is "Accepted" (conforms to the email format) or "Rejected".

## Alphabet Definitions
- `Σ`: The entire set of characters which includes numbers (0-9), alphabets (a-z), '.', and '@'.
- `upsilon`: Numbers 0-9.
- `psi`: Alphabets a-z.
- `delta`: '.' character.
- `theta`: '@' character.

## Notes
- The DFA transitions and states are printed out for each character processed for clarity.
- The program continues to prompt the user to input strings until they choose to exit by entering `n`.
