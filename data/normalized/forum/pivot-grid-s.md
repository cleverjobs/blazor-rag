# Pivot grid ?s

## Question

**Dea** asked on 28 Jun 2023

1] Can you export the gird? 2] How does one expand the columns to fit the header texts? see example.

## Answer

**Nadezhda Tacheva** answered on 30 Jun 2023

Hi Deasun, I just responded to your private ticket on this matter. I am adding the information here as well for visibility. Export to Excel The export functionality is not currently available for the PivotGrid. While it may have some similarities with the Grid component, the PivotGrid differs on many levels in terms of rendering and behavior. We will expose such an option in a future version of the product. I see you already voted for the item. You may as well follow the public request here to be notified of its status updates: PivotGrid - Export to Excel===Expand columns In v1 of the PivotGrid there is currently no built-in option to control the width of the columns and expand them to ensure the whole content will be visible. We will expose such an option in the upcoming 4.4 version of UI for Blazor: Column Width My recommendation is to use this built-in way for setting the width of columns when available as configuring it with CSS might be tricky and can lead to breaking the component layout and rendering. Regards, Nadezhda Tacheva
