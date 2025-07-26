# Keyboard issues with linked ListBox components

## Question

**Mik** asked on 20 Nov 2024

I've run into some keyboard issues when using 2 list box components. Here are my concerns: 1. There should be a consistent tab order. Right now, it is inconsistent. Going to the Repl below illustrates what I mean. Basically, starting with focus on the left box, I would expect that hitting tab would set focus to the toolbar associated with the left listbox. Instead it sets focus to the toolbar associated with the right listbox. Hitting tab again, then focuses the right listbox. Essentially, for me to access the left listbox's tool bar, I need to hit shift-tab when on the left listbox. There is also an inconsistency where sometimes, if I shift-tab too far back, and then tab back again, it bypasses the toolbars altogether and just switches focus from the left listbox to the right listbox. I think this behavior may occur if the right listbox doesn't have a selected item yet, but it is very inconsistent as to tabbing behavior. 2. The keyboard shortcut for transfer from the left listbox to the right listbox is fine using ctrl-right arrow. This is intuitive. However, in order for me to move something back, I need to set focus to the right listbox, then select the item, then set focus back to the left listbox, and then hit ctrl-left arrow. I would have expected that I would be able to just set focus to the right listbox, select the correct item to transfer back, and then hit ctrl-left arrow, to move it back. The current method is not very intuitive, nor very accessible, since it adds more keystrokes to the process. It doesn't really make sense to have to set focus back to the box that will receive the transfer. Here a repl illustrating both issues: [https://blazorrepl.telerik.com/wIbPmOOl37nH3xJC51](https://blazorrepl.telerik.com/wIbPmOOl37nH3xJC51) Please let me know if there are any workarounds for either of these issues.

## Answer

**Hristian Stefanov** answered on 22 Nov 2024

Hi Mike, Let me address both of your questions below: #1: The ListBox toolbar offers a positioning option, such as placing it to the right of the ListBox. However, regardless of the chosen position, the toolbar's HTML element is rendered in the DOM before the ListBox itself. This means that when tabbing through, the focus will follow the DOM sequence, moving to the toolbar of the right ListBox after the left ListBox. This behavior is expected based on the rendering order. #2: Regarding the focus behavior, you are correct—this is a bug in the ListBox's keyboard navigation. The focus should remain on the moved item to allow reverse actions without any additional steps. I’ve submitted a public bug report on your behalf in our feedback portal: When using the keyboard navigation to move an item between two ListBox components, the focus is not retained on the moved item, which prevents reverse action. You are automatically subscribed to this item as its creator and will receive email notifications about future updates. As a token of appreciation for bringing this to our attention, I’ve credited your account with Telerik points. Regards, Hristian Stefanov Progress Telerik

### Response

**Mike** commented on 22 Nov 2024

Thanks for the response and for adding a bug to the

### Response

**Hristian Stefanov** commented on 27 Nov 2024

Hi Mike, After reviewing the behavior and the current design carefully again, I agree that the focus should align with the visual representation of the elements. To address this, I have submitted a task to our accessibility team for enhancement, and it will be resolved in a future release. Thank you for your input. Kind Regards, Hristian

### Response

**Mike** commented on 27 Nov 2024

Hi Hristian, Thanks for the response and making the decision to change the design. Is there a link to the task on the

### Response

**Hristian Stefanov** commented on 28 Nov 2024

Hi Mike, Here is the public item for this: [Accessibility] Align Toolbar DOM Position with Visual Placement Relative to ListBox to Ensure Tab Order Matches Rendered Sequence. You will receive email notifications for future status updates for this item as well. Kind Regards, Hristian
