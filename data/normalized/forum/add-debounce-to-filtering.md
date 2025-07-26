# Add Debounce to filtering

## Question

**Way** asked on 12 Feb 2021

Can you add Debounce to the filtering, JS events are painfully slow in Blazor and too many can overwhelm the UI.

## Answer

**Marin Bratanov** answered on 16 Feb 2021

Hello Wayne, You can use the OnRead to implement custom filtering and also debounce the operations: [https://docs.telerik.com/blazor-ui/components/combobox/events#onread](https://docs.telerik.com/blazor-ui/components/combobox/events#onread) and the particular example the article links is shown here: [https://docs.telerik.com/blazor-ui/knowledge-base/combo-debounce-onread.](https://docs.telerik.com/blazor-ui/knowledge-base/combo-debounce-onread.) I also made the following feature request where you can Follow a built-in feature for this: [https://feedback.telerik.com/blazor/1507143-add-debounce-to-dropdowns-filtering](https://feedback.telerik.com/blazor/1507143-add-debounce-to-dropdowns-filtering) Regards, Marin Bratanov
