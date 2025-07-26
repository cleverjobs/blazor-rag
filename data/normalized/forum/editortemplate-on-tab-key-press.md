# EditorTemplate on TAB key press

## Question

**Cip** asked on 29 Sep 2020

Hello, I'm using the EditorTemplate where I have TelerikNumericTextBox. When I press TAB key the NumercTextBox does not disappear, but there it would be something else that I would like to achieve, when I press TAB key the value of that input should be saved and the user should go to the next input. If the row ends then the user should go to the first editable input from the next row. Is this possible to achieve somehow? Thank you, Cipri

## Answer

**Marin Bratanov** answered on 29 Sep 2020

Hi Cipri, This will probably arrive first in the grid: [https://feedback.telerik.com/blazor/1454022-incell-editing-keyboard-navigation-to-be-closer-to-excel-more-flexibility-on-opening-cells-for-editing-and-moving-between-them-with-fewer-actions.](https://feedback.telerik.com/blazor/1454022-incell-editing-keyboard-navigation-to-be-closer-to-excel-more-flexibility-on-opening-cells-for-editing-and-moving-between-them-with-fewer-actions.) You can also try the information from the comments on capturing custom keyboard events (a built-in feature is unlikely to work for custom editors anyway) and a sample from this thread on focusing the input faster and you can use that to save data if waiting for the OnUpdate event is not fast enough for you. If you use the grid, you would also be able to use its state to set the edited item/field, but the treelist does not expose that yet. Depending on the data you have, you may be able to use the grid, though - if there isn't deep nesting the detail template may help (see also this article ). Regards, Marin Bratanov
