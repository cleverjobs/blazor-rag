# Mimicking appearance of GridSearchBox in TelerikTextBox

## Question

**Ada** asked on 05 Mar 2025

I have some Grids which are fully managed by the TelerikGrid control (as far as sorting, filtering, and pagination goes). These grids use the Data property on the Grid. These TelerikGrids are using the <GridSearchBox />. I am now building some API-driven grids, which are using the OnRead property. For the API-driven Grids I'm using a TelerikTextBox for searching, instead. I would like this grid to look the same as the managed grids. Is there any way to make the TelerikTextBox look identical to the GridSearchBox? I have followed this example to replace the GridSearchBox with a TelerikTextBox, but the appearance is very different. Blazor Search Grid on Button Click - Telerik UI for Blazor Thank you -Adam

## Answer

**Anislav** answered on 05 Mar 2025

Hi Adam, You can use the built-in GridSearchBox for API-driven grids. I modified the example from the docs, and you can see it working here: [https://blazorrepl.telerik.com/cTOxuflX457hzPxG47.This](https://blazorrepl.telerik.com/cTOxuflX457hzPxG47.This) keeps the appearance consistent with fully managed TelerikGrid. Did you use TelerikTextBox instead because you don’t want the search to trigger while typing? If so, the DebounceDelay parameter of GridSearchBox might help. If you still need to use TelerikTextBox, you can make its look and feel closer (but not identical) to GridSearchBox by: Using a PrefixTemplate to add a search icon Setting ShowPrefixSeparator="false" to remove the | separator between the search icon and the input field Setting Placeholder="Search ..." for a similar input hint Enabling ShowClearButton="true" for an X button to clear input <TelerikTextBox @bind-Value="@SearchValue" OnChange="@SearchGrid" ShowPrefixSeparator="false" Placeholder="Search..." ShowClearButton="true"> <TextBoxPrefixTemplate> <TelerikSvgIcon Icon="@SvgIcon.Search" /> </TextBoxPrefixTemplate> </TelerikTextBox> Regards, Anislav Atanasov

### Response

**Anislav** commented on 24 Mar 2025

Adam, did my suggestions help you?
