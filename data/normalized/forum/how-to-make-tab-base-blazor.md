# How to make Tab base blazor

## Question

**LeeLee** asked on 08 Jul 2024

Hello! I want to create a Blazor WebAssembly application with the following program structure:
When clicking on menu items, I'd like tabs to be generated with the displayed Page Name and a close button in the tab header, and the page content displayed in the tab body. How should I structure this? Menu Tab header - Display of the clicked Page Name and a close button Tab body - Display of Page Content

## Answer

**Hristian Stefanov** answered on 11 Jul 2024

Hi Lee, To achieve the desired structure, use our TabStrip component, and for the menu items, use our Menu. Then: Within the TabStripTab tag, display the page content. Within the HeaderTemplate, display the page name and a close button, as shown in this knowledge base article. Regards, Hristian Stefanov Progress Telerik
