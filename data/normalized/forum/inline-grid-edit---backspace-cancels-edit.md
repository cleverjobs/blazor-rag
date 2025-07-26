# Inline Grid Edit - Backspace Cancels Edit

## Question

**Bry** asked on 15 May 2024

When editing a text field on a Blazor Grid in inline edit mode, pressing the backspace key will cause the cell edit to cancel, similar to what the escape key does. To reproduce, enter edit mode and press the backspace key, or keep pressing the backspace key until the edit cancels. This is usual behavior since the backspace key is very often used to clear the text before entering new text and it is unexpected when pressing the key causes the edit to suddenly cancel. It there a way to prevent this unwanted behaviour? Bryan

### Response

**Hristian Stefanov** commented on 15 May 2024

Hi Bryan, I tried to recreate the described issue within our Grid - Inline Editing demo. As a result, pressing backspace clears the text and does not seem to close the editing. Maybe I'm missing something from the scenario, so could you share the configuration you are testing with so I can see the behavior firsthand? This will allow me to investigate further and suggest a possible solution. For your convenience, you can send the sample via the REPL platform. I eagerly anticipate hearing back from you. Your cooperation is highly valued. Kind Regards, Hristian
