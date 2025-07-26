# "Working" indicator in edit grid popup?

## Question

**And** asked on 15 Jun 2020

I have a Grid with a popup edit window and an Add Item command in the toolbar. When a new item is added, it calls a method that calls several other async tasks which can take 3-4 seconds to complete. Is there a way to modify the Update button on the edit grid popup with some kind of working/processing indicator? As an example of what I've attempted (using Ed Charbeneau's Spinkit): <GridCommandButton Command="Save" Icon="add" ShowInEdit="true" OnClick="@SendNewUserEmail"> <SpinLoader IsLoading="@IsProcessingNewUser"> <LoadingTemplate> <Circle /> Working on it... </LoadingTemplate> <ContentTemplate> Add User </ContentTemplate> </SpinLoader> </GridCommandButton> But this button doesn't appear in the grid popup at all.

## Answer

**Marin Bratanov** answered on 15 Jun 2020

Hi Andrew, The command buttons render only in the rows, and, at the moment, conditional rendering through the context is not available on them (see here ). You may also find interesting this feature for a built-in spinner for data operations although it is likely to work for data loading and not updating. That said, I am logging the issue that the grid does not render the command buttons but separate buttons here: . At this point, I cannot say whether the command buttons will render, or a different approach should be exposed, because technologically, it is extremely likely that the command buttons might not be available for the popup as-is. You can Follow its status here: [https://feedback.telerik.com/blazor/1471845-the-popup-edit-form-renders-its-own-buttons-and-not-the-command-buttons](https://feedback.telerik.com/blazor/1471845-the-popup-edit-form-renders-its-own-buttons-and-not-the-command-buttons) and I've added your Vote for it on your behalf. The workaround I can offer at the moment is to use a custom window for editing, as shown here: [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form.](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form.) Regards, Marin Bratanov
