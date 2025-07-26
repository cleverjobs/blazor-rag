# Using push Drawer with horizontal scrolling Grid

## Question

**Car** asked on 24 Oct 2022

I'm running into an issue trying to implement a horizontally scrolling grid in the main content of a page alongside a push drawer. From what I understand, scrolling horizontally requires a fixed width TelerikGrid, but using push mode on a drawer requires the same width to not be set. Currently, if I set a fixed width for the grid, it will always remain at that width, regardless of whether the drawer is expanded or closed. If I don't set a width, the grid will expand to its full width and go off the screen, rather than remaining on the screen and expanding/contracting when the drawer is opened or closed. Is there a good way to implement horizontal scrolling in a Telerik Grid while still allowing the grid to increase and decrease in width when the drawer is opened/closed?

### Response

**Greg** commented on 13 Oct 2023

I have a similar problem (also with Grid in Drawer) - when Paging is true the Grid shows horizontal scrollbar but if I set Paging=false the Horizontal scrollbar never appears regardless of column width.

### Response

**Dimo** commented on 17 Oct 2023

@Greg - If Grid paging is disabled, the component will expand vertically, according to the total number of rows. This can move the component's bottom outside the visible viewport area, or the Grid may be clipped by a parent element. Please verify. Here are working examples: Pageable Grid inside a Drawer Non-pageable Grid inside a Drawer In both cases, the Grid suffers from a general CSS problem related to tables inside a flexbox layout. In such cases, the Grid must have a non-percentage width, otherwise it will expand horizontally and will not show a scrollbar. The optimal workaround will vary in each specific scenario. In the above examples, I am using a calc() value for the Grid Width, which depends on the Drawer state.
