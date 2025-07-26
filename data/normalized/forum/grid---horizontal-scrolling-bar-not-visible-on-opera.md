# Grid - Horizontal scrolling, bar not visible on Opera.

## Question

**Dor** asked on 03 Jan 2024

Hello, I have problem with horizontal scrollbar on grid - it works ok on all browser except Opera. It seems that it exists (when i press and drag mouse on scroll area it moves grid) but is invisible. The same problem occurs even on example: [https://demos.telerik.com/blazor-ui/grid/scrolling](https://demos.telerik.com/blazor-ui/grid/scrolling) That's how it looks on Opera: I have the latest version of Opera: 106.0.4998.19 (chromium version:120.0.6099.130). I've also check on version 105.0.4970.60. Is there anything that i can do with that? Thanks for help.

## Answer

**Hristian Stefanov** answered on 03 Jan 2024

Hi Dorian, Indeed, there is an issue with the horizontal scroll. After a thorough investigation, I can confirm that this is a bug originating from the Opera browser itself. It's worth noting that this behavior is not exclusive to Telerik components; it occurs with a standard HTML "div" element as well. Here is an example illustrating this behavior with "div": REPL link. For additional insights, you can find a relevant discussion on the Opera official forum titled "Horizontal scroll bar is not visible". Workaround To address this, a potential workaround involves utilizing custom CSS to style the scrollbar, as demonstrated in the second comment of the forum link provided above. Regards, Hristian Stefanov Progress Telerik
