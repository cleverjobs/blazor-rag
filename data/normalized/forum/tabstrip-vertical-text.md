# TabStrip vertical text

## Question

**Had** asked on 21 Jan 2025

Probably a bit of a vague question, but is there any way to make the “TabStrip” component tab texts appear vertically or is it planned to support this behavior sometime? I've tried modifying it a bit via css but I'm having problems with containers. I think I'm probably not using the right component for what I want to achieve... but if it helps anyone who is looking for the same idea it is already reflected here.

## Answer

**Hristian Stefanov** answered on 21 Jan 2025

Hi Hadrian, To make the text inside each tab appear vertically, you can use the following CSS: <style>.k-tabstrip.k-link-text {
writing-mode: vertical-rl; /* Rotate text to vertical layout */ text-orientation: mixed; /* Orient characters naturally */ display: inline-block; /* Ensure proper layout handling */ } </style> <TelerikTabStrip> <TabStripTab Title="First"> First tab content. </TabStripTab> <TabStripTab Title="Second"> Second tab content. </TabStripTab> <TabStripTab Title="Third"> Third tab content. </TabStripTab> </TelerikTabStrip> Additionally, upon interest, here are the available built-in tab position settings: TabStrip - Position and Alignment. Regards, Hristian Stefanov Progress Telerik
