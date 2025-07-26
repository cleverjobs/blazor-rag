# Data binding

## Question

**Igo** asked on 13 Dec 2019

I see that Grid supports binding to INotifyCollectionChanged ([https://demos.telerik.com/blazor-ui/grid/observable-data).](https://demos.telerik.com/blazor-ui/grid/observable-data).) It is wonderful! 1) Is that binding supported in other list controls (ComboBox, DropDownList)? 2) Does Telerik support binding to INotifyPropertyChanged? This question applies to all controls. Добавить в Словарь Новый список слов для Английский -> Русский... Создать новый список слов... Копировать Добавить в Словарь Новый список слов для Английский -> Русский... Создать новый список слов... Копировать Добавить в Словарь Новый список слов для Английский -> Русский... Создать новый список слов... Копировать

## Answer

**Marin Bratanov** answered on 13 Dec 2019

Hi Igor, At the moment, this is only available for the grid. There is also a feature request for the TreeView that you can Vote for and Follow: [https://feedback.telerik.com/blazor/1433824-binding-to-observablecollection.](https://feedback.telerik.com/blazor/1433824-binding-to-observablecollection.) If you would like this implemented in all components, I'd encourage you to post a new public feature request for that so we can gather the community feedback and actual scenarios where that would be needed. At this stage, we are not aware of many cases where such changes are needed for most components, usually the entire data would be replaced and StateHasChanged() should take care of the UI update. Regards, Marin Bratanov

### Response

**Igor** answered on 13 Dec 2019

I have created feature request: [https://feedback.telerik.com/blazor/1446090-data-binding-as-in-wpf-and-xamarin-for-the-all-controls](https://feedback.telerik.com/blazor/1446090-data-binding-as-in-wpf-and-xamarin-for-the-all-controls)
