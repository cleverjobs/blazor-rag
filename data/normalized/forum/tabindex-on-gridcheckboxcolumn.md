# TabIndex on GridCheckboxColumn

## Question

**Kev** asked on 26 Sep 2023

Checkbox shows default tabindex="-1" but would like for users to be able to tab through grid

### Response

**Fabian** commented on 17 Oct 2023

This is an issue for our users too. It is the only column that, due to its content and the tabindex for every column being '-1', can not be reached via the tab-key.

## Answer

**Dimo** answered on 19 Oct 2023

Hello, Our components represent a single tab stop. This means that users move from one component to another with Tab, and use other keys to navigate inside a specific component. Tabbing during Grid editing is one of the few exceptions to the above rule. This is the reason why our keyboard navigation doesn't support tabbing from one selection checkbox to another. The expected workflow for selection is: Select rows with Space and optional modifier keys OR Focus the desired checkbox cell with the arrow keys Hit Enter to focus the checkbox itself Hit Space to (un)select the row Hit Esc to focus the cell and be able to navigate elsewhere The second algorithm is similar to in-cell editing. If tabbing across checkboxes is a must, then a possible workaround is to use a non-checkbox column with a <Template>. Render checkboxes inside the template with the desired tabindex, and manage the selection process completely manually. Regards, Dimo Progress Telerik
