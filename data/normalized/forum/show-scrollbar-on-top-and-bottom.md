# Show Scrollbar on top and bottom

## Question

**Nic** asked on 05 Jan 2021

Hello! Currently the horizontal scrollbar is only visible at the bottom. Is there a way to make it visible at the top too? Thank you and best regards Nico

## Answer

**Marin Bratanov** answered on 05 Jan 2021

Hello Nico, The only way to do that would be to have the grid have a fixed Width (say, a certain value in pixels) and to have its parent produce a scrollbar. Then, if you can show that scrollbar at the top instead of at the bottom you could achieve such behavior. What I can suggest you consider instead is that you create such a layout that the entire grid (including its footer) is always visible (which also means setting an appropriate Height to the grid, such as a small enough value in pixels, or 100% so that it can fill up the layout) so that the user can always see all the scrollbars. Regards, Marin Bratanov
