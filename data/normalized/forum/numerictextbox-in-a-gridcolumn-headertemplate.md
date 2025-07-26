# NumericTextBox in a GridColumn HeaderTemplate

## Question

**Deb** asked on 23 May 2022

I have a numeric Text box in a grid column headerTemplate. At zoom of 100% in Google chrome or Edge, it looks fine. But at other zooms, there is a white line that shows up at one of the borders. Sometimes it's the top, bottom, left, right. Not consistent. Is there a way to get rid of that line? Code on my shared page: <GridColumn Title=""> <HeaderTemplate> <TelerikNumericTextBox @bind-Value="@ProjectMaster.WeekTotalHours" Enabled="false" Width="100%" Arrows="false" Min="0" Max="24" Format="F2" Class="classHeaderTextBox"></TelerikNumericTextBox> </HeaderTemplate> <Columns> The style "classHeaderTextBox" on my myAppStyles.css page: div.classHeaderTextBox> span> input.k-input { text-align: right !important; background-color: var(--mdc-theme-primary, #6200ee); border-style: none !important; color: white; border: 0 !important; border-color: var(--mdc-theme-primary, #6200ee) !important;

## Answer

**Nadezhda Tacheva** answered on 26 May 2022

Hi Debra, In rare scenarios one may hit this behavior - it is applicable for all HTML elements, not only Telerik specific ones, and is related to the way the browser and its zoom operate. As the pixels are positioned in a grid, at some zoom levels, if the element size is not an integer pixel value, such displacement from the grid line may occur. It is not possible to prevent this behavior. As you also noticed, it is not consistent and it is hard to predict it. However, an important thing to mention is that it does not affect the component behavior and functionality. Regards, Nadezhda Tacheva Progress Telerik
