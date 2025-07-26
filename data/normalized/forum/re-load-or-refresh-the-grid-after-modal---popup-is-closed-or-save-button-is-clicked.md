# Re-Load or Refresh the grid after Modal - Popup is Closed or Save button is clicked

## Question

**Vis** asked on 15 Sep 2020

Blazor : How I can Re-Load or Refresh the grid after Modal - Popup is Closed or Save button is clicked? I am calling the Save Action in Modal-Popup page and not using EventCallback method

## Answer

**Marin Bratanov** answered on 15 Sep 2020

Hello Vishnu, If you are referring to the built-in popup edit form - the application code must update the view-model with the new data so that it can be reflected in the grid. You can find examples in the PopUp editing documentation. In general, if you want to refresh the grid data, there are a couple of standard framework approaches that you can read about in this KB article: Refresh Grid On custom modal popups - please review the linked articles from the Important Notes section of the Window documentation. They explain how the window is no longer in the same sibling context and how to update the rest of the comopnents you need an event that will call .StateHasChanged (which is, usually, an EventCallback and if you can't use an EventCallback you should try to, or at least try to invoke StateHasChanged in the context of the component you wish to update). Regards, Marin Bratanov

### Response

**Vishnu** answered on 15 Sep 2020

Thanks Marin...
