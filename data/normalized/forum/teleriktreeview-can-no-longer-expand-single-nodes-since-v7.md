# TelerikTreeView can no longer expand single nodes since v7

## Question

**Jos** asked on 29 Jan 2025

Hello, We recently upgraded to Telerik v7.0 for our controls and since then expanding a single item always expands all items. Has anyone else run into this or does anyone know a workaround?

### Response

**Joseph** commented on 29 Jan 2025

Reverting back to Telerik v6.2 did resolve the issue, FYI.

### Response

**Anislav** commented on 08 Mar 2025

I am unable to reproduce the issue. I created a REPL page with a TelerikTreeView sample using Telerik UI for Blazor version 7.0: REPL link. When I click on an item, only that item expands as expected. Could you provide a sample that reproduces the issue?
