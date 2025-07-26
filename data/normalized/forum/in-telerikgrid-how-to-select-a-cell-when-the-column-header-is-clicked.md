# In TelerikGrid, how to select a cell when the column header is clicked?

## Question

**Vit** asked on 22 Apr 2025

I have a TelerikGrid with SelectionMode=Single, so when I click on cell, it becomes selected. Then I click on a header of another column; the header cell gets the focus (and becomes highlighted), but the selected cell does not change. To the user, it looks like there are two selected columns now. Is there a practical way to select the cell at the current row and the focused column when the user clicks on a column header? Maybe detect when a column header gets the focus (without going through JSInterop)? If that is diffucult - can I prevent header cells from getting the focus but keep the ability to resize columns? I can change the header styles to make its focus invisible, but that would be a short-term workaround only. I use Telerik in a Blazor Maui Hybrid application. Thank you.

## Answer

**Anislav** answered on 22 Apr 2025

Here is an example using TelerikGrid with SelectionMode="Single": [https://blazorrepl.telerik.com/QJYIwGuW06Tyh8by34.](https://blazorrepl.telerik.com/QJYIwGuW06Tyh8by34.) However, I’m not able to reproduce the issue you mentioned. Do you notice any differences between the setup of the grid in the example and your code? Regards, Anislav Atanasov

### Response

**Vitaly** commented on 22 Apr 2025

Hi Anislav, Thank you for the example. The error is mine: I forgot to mention that my grid has Navigable="true". When I set this flag in your example, I can use the keyboard to move across the grid (in fact, I can navigate from the grid body into the header, which is weird). And then I can click on the header cell and highlight it. Either way, with or without Navigable, I would like the user to click on a header cell and see the cell in that column to get selected. Would that be possible? I tried hooking up to the focusin event, but I couldn't make it work.

### Response

**Anislav** commented on 22 Apr 2025

From my point of view, it makes sense to allow keyboard navigation to the header cell as well—especially if the grid is sortable. In that case, when the user presses the Enter key, the grid can be sorted by the currently selected header cell.

### Response

**Anislav** answered on 22 Apr 2025

The easiest way to customize this behavior is by overriding the CSS for the focus state of the grid header. You can either set a background color that matches the selected cell in the grid body or remove the borders (shadows) that indicate focus. Most likely, you'll end up removing the borders from the focused header cell as deselecting the currently selected cell in the body when a header cell is clicked would be quite difficult to implement. Here is an example of the CSS: <style>.k-grid.k-table-th:focus,.k-grid.k-table-th.k-focus { box-shadow: none!important;
} </style> Regards, Anislav Atanasov

### Response

**Vitaly** commented on 22 Apr 2025

Sorry, just to confirm. You are saying that - no, it's not possible to have a notification when the header cell is clicked or hit with Space, right? No worries, I'll try to go through Javascript.

### Response

**Anislav** commented on 23 Apr 2025

I’m running out of ideas. I don’t think it’s possible to listen for standard HTML events like onfocus or onkeypress, even if you wrap the table or provide a custom cell template. So it seems JavaScript is the only workaround here. Regards, Anislav Atanasov
