# "multiple" attribute functionality

## Question

**Edw** asked on 30 Oct 2020

I need functionality similar to an html <select> with a "multiple" attribute, i.e. a data-bound listbox that allows multiple selections. I need a pretty standard UI with two listboxes, where you can select one or more items and move to the other listbox. Seems that neither the DropDownList nor MultiSelect can help me there. Any thoughts?

## Answer

**Marin Bratanov** answered on 31 Oct 2020

Hi Edward, The TelerikMultiSelect is the equivalent of a multiple select, and in our latest version it can let you select several items at once without closing (see demo ). If that's not the UX you seek, a grid with multiple selection that has a single column can let you have the listbox appearance. In addition, it will provide all other grid features such as events and filtering, and virtual scrolling. If you don't want them, you can simply keep them disabled, and use a bit of CSS to hide the header if you don't want that either. Regards, Marin Bratanov

### Response

**Edward** answered on 01 Nov 2020

Worked really well for me with a single-column grid and a checkbox column. Thanks!
