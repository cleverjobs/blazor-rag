# Incell Editing... Navigation is difficult

## Question

**Jef** asked on 23 Nov 2020

To give some background, I'm looking at this from the perspective of using the grid in a similar fashion as Excel. My users will click on a cell in the row and then from there navigate via the keyboard or mouse. If you go to the Grid - Incell Editing demo page and click into the first editable column (Weight) and then hit tab, the focus leaves the grid entirely (not desireable). Also, if you are in the Weight field and mouse click into the field immediately to the right (Color) the current active cell flashes but then stays in focus. It's a bit of a mess. My intent is to have a grid that expert users can navigate quickly using the keyboard with little mouse input. Is Inline editing a better option? Can I leverage a row-click event to bring the row in edit mode? Can navigating away from the row trigger an automatic update? Or what about hitting tab in the last editable cell? Can we have it automatically add a new row and enter edit mode on the new row? The users would revolt against having to click and Edit button and a Save button on each row.

## Answer

**Marin Bratanov** answered on 24 Nov 2020

Hello Jeffrey, You can follow the implementation of a faster navigation like that here: [https://feedback.telerik.com/blazor/1454022-incell-editing-keyboard-navigation-to-be-closer-to-excel-more-flexibility-on-opening-cells-for-editing-and-moving-between-them-with-fewer-actions.](https://feedback.telerik.com/blazor/1454022-incell-editing-keyboard-navigation-to-be-closer-to-excel-more-flexibility-on-opening-cells-for-editing-and-moving-between-them-with-fewer-actions.) It will probably be a separate editing mode. I've also added your Vote to it to raise its priority. Regards, Marin Bratanov
